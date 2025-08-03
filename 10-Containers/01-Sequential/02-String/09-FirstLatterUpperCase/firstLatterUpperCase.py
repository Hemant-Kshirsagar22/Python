print('Start of program')

string = input('Enter The String : ')

i = 0

result = str()

while i < len(string) :
    if((i == 0 or string[i - 1] == ' ') and (ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'))) :
        result = result + chr(ord(string[i]) - 32)
    else :
        result = result + string[i]
    i = i + 1

print("result :", result)

print('End of program')
