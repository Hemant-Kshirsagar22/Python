Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import sys
a = 10
sys.getrefcount(a)
4294967295
b = 10
sys.getrefcount(b)
4294967295
sys.getrefcount(10)
4294967295
b = a
sys.getrefcount(b)
4294967295
n = 30
n
30
b
10
v
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    v
NameError: name 'v' is not defined
print(512)
512
print(a,n)
10 30
>>> a = 10
>>> b = 20
>>> c = a + b
>>> c
30
>>> #
>>> 10
10
>>> 'x'
'x'
>>> "x"
'x'
>>> True
True
>>> 'Hemant'
'Hemant'
>>> "Hemant"
'Hemant'
>>> 512
512
>>> 
>>> c = a - b
>>> c
-10
>>> c = a * b
>>> c
200
>>> a / b
0.5
>>> c = a / b
>>> c
0.5
