import sys

class Quadrilateral :
    def __init__(self, s1 : float, s2 : float, s3 : float, s4 : float) :
        # validation check 1 : s1, s2, s3, s4 must be type of int or float
        acceptable_type = [int, float] 
        if(
            type(s1) not in acceptable_type or
            type(s2) not in acceptable_type or
            type(s3) not in acceptable_type or
            type(s4) not in acceptable_type
        ) :
            print('Type of all side must be int or float')
            sys.exit(-1)
        
        # validation check 2 : s1, s2, s3, s4 all must be +ve
        if s1 <= 0.0 or s2 <= 0.0 or s3 <= 0.0 or s4 <= 0.0 :
            print("lengths of all side must be +ve")
            sys.exit(-1)
        
        # validation check 3 : sum of length of any three side of quadrilateral must be grreater than the fourth
        if(
            (s1 + s2 + s3) <= s4 or
            (s1 + s2 + s4) <= s3 or
            (s1 + s3 + s4) <= s2 or
            (s2 + s3 + s4) <= s1 
        ) :
            print("Given four positive numbers do not form a valid side length of quadrilateral")
            sys.exit(-1)
        
        # create four attributes name s1, s2, s3, s4 in newly allocated objects and initialize them by formal parameters of s1, s2, s3, s4
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self) :
        return self.s1 + self.s2 + self.s3 + self.s4
    
    def area(self) :
        s = self.perimeter() / 2.0
        return((s - self.s1) * (s - self.s2) * (s - self.s3) * (s - self.s4)) ** 0.5
    
    def __str__(self) :
        return f'Q[{self.s1}, {self.s2}, {self.s3}, {self.s4}]'
    

q_s1 = 2.8
q_s2 = 3.2
q_s3 = 4.5
q_s4 = 1.6

Q = Quadrilateral(q_s1, q_s2, q_s3, q_s4)
P = Q.perimeter()
A = Q.area()

print(f"Perimeter of Quadrilateral {Q} : {P:.2f}")
print(f"Area of Quadrilateral {Q}      : {A:.2f}")