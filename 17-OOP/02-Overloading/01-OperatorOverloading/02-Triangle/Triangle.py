import math
class Triangle :
    def __init__(self, a : float, b : float, c : float) :
        if type(a) != int and type(a) != float :
            raise TypeError('please enter int/float value for side A of triangle')
        
        if type(b) != int and type(b) != float :
            raise TypeError('please enter int/float value for side B of triangle')
        
        if type(c) != int and type(c) != float :
            raise TypeError('please enter int/float value for side C of triangle')
        
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float :
        '''
        s = (a + b + c) / 2
        area = sqrt((s * (s - a) * (s - b) * (s - c)))
        '''
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt((s * (s - self.a) * (s - self.b) * (s - self.c)))
        return area
    
    def perimeter(self) -> float :
        return self.a + self.b + self.c
    
    def isEquilataral(self) -> bool :
        return (self.a == self.b) and (self.b == self.c)
    
    def isRightAngleTriangle(self) -> bool :
        m = max(self.a, max(self.b, self.c))
        if m == self.a:
            if math.pow(self.a, 2) == math.pow(self.b, 2) + math.pow(self.c, 2) :
                return True
        elif m == self.b :
            if math.pow(self.b, 2) == math.pow(self.a, 2) + math.pow(self.c, 2) :
                return True
        else :
            if math.pow(self.c, 2) == math.pow(self.a, 2) + math.pow(self.b, 2) :
                return True
        return False
            
    def __add__(self, other) :
        return Triangle((self.a + other.a), (self.b + other.b), (self.c + other.c))
    
    def __sub__(self, other) :
        return Triangle((self.a - other.a), (self.b - other.b), (self.c - other.c))
    
    def __mul__(self, other) :
        return Triangle((self.a * other.a), (self.b * other.b), (self.c * other.c))
    
    def __str__(self) :
        return f"Triangle[{self.a}, {self.b}, {self.c}]"
    
t1 = Triangle(5, 4, 3)
t2 = Triangle(5, 2, 3)

t3 = t1 + t2
print(f"{t1} + {t2} = {t3}")

t3 = t1 * t2
print(f"{t1} * {t2} = {t3}")

t3 = t1 - t2
print(f"{t1} - {t2} = {t3}")

print(f"area : {t1.area()}")
print(f"perimeter : {t1.perimeter()}")
print(f"is right angle : {t1.isRightAngleTriangle()}")
print(f"is equilateral triangle : {t1.isEquilataral()}")


