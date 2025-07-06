print("start of program")

# list creation
L = [ 1, 2, 3, 4, 5 ]

# finding length of list using len() function, which take list of variable as arguments
length = len(L)

sum = 0

# while loop for calculating the sum
i = 0
while i < length :
	sum = sum + L[i]
	i = i + 1

arithmaticMean = sum / length

print("Arithmatic Mean Of :", L, "Is :", arithmaticMean)

print("End Of Program")
 
