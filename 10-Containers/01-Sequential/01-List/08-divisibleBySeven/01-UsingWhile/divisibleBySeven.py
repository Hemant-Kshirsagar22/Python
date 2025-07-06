print("Start of program")

L = [ 7, 5, 14, 3, 21 ]
length = len(L)

print("numbers divisible by 7 in list :", L, "is")

i = 0
while i < length :
	if L[i] % 7 == 0 :
		print(L[i])
	i = i + 1

print("End Of Program")

