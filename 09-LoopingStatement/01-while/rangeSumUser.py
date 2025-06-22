print('start of program')

start_str = input('Enter Start Of Program : ')
start = int(start_str)

end_str = input('Enter End Of Program : ')
end = int(end_str)

if start > end:
    temp = start
    start = end
    end = temp
    
i = start
addition = 0

while i <= end :
    addition = addition + i
    i = i + 1

print('sum of', start_str, 'to', end_str, 'is', addition)
print('End Of Program')
