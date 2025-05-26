str_a = input("Enter The first Operand  : ")
a = int(str_a)

str_b = input("Enter The Second Operand : ")
b = int(str_b)

print("operand 1 : ", a)
print("operand 2 : ", b)

print("======= Relational Operators ========")

c = a == b
print('a == b : (', a, ' == ', b,') : ', c)

c = a != b
print('a != b : (', a, ' != ', b,') : ', c)

c = a > b
print('a > b  : (', a, ' > ', b,')  : ', c)

c = a < b
print('a > b  : (', a, ' < ', b,')  : ', c)

c = a <= b
print('a <= b : (', a, ' <= ', b,') : ', c)

c = a >= b
print('a >= b : (', a, ' >= ', b,') : ', c)
