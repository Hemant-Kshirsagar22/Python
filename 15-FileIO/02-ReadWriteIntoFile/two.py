import os

# wrting into file

f_handle = open("abc.txt", "w")

print("type(f_handle) :", type(f_handle))

print("file descriptor : ", f_handle.fileno())

print("writing into the file", file = f_handle)

L = [10, 20, 30, 40, 50]

for i in range(len(L)) :
    print(f"L[{i}] : {L[i]}", file = f_handle)

f_handle.close()

# reading file

f_handle = open('abc.txt', 'r')

for line in f_handle :
    print(line.rstrip())

f_handle.close()
