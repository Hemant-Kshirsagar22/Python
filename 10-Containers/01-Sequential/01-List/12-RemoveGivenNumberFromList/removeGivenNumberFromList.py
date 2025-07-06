print('start of program')

L1 = list(range(1,11))
print('L1',L1)

number_str = input('Enter The number you want to remove from list : ')
number = int(number_str)
i = 0
removedNumber = False

while i < len(L1) :
    if L1[i] == number :
        L1.pop(i)
        removedNumber = True

    i = i + 1

if removedNumber == False:
    print(number, "not present in list")
else :
    print(number, 'is removed from list\nL1', L1)

print('end of program')
