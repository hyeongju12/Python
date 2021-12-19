class Car():
    """
    Car class
    Author : You
    Date: 2021.12.19.
    """
    def __init__(self, company, details):
        # self._compnay = 인스턴스 변수
        self._company = company
        self._details = details

    # sef __str__(self) : 인스턴스 메서드
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

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