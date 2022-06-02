class Car:
	def __init__(self):
		self.wheels = 4

	def drive(self):
		print('driving...')

hyundai = Car()

print(hasattr(hyundai, 'wheels'))
print(hasattr(hyundai, 'drive'))

method = getattr(hyundai, 'drive')
method()
