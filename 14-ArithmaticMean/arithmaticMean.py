import sys

def arithmatic_mean(L : list) -> float :
    if type(L) != list:
        printf("L should be type of list")
        sys.exit(-1)

    if len(L) == 0 :
        print("L should Not be empty list")
        sys.exit(-1)

    a_sum = 0.0
    for x in L :
        if type(x) != int and type(x) != float :
            print("List elements should be type of int/float")
        a_sum = a_sum + x
    
    a_mean = a_sum / len(L)

    return a_mean

def main() :
    '''
    '''

    List = [10.0, 20.1, 30.1, 45.5, 64.4]
    a_mean = arithmatic_mean(List)
    print(f'arithmatic Mean : {a_mean}')

main()