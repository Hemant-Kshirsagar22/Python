'''
@Author : Hemant Ganesh Kshirsagar
@Goal : To Create Basic Student class
@date : 16 / 08 / 2025
'''

class Student :
    def __init__(self, init_roll_number : int, init_name : str, init_age : int, init_std : int, init_marks : float) :
        self.roll_number = init_roll_number
        self.name = init_name
        self.age = init_age
        self.std = init_std
        self.marks = init_marks

    def __str__(self) :
        return f'{self.__dict__}'
    
    def show(self) -> None :
        print(self.__dict__)

student_one = Student(101, 'Hemant', 22, 17, 70.0)
print(student_one)
student_one.show()