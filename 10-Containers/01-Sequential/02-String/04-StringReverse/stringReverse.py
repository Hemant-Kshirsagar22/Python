print("Start Of Program")

str_one = input("Enter The String For Reverse : ")

str_two = ''

i = len(str_one) - 1

while i >= 0 :
	str_two = str_two + str_one[i]
	i = i - 1

print(str_two)
print("End Of Program")

