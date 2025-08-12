import sys

source_file_name = input('Enter Source File Name : ')
destination_file_name = input('Enter Destination file name : ')

def copyFile(source : str, destination : str) :
	f_src_handle = open(source, 'r')
	f_dest_handle = open(destination, 'w')

	for line in f_src_handle :
		print(line, end = '', file=f_dest_handle)
	
	f_src_handle.close()
	f_dest_handle.close()

def main() :
	copyFile(source_file_name, destination_file_name)
    sys.exit(0)
    
main()

