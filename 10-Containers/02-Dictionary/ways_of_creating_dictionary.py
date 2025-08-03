Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
D = { 'A' : 10, 'B' : 20, 'C' : 30 }
for x in D :
    print(x,D[x])

    
A 10
B 20
C 30
for x in D :
    print(x,D[x])

    
A 10
B 20
C 30
for x in D :
    print(x, D[x])

    
A 10
B 20
C 30
for x in D :
    print(x, D[x])

    
A 10
B 20
C 30
for x in D :
    print(x, D[x])

    
A 10
B 20
C 30
D1 = {'A' : , 'B' : 20}
SyntaxError: expression expected after dictionary key and ':'
L = ['A', 'B', 'C']
D1 = dict.fromkeys(L)
D1
{'A': None, 'B': None, 'C': None}
D2 = dict.fromkeys(L)
D2
{'A': None, 'B': None, 'C': None}
D3 = dict.fromkeys(L)
D2
{'A': None, 'B': None, 'C': None}
D3
{'A': None, 'B': None, 'C': None}
D4 = dict.fromkeys(L)
D4
{'A': None, 'B': None, 'C': None}
D5 = dict.fromkeys(L)
D5
{'A': None, 'B': None, 'C': None}
D6 = dict.fromkeys(L, 10)
D6
{'A': 10, 'B': 10, 'C': 10}
D7 = dict.fromkeys(L. 20)
SyntaxError: invalid syntax
D7 = dict.fromkeys(L, 20)
D7
{'A': 20, 'B': 20, 'C': 20}
K = ['A', 'B', 'C', 'D', 'E']
V = [10, 20, 30, 40, 50]
Z = zip(K, V)
Z
<zip object at 0x103c93c40>
print(Z)
<zip object at 0x103c93c40>
for x in Z :
    print(x)

    
('A', 10)
('B', 20)
('C', 30)
('D', 40)
('E', 50)
for x in Z :
    print(x, type(x))

    

for x in Z :
    print(x)
    print(type(x))

    

Z = zip(K, V)
for x in Z :
    print(x, type(x))

    
('A', 10) <class 'tuple'>
('B', 20) <class 'tuple'>
('C', 30) <class 'tuple'>
('D', 40) <class 'tuple'>
('E', 50) <class 'tuple'>
Z = zip(K, V)
D = dict(Z)
D
{'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
for x in D :
    print(x, D[x])

    
A 10
B 20
C 30
D 40
E 50
>>> # zip is an object that is removed as we use it
>>> for x in Z :
...     print(x)
... 
...     
>>> D1 = dict(zip(K, V))
>>> for x in D1 :
...     print(x , ':', D1[x])
... 
...     
A : 10
B : 20
C : 30
D : 40
E : 50
>>> L = [('A', 10), ('B', 20), ('C', 30), ('D', 40)]
>>> D2 = dict(L)
>>> D2
{'A': 10, 'B': 20, 'C': 30, 'D': 40}
>>> type(L)
<class 'list'>
>>> type(L[0])
<class 'tuple'>
>>> for x in D2 :
...     print(x, ':', D[x])
... 
...     
A : 10
B : 20
C : 30
D : 40
