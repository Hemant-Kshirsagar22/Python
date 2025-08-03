print('start of program')

string = input('Enter The String containing digits :')
count = 0
for x in string :
    if ord(x) >= ord('0') and ord(x) <= ord('9') :
        print(x)
        count = count + 1

print("String : '", string, "'")
print("count of digits : ", count)
print('end of program')
