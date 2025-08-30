class Date :
    def __init__(self, init_day : int, init_month : int, init_year : int) :
        self.day = init_day
        self.month = init_month
        self.year = init_year
    
    def get_day(self) : 
        print("get_day() : id(self) :", id(self))
        day_value = self.day
        return day_value

    def get_month(self) :
        print("get_month() : id(self) :", id(self))
        month_value = self.month
        return month_value
    
    def get_year(self) :
        print("get_year() : id(self) :", id(self))
        year_value = self.year
        return year_value
    
D = Date(1, 1, 1970)

print("D.__dict__ :", D.__dict__)
print("id(D) :", id(D))

day = D.get_day() # day = Date.get_day(D)
month = D.get_month() # month = Date.get_month(D)
year = D.get_year() # year = Date.get_year(D)

print("Day   :", day)
print("Month :", month)
print("Year  :", year)