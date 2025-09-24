def square(x : float) -> float :
    if type(x) != float and type(x) != int :
        raise TypeError('Excpected numerical value')
    
    if x < 0.0 :
        raise ValueError('x must be greater than zero')
    
    print(X) # for code 2
    return x * x

try :
    print('calling square with wrong type')
    square('Hello')
    print('control flow won\'t come here')
except ValueError :
    print('CORRECT TYPE : WRONG VALUE')
except TypeError :
    print('WRONG TYPE OF ARGUMENT')

print('\n\ncontinuing with code')

try :
    print('calling square with correct type, wrong value')
    square(-7.9)
    print('control flow won\'t come here')
except ValueError :
    print('CORRECT TYPE : WRONG VALUE')
except TypeError :
    print('WRONG TYPE OF ARGUMENT')

print('\n\ncontinuing with code')

try :
    print('calling square with correct type as well as correct value')
    square(7.7)
    print('control flow won\'t come here')
except ValueError :
    print('CORRECT TYPE : WRONG VALUE')
except TypeError :
    print('WRONG TYPE OF ARGUMENT')    
except : # default exception handler
    print('SOMTHING WENT WRONG')

print('End of program')