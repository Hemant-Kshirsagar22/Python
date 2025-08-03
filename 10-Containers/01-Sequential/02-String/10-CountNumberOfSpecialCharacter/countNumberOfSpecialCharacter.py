print('start of program')

string = input('Enter The String to count Special character :')

count = 0

for x in string :
    if ((ord(x) < ord('A') or ord(x) > ord('Z')) and (ord(x) < ord('a') or ord(x) > ord('z')) and (ord(x) < ord('0') or ord(x) < ord('0'))) :
        count = count + 1
        
print("String :", string)
print("number of special characters :", count)
print('End of program')
