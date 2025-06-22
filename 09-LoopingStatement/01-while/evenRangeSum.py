print('Start of program')

str_start = input('Enter The start : ')
start = int(str_start)

str_end = input('Enter The End : ')
end = int(str_end)

if start > end :
    temp = start
    start = end
    end = temp

i = start
addition = 0

while i <= end :
    if i % 2 == 0 :
        addition = addition + i
    i = i + 1

print('Even Number Sum Between', str_start, 'to', str_end, 'is', addition)
print('End Of Program')

        
