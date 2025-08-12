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

def main() -> None :
	fileName = input('Enter File Name : ')
	
	print('wordCount :', wordCount(fileName))

	sys.exit(0)

main()


