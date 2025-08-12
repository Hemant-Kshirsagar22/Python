Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Tuple
# 1. Explicit Syntax
T = (10, 20, 30, 40)
T
(10, 20, 30, 40)
type(T)
<class 'tuple'>
T = (True, False, 10, 3.14, [10, 20, 30], {'A' : 50, 'B' : 60}, (60, 70, 80))
T
(True, False, 10, 3.14, [10, 20, 30], {'A': 50, 'B': 60}, (60, 70, 80))
type(T)
<class 'tuple'>
for x in T :
    print(x, ":", type(x))

    
True : <class 'bool'>
False : <class 'bool'>
10 : <class 'int'>
3.14 : <class 'float'>
[10, 20, 30] : <class 'list'>
{'A': 50, 'B': 60} : <class 'dict'>
(60, 70, 80) : <class 'tuple'>
# class method
s = "Hello"
L = [100, 200, 300, 400]
S = {10.1, 20.2, 30.3}
T1 = tuple(s)
T1
('H', 'e', 'l', 'l', 'o')
T2 = tuple(L)
T2
(100, 200, 300, 400)
T3 = tuple(S)
T3
(10.1, 20.2, 30.3)


# empty tuple
T = ()
type(T)
<class 'tuple'>
len(T)
0


T1 = (True)
type(T1)
<class 'bool'>
# when we give single value to tuple it will consider as we are giving presision to that value ex. (10 - 2) + 10
T1 = (True,)
type(T1)
<class 'tuple'>
T2 = ("Hello")
T2
'Hello'
T2 = ("Hello",)
T2
('Hello',)
type(T2)
<class 'tuple'>


# built in method
T
()
t1 = (True,)

T = (10, 20, 30, 40)
len(T)
4
print(T)
(10, 20, 30, 40)

type(T)
<class 'tuple'>
id(T)
4378860400


# Traversal
# iteration method : for loop
for x in T :
    print(T, type(T))

    
(10, 20, 30, 40) <class 'tuple'>
(10, 20, 30, 40) <class 'tuple'>
(10, 20, 30, 40) <class 'tuple'>
(10, 20, 30, 40) <class 'tuple'>
for x in T :
    print(x, type(x))

    
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
>>> for x in range(len(T)) :
...     print(x)
... 
...     
0
1
2
3
>>> for x in range(len(T)) :
...     print(x, T[x])
... 
...     
0 10
1 20
2 30
3 40
