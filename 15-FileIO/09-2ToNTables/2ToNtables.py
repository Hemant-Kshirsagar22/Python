import sys

def printTableIntoFile(number : int) -> bool :
    file_handle = open('table.txt', 'a')
    if file_handle == None :
        file_handle = open('table.txt', 'w')
        if file_handle == None :
            return False

    for x in range(1, 11) :
        print(f"{number} * {x} = {number * x}", file=file_handle)
    print(file=file_handle)
    file_handle.close()
    return True

def main() -> None :
    number = int(input("Enter The Number For creating table : "))
    for number in range(2, number + 1) :  
        if printTableIntoFile(number) :
            print(f"Table of {number} written into the file \"table.txt\"")
        else :
            print(f"failed to create a table of {number}")
    sys.exit(0)

main()