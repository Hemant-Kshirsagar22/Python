import sys

def countWords(line : str) -> int :
	count = 0
	if(line == '') :
		return(0)
	for x in line :
		if x == ' ' :
			count += 1
	return(count + 1) # + 1 because wordCount = spaceCount + 1
	
def wordCount(fileName : str) -> int :
	f_handle = open(fileName, 'r')
	
	wCount = 0

	for line in f_handle :
		wCount += countWords(line.rstrip())
	return(wCount)			
			

def main() -> None :
	fileName = input('Enter File Name : ')
	print('wordCount :', wordCount(fileName))
	sys.exit(0)

main()

