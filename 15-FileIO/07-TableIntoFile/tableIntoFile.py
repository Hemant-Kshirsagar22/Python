import sys

def printTableIntoFile(number : int) -> bool :
    file_handle = open('table.txt', 'w')
    if(file_handle == None) :
        print('Failed To Open File !!!')
        return False

    for x in range(1, 11) :
        print(f"{number} * {x} = {number * x}", file=file_handle)
    
    file_handle.close()
    return True

def main() -> None :
    number = int(input("Enter The Number For creating table : "))
    
    if printTableIntoFile(number) :
        print("Table written into the file \"table.txt\"")
    else :
        print("failed to create a table")
    sys.exit(0)

main()