Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {'A' : 10, 'B' : 20, 'C' : 30, 'D' : 40, 'E' : 50}
>>> d
{'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
>>> d['A']
10
>>> d['B']
20
>>> d['b']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d['b']
KeyError: 'b'
