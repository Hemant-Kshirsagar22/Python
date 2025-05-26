Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
b = 0
not b
True
a = 1
not a
False
b = -10
not b
False
not a
False
not 10
False
not -10
False
not 0
True
and
SyntaxError: invalid syntax
a = True
b = False
b and b
False
b and a
False
a and b
False
a and a
True
1.1 and 0.0
0.0
"Hello" and "world"
'world'
>>> "1" and "0"
'0'
>>> "h" and ""
''
>>> "h" and "b"
'b'
>>> "b" and "h"
'h'
>>> "0" and "1"
'1'
>>> 1 && b
SyntaxError: invalid syntax
>>> a = True
>>> b = False
>>> b or b
False
>>> b or a
True
>>> a or b
True
>>> a or a
True
>>> a = 1
>>> b = 0
>>> b or b
0
>>> b or a
1
>>> a or b
1
>>> a or a
1
