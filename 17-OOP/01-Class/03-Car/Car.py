'''
@Author : Hemant Ganesh Kshirsagar
@Date : 16 / 08 / 2025
'''

class Car :
    def __init__(self, init_company_name : str, init_model : str, init_horse_power : int, init_fuel_type : str) :
        self.company_name = init_company_name
        self.model = init_model
        self.horse_power = init_horse_power
        self.fuel_type = init_fuel_type
    
    def __str__(self) :
        return f'{self.__dict__}'
    
    def show(self) :
        print(self.__dict__)

car_one = Car('Tata', 'Safarri', 300, 'Petrol')
print(car_one)
car_one.show()