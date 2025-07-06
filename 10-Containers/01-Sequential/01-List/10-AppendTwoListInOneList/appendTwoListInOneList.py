print('Start of program')
L1 = [10, 20, 30, 40, 50]
L2 = [60, 70, 80, 90, 100]
L3 = list()

i = 0
length = len(L1) + len(L2)
while i < length :
    if i < len(L1) :
        L3.append(L1[i])
    else :
        L3.append(L2[i - len(L1)])
    i = i + 1

print('L1',L1,'\nL2',L2,'\nappended List',L3)

print('end of program')
