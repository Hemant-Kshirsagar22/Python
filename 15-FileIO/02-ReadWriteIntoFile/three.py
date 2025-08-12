import os

f_handle = open('abc.txt', 'w')

print("type(f_handle) : ", type(f_handle))

print("file Descriptor", f_handle.fileno())

print('first line inside the file', file = f_handle)

L = [1, 2, 3, 4, 5]

i = 0
while i < len(L) :
    print(f"L[{i}] = {L[i]}", file = f_handle)
    i += 1

f_handle.close()

# read
f_handle = open('abc.txt', 'r')

for line in f_handle :
    print(line.rstrip())

f_handle.close()
