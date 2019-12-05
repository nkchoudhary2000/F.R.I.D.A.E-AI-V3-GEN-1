import sublime
import sublime_plugin, re

def make_rows(self, edit):
  try:
    sels = self.view.sel()
    input = ''
    printPage = ''
    count = 0
    netRow = ""
    count = False
    joinLabel = " "
    lastNet = ""
    netLabel = []
    netTemp = ""
    for sel in sels:
      input = self.view.substr(sel)
      input = re.sub("\t+", " ", input)
      input = re.sub("\n +\n", "\n\n", input)
      input = re.sub("\n{2,}", "\n", input)
      input = input.strip().split("\n")
      

      for eachRow in input:
        eachRow = eachRow.split(' ', 1)
        nets = re.findall(r'\w+', eachRow[1])
        list1 = ["NET", "SUBNET"]

        if any(check in list1 for check in nets):
          print(eachRow[1])
          print(count)
          if count:
            netRow += "<net labels=\"%s\">%s</net>\n" % (joinLabel.join(netLabel).replace(" ","")[ : -1], netTemp.strip())
            print(count)
            lastNet = eachRow[1]
          netLabel.clear()
          netTemp = eachRow[1]
          continue
        else:
          count = True
          netLabel.append("r%s," % (eachRow[0]))
          printPage += "<row label=\"r%s\">%s</row>\n" % (eachRow[0], eachRow[1].strip())

      netRow += "<net labels=\"%s\">%s</net>\n" % (joinLabel.join(netLabel)[ : -1], lastNet)
  except Exception as e:
    print (e)
  return (netRow + "\n" + printPage)



class OpenEndCode(sublime_plugin.TextCommand):
  def run(self, edit):
    netRows = make_rows(self, edit)
    template = """<exec when="virtualInit">
[qLabel]_coded = File("coded_oe.dat","uniqueid")
</exec>
 
<checkbox label="v[qLabel]_coded_data" atleast="1">
  <title>v[qLabel] Coded Data</title>
  <virtual>
respData = [qLabel]_coded.get(\"[qLabel]||%s" % uuid)
 
if respData:
    for eachCode in range([code_range]):
        if respData['code%s' %(eachCode+1)] not in ['',None]:
            v[qLabel]_coded_data.attr('r%s' % (respData['code%s' %(eachCode+1)])).val = 1
  </virtual>

"""+ netRows +"""
  
</checkbox>"""
    sels = self.view.sel()
    for sel in sels:
      self.view.replace(edit, sel, template)

