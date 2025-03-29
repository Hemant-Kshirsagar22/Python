# Compute Gravity
print(" ------------------ Compute Gravity ---------------------")

str_m1 = input("Enter Mass Of Object One (Kg) : ")
m1 = float(str_m1)

str_m2 = input("Enter Mass Of Object Two (Kg) : ")
m2 = float(str_m2)

str_r = input("Enter Distance Between Two Objects : ")
r = float(str_r)

G = 6.67430 * (10 ** -11)

force = G * ((m1 * m2) / (r ** 2))

print("Force Applied : ", force)

print(" ------------------ End Of Program -----------------------")
