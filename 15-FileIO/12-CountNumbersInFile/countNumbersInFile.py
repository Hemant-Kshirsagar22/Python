import sys

def findNumberOccurance(inputFile : str) -> dict :
    if type(inputFile) != str or len(inputFile) == 0:
        raise TypeError('Enter valid file name')
    
    fileHandle = open(inputFile, 'r')
    if fileHandle == None :
        raise FileNotFoundError(f'{inputFile} file not found')
    
    numberCountDict = {}

    for line in fileHandle :
        words = line.rstrip().split(' ')
        for word in words :
            if str.isnumeric(word) :
                if word not in numberCountDict :
                    numberCountDict[word] = 0
                numberCountDict[word] += 1
                
    return numberCountDict

def main() -> None :
    fileName = str(input('Enter file name : '))

    print(f'{findNumberOccurance(fileName)}')

    sys.exit(0)

main()