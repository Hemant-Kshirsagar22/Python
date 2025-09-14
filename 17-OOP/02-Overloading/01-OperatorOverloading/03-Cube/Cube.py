class Cube :
    def __init__(self, s : float):
        if type(s) != int and type(s) != float :
            raise TypeError('side of the cube should be int/float')
        self.s = s

    def area(self) -> float :
        return self.s * self.s 

    def perimeter(self) -> float :
        return 6 * 4 * self.s

    def surfaceArea(self) -> float :
        return 6 * (self.s * self.s)

    def volume(self) -> float :
        return self.s * self.s * self.s

    def __add__(self, other) :
        return Cube(self.s + other.s)
    
    def __sub__(self, other) :
        return Cube(self.s - other.s)

    def __mul__(self, other) :
        return Cube(self.s * other.s)

    def __str__(self):
        return f"Cube({self.s})"

c1 = Cube(5)
c2 = Cube(2)

print(f"area : {c1.area()}")
print(f"perimeter : {c1.perimeter()}")
print(f"surface area : {c1.surfaceArea()}")
print(f"volume : {c1.volume()}")

c3 = c1 + c2
print(f"{c1} + {c2} = {c3}")

c3 = c1 - c2
print(f"{c1} - {c2} = {c3}")

c3 = c1 * c2
print(f"{c1} * {c2} = {c3}")
