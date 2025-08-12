# 1
class Date : 
	pass

D = Date()

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

# -----------------------------------------
# 2
class Date :
	def __init__(self) :
		self.day = 1
		self.month = 1
		self.year = 1970

D = Date()

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

# ----------------------------------------
# 3
class Date :
	def __init__(self, day : int, month : int, year : int) :
		self.day = day
		self.month = month
		self.year = year


D = Date(22,9,2003)

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

D = Date(24, 11, 1978)

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

# ----------------------------------------
# 4
class Date :
	def __init__(self, day : int, month : int, year : int) :
		if type(day) != int :
			raise TypeError('Day must be an int')
		if type(month) != int :
			raise TypeError('month must be an int')
		if type(month) != int :
			raise TypeError('year must be an int')
		
		self.day = day
		self.month = month
		self.year = year

# D = Date('100', 2.2, 1990)

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

# ----------------------------------------
# 5

class Date :
	def __init__(self, day : int, month : int, year : int) :
		if type(day) != int :
			raise TypeError('Day must be an int')
		if type(month) != int :
			raise TypeError('Month must be an int')
		if type(year) != int :
			raise TypeError('year must be an int')
		
		self.day = day
		self.month = month
		self.year = year

	def show(self) :
		print(f'{self.day}/{self.month}/{self.year}')

D = Date(3, 8, 2025)

print("type(D)    :", type(D))
print("type(Date) :", type(Date))
print("D.__dict__ :", D.__dict__)

print()
D.show()

