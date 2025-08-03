print("start of program")

string = input('Enter the String : ')

i = 0
j = len(string) - 1

isPalendrom = False

while i != j and i >= 0 and j >= 0 :
    if string[i] != string[j] :
        isPalendrom = True
        break
    i = i + 1
    j = j - 1

if not isPalendrom :
    print('String is palendrom')
else :
    print('String is not palendrom')

print('End of program')
