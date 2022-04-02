class Account:
	num_acnt = 0

	@classmethod
	def get_num_acnt(cls):
		return cls.num_acnt

	def __init__(self, name, money):
		self.user = name
		self.balance = money
		Account.num_acnt += 1

	def deposit(self, money):
		if money < 0:
			return '금액을 넣어주세요.'
		self.balance += money

	def withdraw(self, money):
		if money>0 and money <= self.balance:
			self.balance -= money
			return money
		else:
			return '금액이 부족합니다.'

	def transfer(self, other, money):
		mon = self.withdraw(money)
		if mon:
			other.deposit(mon)
			return '송금 했습니다.'
		else:
			return '금액을 입력해주세요'

	def __str__(self):
		return f'user : {self.user}, money : {self.balance}'

if __name__ == "__main__":
	my_acnt = Account('hyeongju', 10000)
	your_acnt = Account('hyeonji', 8000)

	my_acnt.deposit(5000)

	my_acnt.transfer(your_acnt, 3000)

	print(my_acnt.__str__())
	print(your_acnt.__str__())


