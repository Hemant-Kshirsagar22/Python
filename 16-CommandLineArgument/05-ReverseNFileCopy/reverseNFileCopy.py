import sys

def file_copy(inputFile : str, outputFile : str, isFirst : bool) -> None :
    if type(inputFile) != str or type(outputFile) != str :
        raise TypeError('please provide path of input and output file')
    input_handle = open(inputFile, 'r')
    if isFirst :
        output_handle = open(outputFile, 'w')
    else :
        output_handle = open(outputFile, 'a')
    
    for line in input_handle :
        print(f"--------------------{input_handle.name}---------------------", file=output_handle)
        print(line.rstrip(),file=output_handle)
        print("------------------------------------------------", file=output_handle)

def file_n_copy(inputFiles : list[str], outputFile : str) -> None :
    if type(inputFiles) != list or type(outputFile) != str :
        raise TypeError('please provide path of input files as list[str] and output file as str')
    
    isFirst = True
    for file in inputFiles :
        file_copy(file, outputFile, isFirst)
        isFirst = False

def main(argc : int, argv : list[str]) -> None :
    inputFiles = argv[1 : len(argv)- 2]
    print(inputFiles, type(inputFiles))
    print(argv[len(argv) - 1], type(argv[len(argv) - 1]))
    file_n_copy(inputFiles, argv[len(argv)-1])
    file_n_copy(inputFiles[-1::-1], argv[len(argv) - 2])
    sys.exit(0)
main(len(sys.argv), sys.argv)
