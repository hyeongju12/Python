class Stock:
	def __getattribute__(self, item):
		print(f'{item} 객체에 접근하였습니다.')

c = Stock()
print(c.data)