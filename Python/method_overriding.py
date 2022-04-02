class CarOwner:
	def __init__(self, name):
		self.name = name

	def concentrate(self):
		print(f'{self.name} can not do anything else')

class Car:
	def __init__(self, owner_name):
		self.owner = CarOwner(owner_name)

	def drive(self):
		self.owner.concentrate()
		print(f'{self.owner.name} is driving now')

class SelfDrivingCar(Car):
	def drive(self):
		print('Car is driving by itself')

if __name__ == "__main__":
	car = Car('greg')
	car.drive()

	car_2 = SelfDrivingCar('mark')
	car_2.drive()