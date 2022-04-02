class Name:
	c_mem = 3  # --> 클래스 멤버

	@classmethod  # --> 데코레이터로 classmethod 선언 해줘야함.
	def cls_f(cls):  # --> 클래스 메소드
		print(cls.c_mem)


if __name__ == "__main__":
	a = Name
	print(Name.c_mem)
	Name.cls_f()
	print(a.c_mem)
	a.cls_f()

	# 모든 객체가 공통된 데이터를 가지면 클래스 멤버를 통해 선언하면 좋다.
	