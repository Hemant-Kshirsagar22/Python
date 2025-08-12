import os

# writing into the file
f_handle = open("abc.txt", "w")

print('type of f_handle : ', type(f_handle))

print("file descriptor : ", f_handle.fileno())

print("Writing into the file\n", file = f_handle)

L = [10, 20, 30, 40 ,50]

for x in L :
    print(x, file = f_handle)

f_handle.close()

# reading from file
f_handle = open("abc.txt", "r")

for line in f_handle :
    print(line.rstrip())

f_handle.close()