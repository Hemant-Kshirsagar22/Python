import sys

def main(argc : int, argv : list[str]) -> None :
	'''
	@input:
		@argc: commandLine argument count.
		@argv: commandLine argument vector.
	
	Driver function of the module.
	'''
	
	print("argc :", argc)
	print("argv :", argv)

	sys.exit(0)

main(len(sys.argv), sys.argv) 
