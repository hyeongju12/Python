'''
파이썬에서는 C++ 처럼 정보 은닉 기능이 없다.
대체 방법 2가지가 있는데,
1. __멤버 <- 숨기려는 멤버 변수 앞에 언더바 두 개를 붙인다.
2. 프로퍼티 기법
'''

# __멤버 사용
# class Account:
# 	def __init__(self, name, money):
# 		self.name = name
# 		self.__balance = money
#
# 	def get_balance(self):
# 		return self.__balance
#
# 	def set_balance(self, money):
# 		if money<0:
# 			return
# 		self.__balance = money
#
# if __name__ == "__main__":
# 	my_acnt = Account('mark', 5000)
# 	my_acnt.__balance = -3000
# 	my_acnt._Account__balance = 8000 --> 변경된 이름으로 접근이 가능하다. 의도적인 접근은 막을 수 없다.
#
# 	print(my_acnt.get_balance())
#
# 	print(my_acnt.__dict__)

# 프로퍼티 사용법
class Account:
	def __init__(self, name, money):
		self.name = name
		self._balance = money

	@property # property 데코레이터를 붙인다.
	def balance(self): # -> balance 함수는 getter() 함수가 된다. // 값을 가져오는 역할
		return self._balance

	@balance.setter # getter 함수와 같은 이름을 가진 함수 위에 @balance.setter라고 데코레이터를 붙여준다.
	def balance(self, money): # 이 함수는 setter 함수가 되고 가져온 값으로 _balance를 초기화 한다.
		if money<0:
			return
		self._balance = money

if __name__ == "__main__":
	my_acnt = Account('mark', 5000)
	my_acnt.balance = -3000 # 객체의 balance라는 멤버의 값을 변경하려 하지만
	# my_acnt 객체에는 balance라는 멤버가 없다. 따라서 변경되는 값은 없다.
	# __dict__으로 구성을 봤을 때 {'name': 'mark', '_balance': -3000}
	# 위 변수명으로 접근하게 되면 값을 변경 할 수 있다.

	# 위 방법은 getter와 setter 함수인 balance를 호출하여 값이 변경 됨.

	my_acnt._balance = -3000
	print(my_acnt.__dict__)

