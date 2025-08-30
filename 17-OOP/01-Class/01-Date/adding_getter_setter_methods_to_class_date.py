class Date :
    def __init__(self, init_day : int, init_month : int, init_year : int) :
        self.day = init_day
        self.month = init_month
        self.year = init_year
    
    # getter of attribute 'day' / accessor method of attribute 'day'
    def get_day(self) -> int : 
        return self.day

    # getter of attribute 'month' / accessor method of attribute 'month'
    def get_month(self) -> int :
        return self.month
    
    # getter of attribute 'year' / accessor method of attribute 'year'
    def get_year(self) :
        return self.year
    
    # setter of attribute 'day' / mutator method of attribute 'day'
    def set_day(self, new_day : int) -> None :
        self.day = new_day
    
    # setter of attribute 'month' / mutator method of attribute 'month'
    def set_month(self, new_month : int) -> None :
        self.month = new_month
    
    # setter of attribute 'year' / mutator method of attribute 'year'
    def set_year(self, new_year : int) -> None :
        self.year = new_year

    def __str__(self) :
        return f"{self.day :02d} / {self.month :02d} / {self.year :4d}"
    
    
D = Date(1, 1, 1970)

print("D.__dict__ :", D.__dict__)
print("id(D) :", id(D))

print("\n\nGetter Method :")
day = D.get_day()     # day = Date.get_day(D)
month = D.get_month() # month = Date.get_month(D)
year = D.get_year()   # year = Date.get_year(D)

print("Day   :", day)
print("Month :", month)
print("Year  :", year)

print("\nBefore setting Value :", D)
D.set_day(22)
D.set_month(9)
D.set_year(2003)

print("After setting Value  :", D, end="\n\n\n")