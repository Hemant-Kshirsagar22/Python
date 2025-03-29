Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> c = a + b
>>> c
30
>>> a = "abc"
>>> a = True
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': True, 'b': 20, 'c': 30}
>>> e = False
>>> z = 3.14
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': True, 'b': 20, 'c': 30, 'e': False, 'z': 3.14}
>>> a
True
>>> b
20
>>> c = a + b
>>> print(c)
21
