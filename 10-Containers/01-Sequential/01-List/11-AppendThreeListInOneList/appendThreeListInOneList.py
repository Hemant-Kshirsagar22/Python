print('start of program')

L1 = list(range(1, 6))
L2 = list(range(6, 11))
L3 = list(range(11, 16))
L4 = list()
i = 0
length = len(L1) + len(L2) + len(L3)
while i < length :
    if i < len(L1) :
        L4.append(L1[i])
    elif i >= len(L1) and i < len(L1) + len(L2) :
        L4.append(L2[i - len(L1)])
    elif i >= len(L1) + len(L2) :
        L4.append(L3[i - (len(L1) + len(L2))])

    i = i + 1

print('L1', L1, '\nL2', L2, '\nL3', L3, '\nAppended L4', L4)
        
print('end of program')
