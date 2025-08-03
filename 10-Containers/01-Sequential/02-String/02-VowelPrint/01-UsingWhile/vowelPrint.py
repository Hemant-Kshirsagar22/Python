string = input("Enter The String to print vowel : ")

i = 0
print("vowel in string : '", string, "'")
while i < len(string) :
	if string[i] == 'A' or string[i] == 'a' or string[i] == 'E' or string[i] == 'e' or string[i] == 'I' or string[i] == 'i' or string[i] == 'O' or string[i] == 'o' or string[i] == 'U' or string[i] == 'u' :
		print(string[i])
	i = i + 1
		
