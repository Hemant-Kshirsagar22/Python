import sys

def addition(numberOne, numberTwo) :
	result = numberOne + numberTwo
	return result

def main() :
	print('Addition')
	numberOne_str = input('Enter First Number  : ')
	numberTwo_str = input('Enter Second Number : ')
	numberOne = int(numberOne_str)
	numberTwo = int(numberTwo_str)

	result = addition(numberOne, numberTwo)
	
	print(f"{numberOne} + {numberTwo} = {result}")
	sys.exit(0)

main()
