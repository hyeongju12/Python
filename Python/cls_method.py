class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def init_from_string(cls, string):
		name, age = string.split('_')
		return cls(name, int(age))

a = Person.init_from_string('mark_30')

print(a.name)
print(a.age)

'''
생성자의 인자로 name과 age를 입력받는다.
멤버 데이터로 문자열이 들어온다. <name>_<age> 형태면
클래스 메서드(init_from_string) 대체 생성자를 통해
객체 멤버를 초기화 한다.
 
'''