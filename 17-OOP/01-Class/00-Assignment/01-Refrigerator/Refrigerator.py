'''
Refrigerator

attributes
brand           : str
model           : str
capacity        : str
color           : str
voltage         : int
numberOfDrawers : int
material        : str
'''
class Refrigerator :
    def __init__(self,
                brand : str, 
                model : str,
                capacity : str,
                color : str,
                voltage : int,
                numberOfDrawers : int,
                material : str):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.color = color
        self.voltage = voltage
        self.numberOfDrawers = numberOfDrawers
        self.material = material
    
    def __str__(self) :
        return f"Refrigerator\nbrand           : {self.brand}\nmodel           : {self.model}\ncapacity        : {self.capacity}\ncolor           : {self.color}\nvoltage         : {self.voltage}\nnumberOfDrawers : {self.numberOfDrawers}\nmaterial        : {self.material}"
    
R = Refrigerator(
    "Whirlpool",
    "205 WDE CLS 25",
    "184 liters",
    "SAPPHIRE BLUE-Z",
    220,
    4,
    "Stainless Steel"
)

print(R)