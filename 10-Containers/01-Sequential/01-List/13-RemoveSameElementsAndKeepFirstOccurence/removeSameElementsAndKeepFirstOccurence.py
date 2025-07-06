print('start of program')

L1 = [1, 2, 3, 1, 2]

elementCountList = []

print('Before Removeing Duplicate Elements And storing single occurance\n',L1)
i = 0
while i < len(L1) :
    j = i + 1
    while j < len(L1) :
        if L1[i] == L1[j] :
            L1.pop(j)
        j = j + 1
    i = i + 1

print("After Removeing Duplicate Elements And storing single occurance\n" , L1)
print('end of program')
