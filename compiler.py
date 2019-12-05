import sublime, sublime_plugin, re

#=============================
#====    DEVELOPER DETAILS  ==
#=============================

# DEV: NIRAJ CHOUDHARY
# GIT_URL: https://github.com/nkchoudhary2000





#================================
#====	  COUNT ALL LABEL      ==
#================================
		
class CountLabelCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			sels = self.view.sel()
			input = ''
			for sel in sels:
				input = self.view.substr(sel)

				niomLabel = re.findall(r'<(radio|html|textarea|checkbox|number|select) label=\"(\w+)\"', input, re.M)
				surveyLabel = re.findall(r'  label=\"(\w+)\"', input, re.M)


				surveyHtmlLabel = re.findall(r'<html label=\"(\w+)\"', input, re.M)

				#44 65 76 65 6c 6f 70 65 64 20 62 79 3a 20 4e 69 72 61 6a 20 43 68 6f 75 64 68 61 72 79 0a 47 49 54 5f 55 52 4c 3a 20 68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 6e 6b 63 68 6f 75 64 68 61 72 79 32 30 30 30 
				
				print("NIOM Label: ", len(niomLabel), " HTML Label: ", len(surveyHtmlLabel), "Net Question: ", len(niomLabel) - len(surveyHtmlLabel), "\n")
				print("Survey Label: ", len(surveyLabel), " HTML Label: ", len(surveyHtmlLabel), "Net Question: ", len(surveyLabel) - len(surveyHtmlLabel), "\n")
		except Exception as e:
			print(e)


#==============================
#=====     GLOBAL MODULE     ==
#==============================

#RETURN GRID IF CONTAIN TWO SIMILAR ROWS
def CheckGrid(input):

	grid = re.findall(r'("r[1Aa]")',input)
	#print (grid)
	#IDENTIFYING RANKING QUESTION
	if re.search(r'(ranksort)', input, re.I):
		try:
			allChoices = ""
			countRow = re.findall(r'(<row)', input)
			for makeChoice in range(len(countRow)):
				allChoices += "<choice label=\"ch" + str(makeChoice+1) + "\">Rank " + str(makeChoice+1) + "</choice>\n"
			input = input.split("<row",1)
			input = input[0] + "\n" + allChoices + "<row" + input[1]
			#44 65 76 65 6c 6f 70 65 64 20 62 79 3a 20 4e 69 72 61 6a 20 43 68 6f 75 64 68 61 72 79 0a 47 49 54 5f 55 52 4c 3a 20 68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 6e 6b 63 68 6f 75 64 68 61 72 79 32 30 30 30 

			return input
		except Exception as e:
			pass
			#print(e)


	if len(grid) == 2:
		input = input.split(grid[1])
		if (grid[0] == grid[1]):
			input[0] = input[0]+grid[1]+input[1]
			input[1] = input[2]
		input[0] = re.sub(r'<row label="r(\w+)"(.*)(</row>)',r'<col label="c\1"\2</col>',input[0])
		input = input[0]+grid[1]+input[1]
		return input
	else:
		try:
			addCols = ""
			chk_DQ_Grid = re.findall(r'((\t\d{1,3}){2,})',input, re.M)
			
			if chk_DQ_Grid:
				
				cols = chk_DQ_Grid[0][0].split("\t")
				lenCols = len(cols) - 1
				for eachCol in range(lenCols):
					addCols += "<col label=\"c" + str(eachCol+1) + "\"> "+ str(eachCol+1) +" </col>\n"
			
			input = addCols + input
		except Exception as e:
			pass

		return input

	

