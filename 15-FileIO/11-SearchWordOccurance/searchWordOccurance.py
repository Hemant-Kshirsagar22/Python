import sys

def findWordOccurance(inputFile : str, word : str) -> int :
    if type(inputFile) != str or len(inputFile) == 0:
        raise TypeError('Enter valid file name')
    if type(word) != str or len(word) == 0 :
        raise TypeError('word should be valid string')
    
    fileHandle = open(inputFile, 'r')
    if fileHandle == None :
        raise FileNotFoundError(f'{inputFile} file not found')
    
    wordCount = 0

    for line in fileHandle :
        words = line.rstrip().split(' ')
        if word in words :
            wordCount += words.count(word)
    
    return wordCount

def main() -> None :
    fileName = str(input('Enter file name : '))
    word = str(input('Enter Word : '))

    print(f'"{word}" occurs "{findWordOccurance(fileName, word)}" times in file "{fileName}"')

    sys.exit(0)

main()