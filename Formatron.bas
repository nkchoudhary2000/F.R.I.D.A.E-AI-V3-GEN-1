Sub Formatron()
' ACTION PLAN TO TACKLE FORMATING ERROR IN CODING AND DURING QA
' PLANING TEAM: Prasad Jadhav, Bijo Babu, Nishant Shah, Stanly Leon
' FEEDBACK TEAM: Shraddha Kale, Yuvraj Ghatge, Saiesh Naik, Sonal Chavan
' TRAINER: Darshan Hingu
' DEVELOPER: Jitesh Bagshare, Faizen Shaik, Niraj Choudhary
'
' FormatStylePro Macro: This version is only for professional
'
'



'''''''''''''''''''''''''''''''''''''''''''''''''
''                  FOR ITALIC
'''''''''''''''''''''''''''''''''''''''''''''''''

    Selection.Find.Font.Italic = True
    Selection.Find.Replacement.ClearFormatting
    Selection.Find.Replacement.Font.Color = 49407
    With Selection.Find
        .Text = ""
        .Replacement.Text = "<i>^&</i>"
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting

''''''''''''''''''''''''''''''''''''''''''''''''''
''                  FOR UNDERLINE
''''''''''''''''''''''''''''''''''''''''''''''''''

    Selection.Find.Font.Underline = True
    Selection.Find.Replacement.ClearFormatting
    Selection.Find.Replacement.Font.Color = 10498160
    With Selection.Find
        .Text = ""
        .Replacement.Text = "<u>^&</u>"
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting



''''''''''''''''''''''''''''''''''''''''''''''''''
''                  FOR BOLD
''''''''''''''''''''''''''''''''''''''''''''''''''
    Selection.Find.ClearFormatting
    Selection.Find.Font.Bold = True
    Selection.Find.Replacement.ClearFormatting
    Selection.Find.Replacement.Font.Color = 5287936
    With Selection.Find
        .Text = ""
        .Replacement.Text = "<b>^&</b>"
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting


''''''''''''''''''''''''''''''''''''''''''''''''
''       CLEARING PARAGRAPH
''''''''''''''''''''''''''''''''''''''''''''''''



    Dim arrKeyFormat, arrItemFormat, dict, i
    
    '   DEFINING DICTIONARY

    Set dict = CreateObject("Scripting.Dictionary")
    dict.Add "<b>^p", "^p<b>"
    dict.Add "^p</b>", "</b>^p"
   
    'For Italic garbage tag
    dict.Add "<i>^p", "^p<i>"
    dict.Add "^p</i>", "</i>^p"
   
    'For Underline garbage tag
    dict.Add "<u>^p", "<u>"
    dict.Add "^p</u>", "</u>"

 ' INITIALIZING DICTIONARY
    arrKeyFormat = dict.Keys
    arrItemFormat = dict.Items
    
    For i = 0 To dict.Count - 1
    
    With Selection.Find
            .Text = arrKeyFormat(i)
            .Replacement.Text = arrItemFormat(i)
            .Forward = True
            .Wrap = wdFindContinue
            .Format = False
            .MatchCase = False
            .MatchWildcards = False
            .MatchSoundsLike = False
            .MatchAllWordForms = False
        End With
        Selection.Find.Execute Replace:=wdReplaceAll
    Next

''''''''''''''''''''''''''''''''''''''''''''''''
''       CALLING GARBAGE CLEANER
''''''''''''''''''''''''''''''''''''''''''''''''

    'Call ClearGarbage
    
End Sub