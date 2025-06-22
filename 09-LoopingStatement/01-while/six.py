import sys

start_str = input("Enter Start Of Range : ")
start = int(start_str)

end_str = input("Enter End Of Range : ")
end = int(end_str)

if start > end :
    print("Enter End Greater Than Start !!!")
    sys.exit(0)

i = start

while i <= end :
    print(i)
    i = i + 1
