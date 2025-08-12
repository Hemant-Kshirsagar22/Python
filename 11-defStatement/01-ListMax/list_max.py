print('start of program')

L = [10, 20, 130, 40, 50, 60, 70, 80, 9, 10]
L1 = [5, 2, 10, 1, 4]

def listMax(List) :
    max = List[0]
    for x in List :
        if max < x :
            max = x
    print(f'max element in list : {List} is : {max}')

listMax(L)
listMax(L1)

print('end of program')