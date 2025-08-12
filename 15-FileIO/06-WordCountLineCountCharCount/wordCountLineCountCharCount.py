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

def main() -> None :
	fileName = input('Enter File Name : ')

	print('lineCount :', lineCount(fileName))	
	print('wordCount :', wordCount(fileName))
	print('charCount :', charCount(fileName))

	sys.exit(0)

main()
