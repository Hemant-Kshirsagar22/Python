'''
@Author:
    Hemant Ganesh Kshirsagar
'''
import sys

def file_copy(src_file_path : str, dest_file_path : str) -> None :
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

    f_src_handle = open(src_file_path, 'r')
    f_dest_handle = open(dest_file_path, 'w')

    for line in f_src_handle : 
        print(line, end = '', file=f_dest_handle)
    
    f_src_handle.close()
    f_dest_handle.close()



def main(argc : int, argv : list[str]) -> None :
    '''
    @input:
        @argc: commandline argument count
        @argv: commandline argument vector
    
    Driver function of this module
    '''
    #input validation
    if argc != 3 :
        print("UsageError : correct usage is : ", argv[0], "src_file_path dest_file_path")
        sys.exit(-1)
    
    file_copy(argv[1],argv[2])


    sys.exit(0)

main(len(sys.argv), sys.argv)
