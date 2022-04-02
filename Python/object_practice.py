class Person:
	def __init__(self, name, money):
		self.name = name
		self.money = money

	def give_money(self, other, money):
		self.money -= money
		other.money += money

	def get_money(self, money):
		self.money += money

	def show(self):
		print(f'{self.name}', {self.money})


if __name__ == '__main__':
	j = Person('john', 10000)
	m = Person('mark', 6000)

	j.give_money(m, 3000)

	j.show()
	m.show()

	print(type(Person.__init__))
	print(type(Person.get_money))

	print(type(j.__init__))
	print(type(j.get_money))

	print(dir(j.get_money))
	print(j.get_money.__self__)
	print(j.get_money.__func__)
	print(Person.get_money is j.get_money.__func__)
	print(j.give_money.__self__ is j)
