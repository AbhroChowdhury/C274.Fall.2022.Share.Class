'''
safe input ensures that when we get to the end of the line, the while loop breaks. It returns the word in the prompt file on each iteration. When the 
EOFError occurs, the function will start to return false and the loop will eventually stop. 
'''

def safe_input( prompt ):  
    try:
        word = input( prompt )
        return( word, True )
    except EOFError:
        return( "", False )

theCount = 0
allWords = 0
nonTarget = []
cFlag = True
while cFlag:
    word,cFlag = safe_input("")
    if cFlag:
        allWords = allWords + 1
    if word in [ 'the', 'The' ]:
        theCount = theCount + 1
    elif word != '':
        if word not in nonTarget:
            nonTarget.append(word)
print( "All words:%3s. Target words:%3s" % (allWords,theCount) ) #%3s means that the minimum width of the string printed has to be 3
print( "Non-Target words: ", nonTarget )