# returns array [input, label,title]
def QuestionMaker(input, count=1, extra = ""):
	label = ""
	titile = ""
	if input == '':
		return False
	input = input.strip()

	


	input = re.sub(r"^(\w?\d+)\.(\d+)",r"\1_\2",input)
	tempText = input
	all_inner_tag = ["<row","<col","<choice","<group","<net","<exec"]
	#Select All RegEx : ((.*)(\n)(.*)){1,}
	#44 65 76 65 6c 6f 70 65 64 20 62 79 3a 20 4e 69 72 61 6a 20 43 68 6f 75 64 68 61 72 79 0a 47 49 54 5f 55 52 4c 3a 20 68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 6e 6b 63 68 6f 75 64 68 61 72 79 32 30 30 30 


	while "\n\n" in input:
		input = input.replace("\n\n", "\n")

	try:
		label = re.split(r"^([\w-]+)(\.|:|\))", input, 1)[1]
		input = re.split(r"^([\w-]+)(\.|:|\)|\s)", input, 1)[-1]

	except Exception as e:
		#print (e)
		#input = re.split(r"\n", tempText, 1)[-1]
		if (tempText == input):
			#print (input)
			return ["errInput", "", tempText]
		count += 1
		if count >= 3:
			print ("Maximum attempt to form Question")
			return [tempText, "errTitle", label]
		QuestionMaker(input, count, extra)

	try:
		input_array = []
		for tags in all_inner_tag:
			if tags in input:
				input_array.append(input.index(tags))
		if len(input_array) == 0:
			title = input 
		else:
			input_index = min(input_array)
			title = input[0:input_index]

	except Exception as e:
		print (e)
	chkGrid = CheckGrid(input)
	if chkGrid:
		input = chkGrid
	if title == "\n":
		pass
	else:
		input = input.replace(title, "")



	#print ("input:", input, "\nLabel:", label, "\nTitle:", title)
	return [input, label, title]


def CharConverter(input):
	# input = input.encode()
	input = re.sub("\t+", " ", input)
	input = re.sub("\n +\n", "\n\n", input)
	funkyChars = [(chr(133),'...'),(chr(145),"'"),(chr(146),"'"),(chr(147),'"'),(chr(148),'"'),(chr(151),'--')]
	for pair in funkyChars:
		input = input.replace(pair[0],pair[1])
	input = re.sub("\n{3,}", "\n\n", input)
	input = input.replace("&", "&amp;")
	input = input.replace("&amp;#", "&#")
	input = input.replace("amp;amp;", "amp;")
	
	return input


#==============================
#=====     NUMBER FILL       ==
#==============================
class ListGenerator(sublime_plugin.TextCommand):
	def run(self, edit):
		first_line = self.view.substr(self.view.sel()[0]).split('\"')
		chk_alpha = False
		if first_line[0].isdigit():
			counter = int(first_line[0]) - 1
		elif first_line[0].isalpha():
			counter = ord(first_line[0])
			chk_alpha = True
		else:
			counter = 0

		for sel in self.view.sel():
			counter += 1
			if chk_alpha:
				strCounter = str(chr(counter - 1))
				if strCounter == "Z":
					counter = 65
				elif strCounter == "z":
					counter = 97
			else:
				strCounter = str(counter)

	
			each_line = self.view.substr(sel).split("\"")
			#print (each_line)			
			if len(each_line) >= 2:
				strCounter += "\"" + each_line[1]

			self.view.replace(edit, sel, strCounter)

#==============================
#=====      UPPER CASE       ==
#==============================

class UpperCaseGenerator(sublime_plugin.TextCommand):
	def run(self, edit):
		first_line = self.view.substr(self.view.sel()[0]).split('\"')
		if first_line[0].isdigit():
			counter = int(first_line[0]) - 1
		for sel in self.view.sel():
			input = self.view.substr(sel)

			if first_line[0].isdigit():
				counter += 1
				input = str(counter)
				self.view.replace(edit,sel,input)
			else:
				input = input.upper()
				self.view.replace(edit,sel,input)


#==============================
#=====      LOWER CASE       ==
#==============================

class LowerCaseGenerator(sublime_plugin.TextCommand):
	def run(self, edit):
		first_line = self.view.substr(self.view.sel()[0]).split('\"')
		if first_line[0].isdigit():
			counter = int(first_line[0]) + 1
		for sel in self.view.sel():
			input = self.view.substr(sel)

			if first_line[0].isdigit():
				counter -= 1
				input = str(counter)
				self.view.replace(edit,sel,input)
			else:
				input = input.lower()
				self.view.replace(edit,sel,input)

