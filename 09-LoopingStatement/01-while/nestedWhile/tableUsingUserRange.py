print("Start Of Program")

start_str = input("Start Of Table : ")
start = int(start_str)

end_str = input("End Of Table : ")
end = int(end_str)

if start <= end :
    i = 1
    while i <= 10 :
        j = start
        while j <= end :
            multiplication = j * i
            print(j, "*", i, "=", multiplication, end="\t")
            j = j + 1
        print()
        i = i + 1
else :
    i = 1
    while i <= 10 :
        j = start
        while j >= end :
            multiplication = j * i
            print(j, "*", i, "=", multiplication, end="\t")
            j = j - 1
        print()
        i = i + 1
