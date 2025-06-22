print("Start Of Program")

numberOfClassRooms_str = input("Number Of ClassRooms : ")
numberOfClassRooms = int(numberOfClassRooms_str)

numberOfBenches_str = input("NumberOfClassRooms : ")
numberOfBenches = int(numberOfBenches_str)

totalNumberOfBenches = 0

i = 0
while i < numberOfClassRooms :
    j = 1
    while j <= numberOfBenches :
        totalNumberOfBenches = totalNumberOfBenches + 1
        j = j + 1
    i = i + 1

print("Total Number Of Benches : ", totalNumberOfBenches)

print("End Of Program")

        
    
