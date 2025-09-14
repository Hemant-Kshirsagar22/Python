
class Complex :
    def __init__(self, x : float, y : float) :
        if type(x) != int and type(x) != float :
            raise TypeError('real part of complex number must be a numerical value')

        if type(y) != int and type(y) != float :
            raise TypeError('imaginory part of complex number must be a numerical value')
        self.x = x
        self.y = y

    def __str__(self) :
        return f"({self.x:.2f}) + ({self.y:.2f})i"

    def __add__(self, other) :
        add_x = self.x + other.x
        add_y = self.y + other.y
        add_c = Complex(add_x, add_y)
        return add_c
    
    def __sub__(self, other) :
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        sub_c = Complex(sub_x, sub_y)
        return sub_c
    
    def __mul__(self, other) :
        mul_x = self.x * other.x - self.y * other.y
        mul_y = self.x * other.y + self.y * other.x
        mul_c = Complex(mul_x, mul_y)
        return mul_c

    def __truediv__(self, other) :
        if other.x == 0.0 and other.y == 0.0 :
            raise ZeroDivisionError('cannot divide by 0')
        
        div_x = (self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2)
        div_y = (other.x * self.y - self.x * other.y) / (other.x ** 2 + other.y ** 2)
        div_c = Complex(div_x, div_y)
        return div_c
    
    def __ne__(self, other) -> bool :
        b = (self.x != other.x) and (self.y != other.y)
        return b

    def __eq__(self, other) -> bool : 
        b = (self.x == other.x) and (self.y == other.y)
        return b


print("Complex with Operator Overloading")

c1 = Complex(1.1, 2.2)
c2 = Complex(3.4, 6.5)
c3 = Complex(1.1, 2.2)

print(f'C1 : {c1}')
print(f'C2 : {c2}')
print(f'C3 : {c3}')

c_sum = c1 + c2
print(f"c_sum : {c_sum}")

c_sub = c1 - c2
print(f"c_sub : {c_sub}")

c_mul = c1 * c2
print(f"c_mul : {c_mul}")

c_div = c1 / c2
print(f"c_div : {c_div}")

if c1 != c2 :
    print("c1 and c2 are not equal")

if c1 == c3 :
    print("c1 and c3 are equal")
