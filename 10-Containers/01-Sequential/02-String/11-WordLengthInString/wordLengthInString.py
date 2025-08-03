print('Start of program')

string = input('Enter The String For word Count : ')

count = 0
word = ''

i = 0
for x in string :
    if((ord(x) >= ord('A') and ord(x) <= ord('Z')) or (ord(x) >= ord('a') and ord(x) <= ord('z')) or ord(x) == ord(' ')) :
        if x == ' ':
            print(word, ':', len(word))
            word = ''
        elif i == len(string) - 1:
            word += x
            print(word, ':', len(word))
            word = ''
        else :
            word += x
    i = i + 1

print('End of program')
