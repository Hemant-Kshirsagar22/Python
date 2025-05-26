print("=========== START OF PROGRAM =============")

str_marks = input("Enter The Number : ")
marks = int(str_marks)

if marks < 35:
    print("Fail")
    
if marks >= 35:
    print("Pass")

if (marks >= 60 and marks <= 75) :
   print("With 1st Class")

if marks >= 50 and marks < 60 :
    print("With 2nd Class")

if marks >= 35 and marks < 50 :
    print("With 3rd Class")

print("=========== END OF PROGRAM ===============")
