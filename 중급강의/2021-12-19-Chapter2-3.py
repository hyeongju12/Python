class Car():
    """
    Car class
    Author : You
    Date: 2021.12.19.
    Description : Class, Static, Intance Method
    """
    # 클래스 변수 : 모든 인스턴스가 공유
    # 하나의 클래스에서 공통적으로 사용하는 변수를 선언할 때 사용
    price_per_raise = 1.0

    def __init__(self, company, details):
        # self._compnay = 인스턴스 변수
        self._company = company
        self._details = details

    # sef __str__(self) : 인스턴스 메서드
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    #Instance Method
    #Self : 객체의 고유한 속성 값을 사용한다.

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")

    # Static method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'This is not bmw!'

# self의 의미
car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price' : 8000})
car2 = Car('BMW', {'color':'Black', 'horsepower':300, 'price' : 5000})


# 전체정보
car1.detail_info()

# 가격정보 * 직접 접근하는 것은 좋지 않음. 메소드를 이용하는 방법이 좋음.
print(car1._details.get('price'))

Car.price_per_raise = 1.4

#인스턴스로 호출
print(car1.get_price())
print(car1.get_price_culc())

#클래스로 호출
Car.raise_price(1)
Car.raise_price(1.6)

print(car1.get_price())
print(car1.get_price_culc())

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

print(Car.is_bmw(car1))