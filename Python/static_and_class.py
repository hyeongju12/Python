class A:

	@staticmethod
	def f():
		print('static method')

	@classmethod
	def g(cls):
		print(cls.__name__)


print(type(A.f))
print(type(A.g))

'''
정적 메서드는 인자로 클래스나 객체를 받지 않는다.
함수만 클래스 A 네임 스페이스에 있을 뿐 일반 함수와 같으며, 전역 함수를 대체하기에
알맞다. 
'''