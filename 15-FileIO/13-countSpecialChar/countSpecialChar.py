import sys

def findSpecialCharOccurance(inputFile : str) -> dict :
    if type(inputFile) != str or len(inputFile) == 0:
        raise TypeError('Enter valid file name')
    
    fileHandle = open(inputFile, 'r')
    if fileHandle == None :
        raise FileNotFoundError(f'{inputFile} file not found')
    
    specialCharCountDict = {}

    for line in fileHandle :
        line = line.rstrip()
        for ch in line :
            if ch == ' ':
                continue
            if (ch < 'A' or ch > 'Z') and (ch < 'a' or ch > 'z') and (ch < '0' or ch > '9') :
                if ch not in specialCharCountDict :
                    specialCharCountDict[ch] = 0
                specialCharCountDict[ch] += 1
                
    return specialCharCountDict

def main() -> None :
    fileName = str(input('Enter file name : '))

    print(f'{findSpecialCharOccurance(fileName)}')

    sys.exit(0)

main()