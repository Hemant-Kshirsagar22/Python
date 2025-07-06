Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
L = [ 10, 20, 30 ]
type(L)
<class 'list'>
L
[10, 20, 30]
print(L)
[10, 20, 30]
L
[10, 20, 30]
L[0]
10
L[1]
20
>>> L[2]
30
>>> L[3]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    L[3]
IndexError: list index out of range
>>> l[2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l[2]
NameError: name 'l' is not defined. Did you mean: 'L'?
>>> str_one = "ABC"
>>> str_one
'ABC'
>>> str_one[0]
'A'
>>> type(str_one)
<class 'str'>
>>> L = [ 10, 20, 30, 40, 50 ]
>>> type(L)
<class 'list'>
>>> L[0]
10
>>> L[0] = 100
>>> print(L)
[100, 20, 30, 40, 50]
>>> L[1] = True
>>> L
[100, True, 30, 40, 50]
>>> type(L[1])
<class 'bool'>
>>> type(L[0])
<class 'int'>
