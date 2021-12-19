class Car():
    """
    Car class
    Author : You
    Date: 2021.12.19.
    """
    # 클래스 변수 : 모든 인스턴스가 공유
    # 하나의 클래스에서 공통적으로 사용하는 변수를 선언할 때 사용
    car_count = 0

    def __init__(self, company, details):
        # self._compnay = 인스턴스 변수
        self._company = company
        self._details = details
        Car.car_count += 1

    # sef __str__(self) : 인스턴스 메서드
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print("del?")
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail info : {} {}'.format(self._company, self._details.get('price')))

# self의 의미
car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price' : 8000})
car2 = Car('BMW', {'color':'Black', 'horsepower':300, 'price' : 5000})
car3 = Car('AUDI', {'color':'RED', 'horsepower':400, 'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

# 값으로 비교
print(car1._company == car2._company)

# self를 이용하면 별도의 영역에 데이터가 생성됨
# id값으로 비교
print(car1 is car2)

# dir & __dict__
print(dir(car1))
print(dir(car2))

print(car1.__dict__)
print(car2.__dict__)

# Docstring
print(Car.__doc__)

# 실행
car1.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 에러
# 클래스로 접근할 떄는 인자를 전달해야한다.
Car.detail_info(car2)

# 클래스 변수 선언
print(car1.car_count)
print(car2.car_count)

# 공유 확인
# 클래스 변수를 확인할 떄는 dir로 확인하는게 좋다!
# 인스턴스 변수를 선언할 때는 _(언더바)를 앞에 붙이는게 좋다.
# dir로 확인 했을 떄, 클래스 변수와 구분 하기 위해서!!!!
print(dir(car1))

# 클래스 변수 접근
print(car1.car_count)
print(Car.car_count)

# del 메서드 호출과 클래스 변수 확인
del car2

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 > 상위(클래스 변수, 부모 클래스 변수))