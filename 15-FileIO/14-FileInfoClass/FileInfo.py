'''
this class contains
    fileName
    wordCount
    LineCount
    numberCount

'''
class FileInfo :
    def __init__(self, fileName : str) :
        if type(fileName) != str :
            raise TypeError('please give file name or path in form of string')
        
        self.fileName = fileName
        self.wordCount = 0
        self.lineCount = 0
        self.numberCount = {}

    def setWordCount(self, wCount : int) :
        self.wordCount = wCount

    def getWordCount(self) -> int :
        return self.wordCount
    
    def setLineCount(self, lCount : int) :
        self.lineCount = lCount

    def getLineCount(self) -> int :
        return self.lineCount
    
    def setNumberCount(self, dCount : int) :
        self.numberCount = dCount
    
    def getNumberCount(self) -> int :
        return self.numberCount
    
    def countWords(self, line : str) -> int :
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

    def wordsCount(self) -> None :
        f_handle = open(self.fileName, 'r')
        if f_handle == None :
            raise FileNotFoundError('File Not Found')
        wCount = 0

        for line in f_handle :
            wCount += self.countWords(line)
        f_handle.close()

        self.setWordCount(wCount)
    
    def numberOfLinesCount(self) -> None :
        f_handle = open(self.fileName, 'r')
        if f_handle == None :
            raise FileNotFoundError('File Not Found')
        lineCount = 0
        for line in f_handle :
            lineCount += 1
        self.setLineCount(lineCount)
    
    def numberOfNumbersCount(self) -> None :
        f_handle = open(self.fileName, 'r')
        if f_handle == None :
            raise FileNotFoundError('File Not Found')
        
        numberCountDict = {}

        for line in f_handle :
            words = line.rstrip().split(' ')
            for word in words :
                if str.isnumeric(word) :
                    if word not in numberCountDict :
                        numberCountDict[word] = 0
                    numberCountDict[word] += 1
        self.setNumberCount(numberCountDict)

fileInfo = FileInfo('input.txt')

fileInfo.wordsCount()
fileInfo.numberOfLinesCount()
fileInfo.numberOfNumbersCount()

print('word count : ', fileInfo.getWordCount())
print('line count : ', fileInfo.getLineCount())
print('numbers count : ', fileInfo.getNumberCount())

