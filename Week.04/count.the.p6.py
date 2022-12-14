import sys

InputFilename = "file.input.txt"


def open_file(filename=InputFilename):  
    try:
        f = open(filename, "r")  # ooening the file in read mode
        return(f)
    except FileNotFoundError:      # error if the file is not found
        # FileNotFoundError is subclass of OSError
        print("File Not Found")
        return(sys.stdin)  # returns the standard input stream so that the rest of the program can keep running
    except OSError:
        print("OS Error") # error with open related to operating system
        return(sys.stdin)


'''
basically if the file is not opened, data will be read in as a command line input. This funciton just reads data from command line / file
'''
    
    
def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:  
            line = input(prompt)
        # Case:  From file
        else:
            line = f.readline()
            print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


theCount = 0
allWords = 0
nonTarget = []
cFlag = True
inFile = open_file()        # Open file will provide either the file or something from the command line
while cFlag:
    line, cFlag = safe_input(inFile)  # same input will now read from that file which will pass through safe input to see if it 
    if not cFlag: 
        break
    for w in line.split():
        allWords = allWords + 1
        if w in ['the', 'The']:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
print("All words:%3s. Target words:%3s" % (allWords, theCount))
print("Non-Target words: ", nonTarget)
