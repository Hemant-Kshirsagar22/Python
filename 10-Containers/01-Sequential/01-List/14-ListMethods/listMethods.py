Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
L = [ 10, 20, 30, 40, 50 ]

id(L)
4341925504
for x in range(len(L))
SyntaxError: expected ':'
for x in range(len(L)) :
    print(id(L[x]), L[x])

    
4354237584 10
4354237904 20
4354238224 30
4354238544 40
4354238864 50
for x in range(Len(L)) :
    print(id(L[x]), L[x])

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for x in range(Len(L)) :
NameError: name 'Len' is not defined. Did you mean: 'len'?
for x in range(len(L)) :
    print(id(L[x]), L[x])

    
4354237584 10
4354237904 20
4354238224 30
4354238544 40
4354238864 50
for x in range(len(L)) :
    print(id(L[x]), L[x])

    
4354237584 10
4354237904 20
4354238224 30
4354238544 40
4354238864 50
L[4 : 2 : -1]
[50, 40]
L[4 : 2]
[]
L[ 2 ::-2
   ]
[30, 10]
L[4-1 : 1 - 1 : -1
  }
SyntaxError: closing parenthesis '}' does not match opening parenthesis '[' on line 1
L[4-1 : 1 - 1 : -1]
[40, 30, 20]
L = []
>>> L.extend("hemant")
>>> L
['h', 'e', 'm', 'a', 'n', 't']
>>> L = []
>>> L = [ 10, 20, 30, 40, 50]
>>> L
[10, 20, 30, 40, 50]
>>> L[3] = [1,2,3]
>>> L
[10, 20, 30, [1, 2, 3], 50]
>>> for x in range(len(L)) :
...     print(type(L[x]), L[x])
... 
...     
<class 'int'> 10
<class 'int'> 20
<class 'int'> 30
<class 'list'> [1, 2, 3]
<class 'int'> 50
>>> L[1 : 4] = [ 1, 2, 3]
>>> L
[10, 1, 2, 3, 50]
>>> L.extend(range(1,10))
>>> L
[10, 1, 2, 3, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[1 : 4] = 1
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    L[1 : 4] = 1
TypeError: must assign iterable to extended slice
>>> L[1 : 4] = [1]
>>> L
[10, 1, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
