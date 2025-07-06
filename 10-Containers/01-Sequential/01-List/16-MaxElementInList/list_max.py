print('start of program')

L = [10, 20, 130, 40, 50, 60, 70, 80, 9, 10]

max = L[0]
for x in L :
    if max < x :
        max = x

print(f"Max Element in List {L} is : {max}")
print('End of program')