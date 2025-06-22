start_str = input("Enter Start Of Range : ")
start = int(start_str)

end_str = input("Enter End Of Range : ")
end = int(end_str)

if start < end :
    while start <= end :
        print(start)
        start = start + 1
else :
    while start >= end :
        print(start)
        start = start - 1
