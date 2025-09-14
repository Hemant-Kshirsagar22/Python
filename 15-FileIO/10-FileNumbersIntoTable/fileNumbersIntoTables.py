'''
 Discription : This program will read numbers from numbers.txt and create tables of that numbers and write down into table.txt

'''
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

def readNumbersFromFileAndCreateTables() -> bool :
    number_file_handle = open("numbers.txt", 'r')
    if number_file_handle == None :
        return False
    
    for line in number_file_handle :
        numbers = line.split(' ')

        for number in numbers :
            if number.isalnum() :
                if printTableIntoFile(int(number)) :
                    print(f"Table of {number} written into the file \"table.txt\"")
                else :
                    print(f"failed to create a table for {number}")
                    return False

    return True

def main() -> None :
    if readNumbersFromFileAndCreateTables() :
        print('tables created successfully')
    else :
        print('failed to create tables')
    
    sys.exit(0)

main()