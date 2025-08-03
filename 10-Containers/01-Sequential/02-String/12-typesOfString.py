Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
ord('\n')
10
ord('\t')
9
ord('1')
49
chr(49)
'1'
chr(9)
'\t'
'Hello\nWorld'
'Hello\nWorld'
print('Hello\nWorld')
Hello
World
print('Hello\tWorld')
Hello	World
s1 = "Hello    World"
s2 = "Hello\tWorld"
for x in s1 :
    print(x, ord(x))

    
H 72
e 101
l 108
l 108
o 111
  32
  32
  32
  32
W 87
o 111
r 114
l 108
d 100
for x in s2 :
    print(x, ord(x))

    
H 72
e 101
l 108
l 108
o 111
	 9
W 87
o 111
r 114
l 108
d 100


s2 = 'Hello World's !!!
SyntaxError: invalid syntax
s2 = 'Hello World\'s !!!'
s2
"Hello World's !!!"
s = r"Hello\nworld!!!"
s
'Hello\\nworld!!!'
for x in s:
    print(x, ord(x))

    
H 72
e 101
l 108
l 108
o 111
\ 92
n 110
w 119
o 111
r 114
l 108
d 100
! 33
! 33
! 33
n = 10
m = 20
print("Hello,",n,"world
      
SyntaxError: unterminated string literal (detected at line 1)
print("Hello,",n,"world",m)
      
Hello, 10 world 20
s1 = ("Hello, n world !!! m")
      
print(s1)
      
Hello, n world !!! m
s2 = f"Hello, {n} world !!! {m}"
      
s2
      
'Hello, 10 world !!! 20'
for x in s2 :
      print(x, ord(x))

      
H 72
e 101
l 108
l 108
o 111
, 44
  32
1 49
0 48
  32
w 119
o 111
r 114
l 108
d 100
  32
! 33
! 33
! 33
  32
2 50
0 48
s4 = "Addition of (10 + 20) = {n + m}"
      
sr
      
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sr
NameError: name 'sr' is not defined. Did you mean: 's1'?
>>> print(s4)
...       
Addition of (10 + 20) = {n + m}
>>> s4 = f"{s4}"
...       
>>> print(s4)
...       
Addition of (10 + 20) = {n + m}
>>> s4 = f'10 + 20 = {n + m}'
...       
>>> s4
...       
'10 + 20 = 30'
>>> s5 = "Hello {}, world {}".format(n,m)
...       
>>> s5
...       
'Hello 10, world 20'
>>> a = 10
...       
>>> b = 20
...       
>>> c = 30
...       
>>> s6 = "{}, {}, {}".format(a,b,c)
...       
>>> s6
...       
'10, 20, 30'
>>> s7 = "{1}, {2}, {0}".format(a, b, c)
...       
>>> s7
...       
'20, 30, 10'
