class Date :
    def __init__(self, init_day : int, init_month : int, init_year : int) :
        self.day = init_day
        self.month = init_month
        self.year = init_year
    
    def __str__(self) :
        return f'{self.day} / {self.month} / {self.year}'

d = Date(22, 9, 2003)
print(d)