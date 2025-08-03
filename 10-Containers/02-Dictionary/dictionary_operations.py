Python 3.12.8 (v3.12.8:2dc476bcb91, Dec  3 2024, 14:43:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
D = {}
D
{}
D = {'A' : 10}
D
{'A': 10}
D['B'] = 20
D
{'A': 10, 'B': 20}
D[True] = 30
print(D)
{'A': 10, 'B': 20, True: 30}
D[False] = 40
D
{'A': 10, 'B': 20, True: 30, False: 40}
D['Hello'] = 50
D
{'A': 10, 'B': 20, True: 30, False: 40, 'Hello': 50}
D[(10,20)] = 60
D
{'A': 10, 'B': 20, True: 30, False: 40, 'Hello': 50, (10, 20): 60}
D[10.10] = 70
D
{'A': 10, 'B': 20, True: 30, False: 40, 'Hello': 50, (10, 20): 60, 10.1: 70}
del D['B']
D
{'A': 10, True: 30, False: 40, 'Hello': 50, (10, 20): 60, 10.1: 70}
del D[(10, 20)]
D
{'A': 10, True: 30, False: 40, 'Hello': 50, 10.1: 70}
del D['K']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del D['K']
KeyError: 'K'
D['A'] = 100
D
{'A': 100, True: 30, False: 40, 'Hello': 50, 10.1: 70}
D[True] = 400
D
{'A': 100, True: 400, False: 40, 'Hello': 50, 10.1: 70}



# creating empty dictionary
D = {}
D
{}
# inserting elements in dictionary
D['A'] = 10
D
{'A': 10}
D['B'] = 20
D
{'A': 10, 'B': 20}
D[False] = 30
D[(1, 2)] = 40
D
{'A': 10, 'B': 20, False: 30, (1, 2): 40}
>>> 
>>> # Deleting elemenets from dictionary
>>> del D['A']
>>> D
{'B': 20, False: 30, (1, 2): 40}
>>> del D[(1, 2)]
>>> D
{'B': 20, False: 30}
>>> 
>>> del D['B']
>>> D
{False: 30}
>>> 
>>> del D[False]
>>> D
{}
>>> 
>>> D = {'A' : 10}
>>> D
{'A': 10}
>>> D['B'] = 20
>>> D
{'A': 10, 'B': 20}
>>> 
>>> # modifying dictionary
>>> D['A'] = 20
>>> D
{'A': 20, 'B': 20}
>>> D['B'] = False
>>> D
{'A': 20, 'B': False}
>>> D['C'] = 30 # key is not present hence key-value will be inserted
>>> D
{'A': 20, 'B': False, 'C': 30}
