import sys

def countWords(line : str) -> int :
	IN = True
	OUT = False

	state = OUT
	wordCount = 0

	for c in line :
		if state == OUT and not c.isspace() :
			state = IN
			wordCount = wordCount + 1
		
		if state == IN and c.isspace() :
			state = OUT

	return wordCount			

def wordCount(fileName : str) -> int :
	f_handle = open(fileName, 'r')
	
	wCount = 0
    
	for line in f_handle :
		wCount += countWords(line)
		
	f_handle.close()
	return(wCount)	

def lineCount(fileName : str) -> int :
	f_handle = open(fileName, 'r')
	
	lineCount = 0
	for line in f_handle :
		lineCount += 1
		
	f_handle.close()
	return lineCount

def countChars(line : str) -> int :
	count = 0
	for c in line :
		if not c.isspace():
			count = count + 1
	return count

def charCount(fileName : str) -> int :
	f_handle = open(fileName, 'r')
	cCount = 0
	for line in f_handle :
		cCount = cCount + countChars(line)
		
	f_handle.close()
	return(cCount)

def nFileCharWordLineCount(inputFiles : list[str], outputFile : str) :
	if type(inputFiles) != list or type(outputFile) != str :
		print("Please provide file names correctly")
		sys.exit(-1)

	o_handle = open(outputFile, 'w')

	for inputFile in inputFiles :
		print(f"------------------ {inputFile} ---------------------", file=o_handle)
		print('lineCount :', lineCount(inputFile), file = o_handle)	
		print('wordCount :', wordCount(inputFile), file = o_handle)
		print('charCount :', charCount(inputFile), file = o_handle)
		print(f"----------------------------------------------------", file=o_handle)
			

def main(argc : int, argv : list[str]) -> None :

	if argc < 2 :
		print("Enter File Names as command line args")
		sys.exit(0)
	
	nFileCharWordLineCount(argv[1:argc - 1], argv[argc - 1])	

	sys.exit(0)

# main()

main(len(sys.argv), sys.argv)