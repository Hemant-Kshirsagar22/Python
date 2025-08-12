import sys

def lineCount(fileName : str) -> int :
	f_handle = open(fileName, 'r')
	
	lineCount = 0
	for line in f_handle :
		lineCount += 1
	f_handle.close()
	return lineCount

def main() :
	fileName = input('Enter File Name : ')
	print('lineCount :', lineCount(fileName))
	sys.exit(0)

main()
