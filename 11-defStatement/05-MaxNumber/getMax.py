print('start of program')

def getMax(numberOne, numberTwo) :
	if numberOne > numberTwo :
		maxNumber = numberOne
	else :
		maxNumber = numberTwo
	return maxNumber

maxNumber = getMax(30,20);
print("maximum number :", maxNumber)
print('end of program')
