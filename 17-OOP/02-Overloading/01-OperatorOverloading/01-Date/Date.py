class Date :
    def __init__(self, day, month, year) :
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self) :
        return f'{self.day:02d} / {self.month:02d} / {self.year:02d}'
    
    def addDate(self, date) :
        newDay = self.day + date.day
        newMonth = self.month + date.month
        newYear = self.year + date.year
        print(f"Addition of date using addDate()\n{newDay} / {newMonth} / {newYear}")
    
    def __add__(self, date) :
        newDay = self.day + date.day
        newMonth = self.month + date.month
        newYear = self.year + date.year
        newDate = Date(newDay, newMonth, newYear)
        return newDate
    
D1 = Date(22, 9, 2003)
D2 = Date(30, 8, 2025)

D1.addDate(D2)

D3 = D1 + D2
print(D3)