#================================
#====	  REMOVE ALL TAG       ==
#================================
		
class RemoveTagCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			sels = self.view.sel()
			input = ''            
			printPage = ''
			for sel in sels:
				input = self.view.substr(sel)
				input = re.sub(r'\n\n', r'\n', input)
				input = input.strip().split('\n')
				for lines in input:
					lines = re.sub(r'[<](\/)?([\w(\s\"\=\.)?"]+)(\/)?[>]', "", lines)
					printPage = lines
					self.view.replace(edit,sel, printPage)
			  
		except Exception as e:
			print ("Tag Splitter Failed!")
			print (e)

#================================
#====	REMOVE UNWANTED TEXT   == 
#================================
def VacuumCleaner(garbage):
	
	garbage = re.sub(r'(\t\d{1,3}){2,}', "", garbage)
	garbage = CharConverter(garbage)

	#garbage = re.sub(r'(</row>)(\n)([\w\n\s\[\]\(\)])+(<row)',r'\1\2<row>\3</skip>\4',garbage)
	garbage = re.sub(r'(</row>)(\n)(?!<ro)(.*\n{1,}){0,}?(</(radio|html|textarea|checkbox|select)>)',r'\1\2\n\4',garbage)
	#garbage = re.sub(r'(<row>)(\n)(</skip>)',r'',garbage)
	garbage = re.sub(r'<row label="r"></row>',r'',garbage)
	garbage = re.sub(r'(<comment>)(.*)([\n\s]{0,})?(</comment>)',r'\1\2\4',garbage)
	#44 65 76 65 6c 6f 70 65 64 20 62 79 3a 20 4e 69 72 61 6a 20 43 68 6f 75 64 68 61 72 79 0a 47 49 54 5f 55 52 4c 3a 20 68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 6e 6b 63 68 6f 75 64 68 61 72 79 32 30 30 30 

	garbage = re.sub(r'(<)',r'&lt;',garbage)
	garbage = re.sub(r'(>)',r'&gt;',garbage)

	garbage = re.sub(r'\[[\w\s\.=:,!@#$%^&\d+\-\–\+_\*/\…\?\'\"\“\”\(\)\’;]+\]', "", garbage)
	garbage = re.sub(r'\[[\s]{0,}\]',r'',garbage)

	garbage = re.sub(r'(&lt;)',r'<',garbage)
	garbage = re.sub(r'(&gt;)',r'>',garbage)

	garbage = re.sub(r'<html .*>([\n\s]{1,})?</html>([\n\s]{1,})?(<suspend/>)', "", garbage)	
	garbage = re.sub(r'(<[BbIiUu]>)([\s\n]{1,})?(</[BbIiUu]>)', "", garbage)
	garbage = re.sub(r'(</title>)(.*[\n\s\w]{1,}){0,}?(<(col|row|choice|comment|/number|/textarea|group|net|exec))',r'\1\n\3',garbage)
	garbage = re.sub(r'(\t\d{1,3})+',r'',garbage)
	garbage = re.sub(r'(\n{2,})',r'\n',garbage)	
	garbage = re.sub(r'(</term>)',r'\1\n\n',garbage)
	garbage = re.sub(r'(<suspend/>)',r'\1\n\n',garbage)
	garbage = re.sub(r'\n(</title>)',r'\1',garbage)
	garbage = re.sub(r'(<row|<col|<choice|<case|<comment)',r'  \1',garbage)
		
	#garbage = re.sub(r'^(\[)?([A-Z/\(\):_]{2,})+(\])?', "", garbage)

	
	return garbage

#4e 69 72 61 6a 
#============================================
#====	 ONLY FOR TESTING PURPOSE          == 
#============================================

class formatronCommand(sublime_plugin.TextCommand): 
	def run(self, edit):
		try:
			sels = self.view.sel()
			input = ''

			for sel in sels:
				printPage = ''
				setupDone = ''
				input = self.view.substr(sel)
				setupDone = FormatronGarbage(input)
			self.view.replace(edit,sel, setupDone)
		except Exception as e:
			print (e)

