'''
데코레이터의 형태

- 함수만을 wrapping 할때
def decorator(func):
	def wrapper():
		func()
	return wrapper

@decorator
def 함수이름():
	코드

- 매개변수가 전달되는 함수를 wrapping 할때
def decorator(func):
	def wrapper(매개변수1, 매개변수2):
		return 반환값
	return wrapper
'''


# def trace(func):
# 	def wrapper(a, b):
# 		r = func(a, b)
# 		print(f'{func.__name__}({a} + {b}) = {r}')
# 	return wrapper
#
# @trace
# def hello(a, b):
# 	return a+b
#
# hello(1, 3)

# # 가변 인수 함수 데코레이터
# def trace(func):
# 	def wrapper(*args, **kwargs):
# 		r = func(*args, **kwargs)
# 		print(f'{func.__name__} args={args}, kwargs={kwargs}')
# 		return r
# 	return wrapper
#
#
# @trace
# def get_max(*args):
# 	return max(args)
#
#
# @trace
# def get_min(**kwargs):
# 	return min(kwargs.values())
#
# print(get_max(1,2,3,4,5))
# print(get_min(x=10, y=20, z=30))
#
# def trace(func):
# 	def wrapper(self, a, b):
# 		r = func(self, a, b)
# 		print(f'{a} + {b} = {a+b}')
# 		return r
# 	return wrapper
#
#
# class Calc:
# 	@trace
# 	def add(self, a, b):
# 		return a+b
#
# result = Calc()
# print(result.add(3, 5))
#
# def is_multiple(x):
# 	def real_decorator(func):
# 		def wrapper(a, b):
# 			r = func(a, b)
# 			if r % x == 0:
# 				print(f'{func.__name__}의 반환값은 {x}의 배수입니다.')
# 			else:
# 				print(f'{func.__name__}의 반환값은 {x}의 배수가 아닙니다.')
# 			return r
# 		return wrapper
# 	return real_decorator
#
# @is_multiple(7)
# @is_multiple(3)
# def add(a, b):
# 	return a+b
#
#
# print(add(3, 6))

# class Trace:
# 	def __init__(self, func):
# 		self.func= func
#
# 	def __call__(self):
# 		print(self.func.__name__, '함수 시작')
# 		self.func()
# 		print(self.func.__name__, '함수 끝')
#

class Trace:
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		r = self.func(*args, **kwargs)
		print(f'args={args}, kwargs={kwargs} -> {r}')
		return r


@Trace
def hello(a, b):
	return a+b

print(hello(10, 20))