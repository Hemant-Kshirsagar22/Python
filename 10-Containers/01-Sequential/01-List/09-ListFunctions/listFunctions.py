Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> L1 = [10, 20, 30, 40, 50]
>>> L2 = list(range(60,66))
>>> L1
[10, 20, 30, 40, 50]
>>> L2
[60, 61, 62, 63, 64, 65]
>>> L3 = L1 + L2
>>> L3
[10, 20, 30, 40, 50, 60, 61, 62, 63, 64, 65]
>>> L4 = L2 + L1
>>> L4
[60, 61, 62, 63, 64, 65, 10, 20, 30, 40, 50]
>>> L1.append(60)
>>> L1
[10, 20, 30, 40, 50, 60]
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'L1': [10, 20, 30, 40, 50, 60], 'L2': [60, 61, 62, 63, 64, 65], 'L3': [10, 20, 30, 40, 50, 60, 61, 62, 63, 64, 65], 'L4': [60, 61, 62, 63, 64, 65, 10, 20, 30, 40, 50]}
>>> L5 = L1 * 3
>>> L5
[10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60]
