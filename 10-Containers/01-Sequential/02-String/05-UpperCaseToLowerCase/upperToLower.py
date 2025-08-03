print('start of program')

string = input('Enter the string for converting upper case to lower : ')

stringTwo = ''
i = 0
while i < len(string) :
    if ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z') :
        stringTwo = stringTwo + chr(ord(string[i]) + 32)
    else :
        stringTwo = stringTwo + string[i]
    i = i + 1

print('String after converting string upper to lower :', stringTwo)
print('end of program')