#4e 69 72 61 6a 
#===================================================
#====	  CLEAR FORMATTING GARBAGE BY FORMATRON   == 
#===================================================


def FormatronGarbage(input):
	try:
		#print(input)
		try:
			tempText = re.findall(r'(<(/)?([BUI])>)', input)
			for eachText in tempText:
				input = input.replace(eachText[0], eachText[0].lower())
		except Exception as e:
			print(e)
			pass


		#REMOVE ALL CAPITAL SINGLE WORD TO PN SQUARE BRACKET
		input = re.sub(r'<b>([A-Z0-9_\s\.=≠:,!@#$%^&<>\-\–\+\*/\…\?\'\"\“\”\(\)\’;]+)</b>',r'[\1]',input)
		#REMOVE FORMATING TAG FROM SIDE OF SQUARE BRACKET (PN NOTE)
		input = re.sub(r'(<[/]?[bui]>[\s+]?)?(\[|\])([\s+]?<[/]?[bui]>)?', r'\2', input)
		#REMOVE BLANK FORMATING TAG ----NEED BETTER WAY OF DOING THIS
		input = re.sub(r'(</b><b>|</i><i>|</u><u>|<b></b>|<u></u>|<i></i>)', r'', input)

	except Exception as e:
		print (e)

	return input



#4e 69 72 61 6a 
#================================
#====	  MADE ALL ROWS        == 
#================================
def RowsMaker(input):
	input = input.split("\n")
	tempText = ""
	for eachLine in input:
		OE = EXE = SHF = ""
		eachLine = eachLine.strip()

		#INDENTIFY QUESTION LABEL
		eachLine = re.sub(r'^(\[|\()?([Q][_]?)?(([\d]+[a-zA-Z_]+)+|([a-zA-Z_]+)|([a-zA-Z_]+[\d]+)+|([a-zA-Z_]+)([\d]+[a-zA-Z_]+)+)(\.|\)|\])([\s]?\])', r'\10\n\3. ', eachLine)
		
		eachLine = re.sub(r'<b>(\d+)</b>',r'\1',eachLine)
		eachLine = re.sub(r'((MR|OE|SR|RANDOMIZE|GRID|DECK|HEADER|LIST|ROW|COLUMN)(S)?)',r'\1/', eachLine)
		
		eachLine = re.sub(r'^([\da-zA-Z])$',r'<row label="r\1">\1</row>', eachLine)
		eachLine = re.sub(r'^(\[|\(|\s)?((c|r|ch)?([\d]+))(\.|\s|:|\)|\])(.*)',r'<row label="r\4">\6</row>', eachLine)
		if "<row" not in eachLine:
			eachLine = re.sub(r'^(\[|\(|\s)?([a-zA-Z])(\.|\s|:|\)|\])(\s{1,})?(.*)',r'<row label="r\2">\5</row>', eachLine)
		if "<row" in eachLine:
			if re.search(r'(\Wopen[-\s]end\W|\Wspecify\W|\Wtext[-\s]?box\W|\Woe\W|\Wexplain\W)', eachLine, re.I):
				OE = "open=\"1\" openSize=\"25\"" + " "
				SHF = "randomize=\"0\"" + " "
			if re.search(r'(\Wexclusive\W|\Wsingle[-\s]?select\W)|(None of the above)|(None of these)', eachLine, re.I):
				EXE = "exclusive=\"1\"" + " "
				SHF = "randomize=\"0\"" + " "
			if re.search(r'(\Whold\W|\Wanchor\W|\Wrandomize\W|\Wshuffle\W)', eachLine, re.I) and (SHF == ""):
				SHF = "randomize=\"0\"" + " "
			eachLine = re.sub(r'(\">)',"\" " + OE + EXE + SHF + ">", eachLine)
		tempText += eachLine + "\n"

	return tempText
#4e 69 72 61 6a 
#================================
#====	  APPEND SPLIT TAG     == 
#================================

