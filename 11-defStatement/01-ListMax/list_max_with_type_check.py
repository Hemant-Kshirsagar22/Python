print('Start of Program')
import sys
def listMax(L : list) -> int :
    if type(L) != list :
        print("L is not type of list\nExiting the program\n")
        sys.exit(-1)

    max = L[0]
    for x in L :
        if type(x) != int :
            print(x, "is not type of int\nExiting The Program\n")
            sys.exit(-1)
        if max < x :
            max = x
    
    return max
L = [30, 20, 1, 22, 50, 5]
max = listMax(L)
print('Max element in list', L, 'is :', max)

print('End of Program')