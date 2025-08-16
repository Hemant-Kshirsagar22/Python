'''
@Author : Hemant Ganesh Kshirsagar
@Date : 16 / 08 / 2025
@Goal : Create a basic Time class 
'''

class Time :
    def __init__(self, init_hour : int, init_minutes : int, init_second : int, init_format : bool) :
        '''
        @init_format : true when we use 24 hrs format, false when we use 12 hrs
        '''
        self.hour = init_hour
        self.minutes = init_minutes
        self.second = init_second
        self.format = init_format

    def __str__(self):
        return f'{self.hour:02d} : {self.minutes:02d} : {self.second:02d}'
    
    def show(self) -> None :
        print(f'{self.hour:02d} : {self.minutes:02d} : {self.second:02d}')

time = Time(12, 55, 0, True)
time.show()
print(time)


time = Time(1, 55, 0, True)
time.show()
print(time)