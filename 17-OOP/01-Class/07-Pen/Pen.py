'''
@Author : Hemant Ganesh Kshirsagar
@Goal : Create a Pen class
@Date : 16 / 08 / 2025
'''

class Pen :
    def __init__(self, init_company : str, init_pen_type : str, init_ink_type : str, init_ink_color : str, init_price : float) :
        self.company = init_company
        self.pen_type = init_pen_type
        self.ink_type = init_ink_type
        self.ink_color = init_ink_color
        self.price = init_price
    
    def __str__(self) :
        return f'{self.__dict__}'
    
    def show(self) -> None :
        print(f'{self.__dict__}')

pen = Pen('Lexi', 'ink pen', 'ball', 'blue', 200.0)
pen.show()
print(pen)