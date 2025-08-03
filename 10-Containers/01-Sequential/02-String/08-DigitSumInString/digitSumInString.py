print('start of program')

string = input('Enter The String to sum digits in string :')

sum = 0
for x in string :
    if ord(x) >= ord('0') and ord(x) <= ord('9') :
        sum = sum + int(x)
        print(x)

print('String : ', string)
print('digit sum :', sum)

print('end of program')
