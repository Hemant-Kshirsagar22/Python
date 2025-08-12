import sys
print('start of program')

def getMax(numberOne : int, numberTwo : int) -> int :
	if type(numberOne) != int :
		print("numberOne is Not type of int\nExiting The program\n")
		sys.exit(-1)
	
	if type(numberTwo) != int :
		print("numberTwo is Not type of int\nExiting the program\n")
		sys.exit(-1)

	if numberOne > numberTwo :
		maxNumber = numberOne
	else :
		maxNumber = numberTwo

	return maxNumber

max = getMax(10,20)
print('Max :', max)

max = getMax(10, [20, 30, 40])
print('Max :', max)

print('end of program')

