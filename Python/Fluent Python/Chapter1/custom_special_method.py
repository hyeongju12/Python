from math import hypot, sqrt


class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'({self.x}, {self.y})'

	def __abs__(self, a=1):
		return sqrt(self.x ** 2 + self.y ** 2) * a

	def __add__(self, other):
		return Vector(self.x + other.x , self.y + other.y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

a = Vector(3, 4)
b = Vector(5, 6)

print(a)
print(b)
print(abs(a * 3))
print(a+b)

'''
	특별 메서드를 구현하면 사용자 정의 객체도 내장형 객체처럼 작동하게 되어,
	조금 더 파이썬 스러운 프로그래밍을 할 수 있다. 
'''