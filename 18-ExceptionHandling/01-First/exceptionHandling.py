def test_function(x : int) :
    if type(x) != int :
        raise TypeError('x should be type of int')
    print('start test_function')
    print('x :', x)
    print('end of test_function')

try :
    print('start try block')
    print('calling test function')
    test_function(5.5)
    print('returned from test_function')
    print('end of try block')
except TypeError : # if we don't give any type error here it will become default except block it will handle all type of exception
    print('please give right parameters to test_function()')

print('end of program')