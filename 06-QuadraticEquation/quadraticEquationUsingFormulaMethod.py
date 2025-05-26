print(" - - - - - - - Quadratic Equation ( Formula Method ) - - - - - - -")

str_a = input("Enter Co-efficient Of X^2 : ")
a = float(str_a)

str_b = input("Enter Co-efficient Of X : ")
b = float(str_b)

str_c = input("Enter Constant C : ")
c = float(str_c)

print("\nQuadratic Equation :")
print(a, "X^2 + ", b ,"X + ", c)

root1 = ( -b + (((b ** 2) - (4 * a * c)) ** 0.5)) / 2 * a

root2 = ( -b - (((b ** 2) - (4 * a * c)) ** 0.5)) / 2 * a

print("\nRoot1 : ", root1)
print("\nRoot2 : ", root2)

print("\n")

print("- - - - - - - - End Of Program - - - - - - - - - - -")