def AppendSplit(input):
	input = FormatronGarbage(input)
	input = RowsMaker(input).split("\n")
	tempText = ""

	try:

		for eachLine in input:
			eachLine = eachLine.strip()
			eachLine = re.sub(r'(<[BbIiUu]>)([\s\n]{1,})?(\[)(.*)(\]|\))([\s\n]{1,})?(</[BbIiUu]>)', r'\3\4\5', eachLine)
			found = re.search("^(\[|\()?([Q][_]?)?(([\d]+[a-zA-Z_]+)+|([a-zA-Z_]+)|([a-zA-Z_]+[\d]+)+|([a-zA-Z_]+)([\d]+[a-zA-Z_]+)+)(\.|\)|\])", eachLine)
			if found:
				eachLine = re.sub(r'^(\[|\()?([Q][_]?)?(([\d]+[a-zA-Z_]+)+|([a-zA-Z_]+)|([a-zA-Z_]+[\d]+)+|([a-zA-Z_]+)([\d]+[a-zA-Z_]+)+)(\.|\)|\])', r'\3.', eachLine)
				eachLine = "<split>\n" + eachLine
			tempText += eachLine + "\n"
	except Exception as e:
		print(e)
	return tempText

#================================
#====	  MADE COMMENT         == 
#================================

def RespondentInstruction(comment_body):
	if "<comment>" in comment_body:
		return comment_body

	comment_text = """
check all that apply for each column
please be as detailed as possible
Please be as specific as possible
please be specific
Please select one answer
Please select one answer from the list below
Please select one answer for each statement
Please select all that apply from the list below
Please select up to three answers
Please select the one answer
Please write your answer in the box below
please choose all that apply
please explain in detail
Please be as descriptive as possible
please select all that apply
Please select all that apply to you
please select one
Type a whole number
please select one for each statement
please select one response per row
please use each of the text boxes below
please use the text box below
please use the text box below to answer
select all that apply
select at least one for each column
Please Select One Answer for Each Row. 
select one
Select one response per row
select one for each row
select only one
select only one for each row
enter a whole number below
enter number below
"""


	commentList = comment_text.split('\n')[1:-1]
	commentList.sort(key = len, reverse = True)

	for eachComment in commentList:
		#print (len(eachComment))
		eachComment = eachComment.strip()
		foundComment = re.search("(<[biu]>)?(\W)?("+eachComment+")([\s+\)<>/\.]+)?([biu]>)?",comment_body, re.I)

		try:
			subString = str(foundComment.group(0))
			commentString = "<comment>"+subString+"</comment>"
			comment = comment_body.replace(subString, commentString)
			return comment		
		except Exception as e:
			pass
			#print(e)
			#Do nothing: This just to keep error apart
			#print (eachComment,":",foundComment)
	return comment_body

#============================================
#====	  MADE ALL QUESTION  FOR TESTING   == 
#============================================

class madeAllCommand(sublime_plugin.TextCommand): 
	def run(self, edit):
		try:
			sels = self.view.sel()
			input = ''

			for sel in sels:
				printPage = ''
				setupDone = ''
				input = self.view.substr(sel)
				setupDone = AppendSplit(input)
			self.view.replace(edit,sel, setupDone)
		except Exception as e:
			print (e)



#4e 69 72 61 6a 
#================================
#====	RETURN QUESTION TYPE   ==
#================================

def ReturnQType(input, questionLabel):
	input = input.lower()
	try:
		if re.search(r'(ranksort)', input):
			return "ranksort"
		elif re.search(r'(\W?sr\W?|\W?select[-\s]?one\W?|\W?single[-\s]?select\W?)', input) and (("<row" or "<col") in input):
			return "radio"
		elif re.search(r'(\W?mr\W?|\W?exclusive\W?|\W?apply\W?|\W?multi[-\s]?select\W?)', input):
			return "checkbox"
		elif (("<row" or "<col") not in input) and (questionLabel != ""):
			return "textbox"
		elif (("<row" or "<col") not in input) and (questionLabel == ""):
			return "html"
		else:
			return "radio"
	except Exception as e:
		print(e)


