from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
	@abstractmethod
	def eat(self):
		print('eat something')

class Human(Animal):
	def eat(self):
		print('eat rice')

class Lion(Animal):
	def eat(self):
		print('eat meat')

if __name__ == "__main__":
	a = Animal()
