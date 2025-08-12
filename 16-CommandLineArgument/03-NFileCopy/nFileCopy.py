'''
@Author:
    Hemant Ganesh Kshirsagar
    Date : 26/07/2025
'''
import sys

def file_copy(src_file_path : str, dest_file_path : str, isFirstTime : bool) -> None :
    '''
    @input:
        @src_file_path: path of source file.
        @dest_file_path: path of destination file.
    @precondition:
        source file must existing before executing command.
        In destination path all the components must be present.
        Base name may or may not present
    @Behaviour:
        Source file will be open in read mode.
        destination file will be create if not present
        if destination file is present it will be opend in write mode.
        source file will be read line by line, each line will be copied in destination file
    '''
    if type(src_file_path) != str and type(dest_file_path) != str:
        print("source file path and destination file path is not of type of string... exiting")
        sys.exit(-1)
    
    print('src', src_file_path, 'dst', dest_file_path)

    f_src_handle = open(src_file_path, 'r')

    # if we open destination file first time it should be created first
    if isFirstTime :
        f_dest_handle = open(dest_file_path, 'w')
    else :
        f_dest_handle = open(dest_file_path, 'a')

    print(f"---------COYPING:{f_src_handle.name} {f_src_handle.encoding}--------", file=f_dest_handle)
    for line in f_src_handle : 
        print(line.rstrip(), file=f_dest_handle)
    print(f"--------------------------------------", file=f_dest_handle)

    f_src_handle.close()
    f_dest_handle.close()


def file_n_copy(fileNames : list[str]) -> None :
    '''
    @input:
        @fileNames: list of strings of path name where last file name is the destination
   
    @Behaviour:
        it will copy all the files in the last file 
        
    '''
    isFirstTime = True
    for file in fileNames[:-1] :
        file_copy(file, fileNames[len(fileNames) - 1], isFirstTime)
        isFirstTime = False


def main(argc : int, argv : list[str]) -> None :
    '''
    @input:
        @argc: commandline argument count
        @argv: commandline argument vector
    
    Driver function of this module
    '''
    if(argc < 3) :
        print("please give at least two file names as command line arguments !!!")
    file_n_copy(argv[1:])
    sys.exit(0)

main(len(sys.argv), sys.argv)