#================================
#====	RETURN PIPE IN QLABEL  ==
#================================

def ReturnPipeInLabel(qTitle,GLOBAL_LABEL):
	if ("pipe" in qTitle.lower()):
		for eachLabel in GLOBAL_LABEL:
			if (eachLabel in qTitle) and (eachLabel != ""):
				copyAttribute = " onLoad=\"copy('"+ eachLabel +"', rows=True, exclude='')\""
				return copyAttribute
	return ""


#================================
#====	  MADE ALL QUESTION    ==
#================================


class madeAllQuestionCommand(sublime_plugin.TextCommand): 
	def run(self, edit):
		try:
			sels = self.view.sel()
			input = ''
			GLOBAL_LABEL = []

			for sel in sels:
				printPage = ''
				setupDone = ''
				input = self.view.substr(sel)
				input = re.sub(r'<b>([0-9A-Z\W]+)</b>', r'[\1]', input)
				input = AppendSplit(input)
				###################################
				#TESTING FOR ALL AT ONCE RADIO SETUP
				tester = input.split("<split>")
				htmlLabel = ""
				for allQuestion in tester:
					singleQuestion = QuestionMaker(allQuestion)
					if not singleQuestion:
						continue
					content = singleQuestion[0]
					questionLabel = singleQuestion[1]
					questionTitle = singleQuestion[2]



					shf = ""
					ratingAttribute = ""
					questionTitle = RespondentInstruction(questionTitle)

					try:
						comment = re.findall(r'<comment>.*[\n\s]{0,}?.*</comment>',questionTitle)[0]
					except Exception as e:
						comment = ""
					questionTitle = re.sub("<comment>.*[\n\s]{0,}?.*</comment>", "", questionTitle)

					#ADDING RATING ATTRIBUTE
					if re.search(r'((Not at all)|((dis)agree)|(Strongly)|(Very)|(Extremely))\W?(((dis)?like(ly)?)|(completely)|(satisfied)|(easy)|(well)|((dis)?agree))', content, re.I):
						ratingAttribute = " type=\"rating\" values=\"order\""

					if ("randomize" or "shuffle") in (questionTitle.lower()):
						shf = "shuffle=\"rows\""

					#FETCHING PIPE IN QUESTION
					copyAttribute = ReturnPipeInLabel(questionTitle,GLOBAL_LABEL)

					QType = (content + questionTitle + comment)
					QType = ReturnQType(QType,questionLabel)


					

					if QType == "ranksort":
						try:
							countRow = len(re.findall(r'(<choice)', content))
							extraAttrib =  "minRanks=\""+str(countRow)+"\" optional=\"1\" ranksort:cardCSS=\"height:100px\" shuffle=\"rows\" unique=\"none,cols\" uses=\"ranksort.4\""
							setupDone += "<select label=\"%s\" %s%s %s%s>\n  <title>%s</title>\n%s\n%s\n</select>\n<suspend/>\n\n" % (questionLabel.strip(), shf, ratingAttribute,extraAttrib,copyAttribute, questionTitle.strip(), comment, content)
						except Exception as e:
							print(e)
					elif QType == "radio":
						setupDone += "<radio label=\"%s\" %s%s%s>\n  <title>%s</title>\n%s\n%s\n</radio>\n<suspend/>\n\n" % (questionLabel.strip(), shf, ratingAttribute,copyAttribute, questionTitle.strip(), comment, content)
					
					elif QType == "checkbox":
						setupDone += "<checkbox label=\"%s\" %s%s atleast=\"1\">\n  <title>%s</title>\n%s\n%s\n</checkbox>\n<suspend/>\n\n" % (questionLabel.strip(), shf,copyAttribute, questionTitle.strip(), comment, content)
					
					elif (QType == "textbox") and ("\Wpipe in\W" not in questionTitle.lower()):
						if re.search(r'(\Wnumeric\W)|(\Wnumber\W)|(\Whow many\W)|(\Wdollar\W)|(\Wage\W)', questionTitle, re.I):
							setupDone += "<number label=\"%s\" size=\"3\" verify=\"range(1,100)\" optional=\"0\">\n  <title>%s</title>\n%s\n%s\n</number>\n<suspend/>\n\n" % (questionLabel.strip(), questionTitle.strip(), comment, content)
						else:
							setupDone += "<textarea label=\"%s\" optional=\"0\">\n  <title>%s</title>\n%s\n%s\n</textarea>\n<suspend/>\n\n" % (questionLabel.strip(), questionTitle.strip(), comment, content)
					
					elif QType == "html":
						questionTitle = re.sub(r'\n', r'<br/><br/>\n', questionTitle)
						setupDone += "<html label=\"%s_Intro\" where=\"survey\">\n%s\n</html>\n<suspend/>\n\n" % (htmlLabel, questionTitle.strip())
						continue
					
					else:
						continue


					#ADDING CURRENT QUESTION LABEL INTO LABEL COLLECT TO USE IN PIPE IN CASE
					GLOBAL_LABEL.append(questionLabel)
					#print(GLOBAL_LABEL)


					htmlLabel = questionLabel.strip()

					if re.search(r'(skip to end|term|terminate|screen out)', content + questionTitle, re.I):
						termRow = content.split("\n")
						termRow += questionTitle.split("\n")
						termLabel = ""
						tempRow2 = ""
						for eachTerm in termRow:
							if re.search(r'(skip to end|term|terminate|screen out)', eachTerm, re.I):
								tempRow = ''.join(map(str, re.findall(r'[r]\d+', eachTerm))) + " "
								termLabel += questionLabel.strip() + "." + tempRow + "or "
								tempRow2 += tempRow
								#print("term row: ", tempRow, )
						termLabel = re.sub(' or $', '', termLabel)
						setupDone += "\n\n<term label=\"%s_Term\" cond=\"%s\">Term for %s if coded '%s'</term>\n\n" % (questionLabel.strip(), termLabel, questionLabel.strip(), tempRow2.strip())


				#VacuumCleaner() WILL CLEAN ALL UNWANTED TEXT
				setupDone = VacuumCleaner(setupDone)

				#SEQUENCING INTRO LABEL AS PER BELOWED QUESTION LABEL
				htmlLabel = re.findall(r'^<(radio|html|textarea|checkbox|number|select) label=\"(\w+)\"', setupDone, re.M)
				onlyHtmlLabel = re.findall(r'^<html label=\"(\w+)\"', setupDone, re.M)
				count = 0
				for eachHtmlLabel in htmlLabel:
					try:
						if re.search(r'html', eachHtmlLabel[0]):
							if count == 0:
								setupDone = re.sub(r'<html label="'+htmlLabel[count][1],r'<html label="'+htmlLabel[count+1][1]+'_Intro',setupDone)
							else:
								setupDone = re.sub(r'<html label="'+htmlLabel[count-1][1]+'_Intro',r'<html label="'+htmlLabel[count+1][1]+'_Intro',setupDone)
					except Exception as e:
						print ("eachHtmlLabel Block: ", e)
					if count == len(htmlLabel) - 2:
						count = 0
						break
					count +=1
				TotalLabel = re.findall(r'^<(radio|html|textarea|checkbox|number|select) label=\"(\w+)\"', setupDone, re.M)
				for eachLabel in TotalLabel:
					pass
					#print (eachLabel[1], ": ",eachLabel[0] )#44 65 76 65 6c 6f 70 65 64 20 62 79 3a 20 4e 69 72 61 6a 20 43 68 6f 75 64 68 61 72 79 0a 47 49 54 5f 55 52 4c 3a 20 68 74 74 70 73 3a 2f 2f 67 69 74 68 75 62 2e 63 6f 6d 2f 6e 6b 63 68 6f 75 64 68 61 72 79 32 30 30 30 
					
				print ("Question Made:", len(htmlLabel), " Real Question: ", (len(htmlLabel) - len(onlyHtmlLabel)))	
				#END				



				self.view.replace(edit,sel, setupDone)
		except Exception as e:
			print ("CUSTOM_PLUGIN: Question clip failed:")
			#print (e)





		