
class GSPAInt :
    def __init__(self, num : int) :
        if type(num) != int :
            raise TypeError("give integer value for creating object of GSPAInt")
        self.num = num

    def __str__(self) :
        return f'{self.num}'
    
    def __add__(self, other) :
        add_num = self.num + other.num
        newGSPAInt = GSPAInt(add_num)
        return newGSPAInt
    
    def __sub__(self, other) :
        sub_num = self.num - other.num
        newGSPAInt = GSPAInt(sub_num)
        return newGSPAInt
    
    def __mul__(self, other) :
        mul_num = self.num * other.num
        newGSPAInt = GSPAInt(mul_num)
        return newGSPAInt
    
    def __truediv__(self, other) :
        if other.num == 0 :
            raise ZeroDivisionError('denominator must not be 0')
        div_num = self.num / other.num
        return div_num
    
    def __floordiv__(self, other) :
        if other.num == 0 :
            raise ZeroDivisionError('denominator must not be 0')
        quotient = self.num // other.num
        newGSPAInt = GSPAInt(quotient)
        return newGSPAInt
        
    def __mod__(self, other) :
        if other.num == 0 :
            raise ZeroDivisionError('denominator must not be 0')
        reminder = self.num % other.num
        newGSPAInt = GSPAInt(reminder)
        return newGSPAInt

    def __pow__(self, other) :
        pow = self.num ** other.num
        newGSPA = GSPAInt(pow)
        return newGSPA
    
    def __gt__(self, other) -> bool :
        return self.num > other.num
    
    def __ge__(self, other) -> bool :
        return self.num >= other.num
    
    def __lt__(self, other) -> bool :
        return self.num < other.num
    
    def __le__(self, other) -> bool :
        return self.num <= other.num
    
    def __eq__(self, other) -> bool :
        return self.num == other.num
    
    def __ne__(self, other) -> bool :
        return self.num != other.num
    
print("Showing GSPA int")

gn1 = GSPAInt(17)
gn2 = GSPAInt(18)

gn_sum = gn1 + gn2
gn_sub = gn1 - gn2
gn_mul = gn1 * gn2

print(f"gn_sum : {gn_sum}")
print(f"gn_sub : {gn_sub}")
print(f"gn_mul : {gn_mul}")

gn_quotient = gn1 // gn2 # __floordiv__
print(f"gn_quotient : {gn_quotient}")

gn_reminder = gn1 % gn2 # __mod__
print(f"gn_remider : {gn_reminder}")

f_div = gn1 / gn2 # __truediv__
print(f"f_div : {f_div}")

gn_power = gn1 ** gn2 # __power__
print(f"gn_power : {gn_power}")

b = gn1 > gn2 # __gt__
print(f"gn1 > gn2 : {b}")

b = gn1 >= gn2 # __ge__
print(f"gn1 >= gn2 {b}")

b = gn1 < gn2 # __lt__
print(f"gn1 < gn2 : {b}")

b = gn1 <= gn2 # __le__
print(f"gn1 <= gn2 : {b}")

b = gn1 == gn2 # __eq__
print(f"gn1 == gn2 : {b}")

b = gn1 != gn2 # __ne__
print(f"gn1 != gn2 : {b}")
