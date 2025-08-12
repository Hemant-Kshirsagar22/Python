'''
@Author      : Hemant Ganesh Kshirsagar
@Date        : 06/07/2025
@Description : This is a program of genaric addition function where we can pass any type of data and we get addition of that numbers
'''
import sys

def addition(inputOne, inputTwo):
    '''
    @input:
        @inputOne : first input type of int/float/list
        @inputTwo : second input type of int/float/list
        Both type should be same.
        inputOne == inputTwo
    @return:
        @result : returns addition according to given type
    '''

    if type(inputOne) != int and type(inputOne) != list and type(inputOne) != float :
        print("inputOne should be int/float/ list of int or float")
        sys.exit(-1)

    if type(inputTwo) != int and type(inputTwo) != list and type(inputTwo) != float :
        print("inputTwo should be int/float/ list of int or float")
        sys.exit(-1)

    if type(inputOne) != type(inputTwo) :
        print("type of inputOne and inputTwo must be same")
        sys.exit(-1)
    
    result = None
    
    if type(inputOne) == int :
        result = int()
        result = inputOne + inputTwo
    elif type(inputOne) == float :
        result = float()
        result = inputOne + inputTwo
    elif type(inputOne) == list :
        inputOneSize = len(inputOne)
        inputTwoSize = len(inputTwo)
        result = []
        if(inputOneSize > inputTwoSize) :
            i = 0
            while i < inputOneSize :
                if i < inputTwoSize :
                    if type(inputTwo[i]) != int and type(inputTwo[i]) != float :
                        print("list element should be type of int/float")
                        sys.exit(-1)
                    
                if type(inputOne[i]) != int and type(inputOne[i]) != float :
                    print("list element should be type of int/float")
                    sys.exit(-1)

                if i < inputTwoSize :
                    result.append(inputOne[i] + inputTwo[i])
                else :
                    result.append(inputOne[i])
                i = i + 1
        else :
            i = 0
            while i < inputTwoSize :
                if i < inputOneSize :
                    if type(inputOne[i]) != int and type(inputOne[i]) != float :
                        print("list element should be type of int/float")
                        sys.exit(-1)

                if type(inputTwo[i]) != int and type(inputTwo[i]) != float :
                    print("list element should be type of int/float")
                    sys.exit(-1)

                if i < inputOneSize :
                    result.append(inputOne[i] + inputTwo[i])
                else :
                    result.append(inputTwo[i])
                i = i + 1
    else :
        print("input type must be int, float or list")
    
    return result


    
def main() :
    '''
    Driver Function module
    '''

    L1 = [10, 20, 30]
    L2 = [10, 38, 90, 100]

    result = addition(10, 20)
    print(result)

    result = addition(10.01, 30.50)
    print(result)

    result = addition(L1, L2)
    print(result)
    
    result = addition(L2, L1)
    print(result)

    sys.exit(0)

main()