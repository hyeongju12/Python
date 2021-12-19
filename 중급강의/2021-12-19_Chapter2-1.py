# 일반적인 코딩

# 방법 1. copy & paster
# 단점 
# 1. 차량의 종류 증가에 따라 데이터를 복사/붙여넣기를 반복
# 2. 자동차의 데이터가 변경되면 찾아서 수정해야하는 불편함

# 차량1
car_company = "Ferrari"
car_detail_1 = [
    {'color':'white'},
    {'horsepower':400},
    {'price' : 8000}
]

# 차량2
car_company = "BMW"
car_detail_1 = [
    {'color':'Black'},
    {'horsepower':300},
    {'price' : 5000}
]


# 차량3
car_company = "AUDI"
car_detail_1 = [
    {'color':'RED'},
    {'horsepower':400},
    {'price' : 6000}
]

# 방법2. 리스트 구조
# 단점
# 1. 리스트는 인덱스를 이용하여 데이터 관리
# 2. 인덱스를 이용함에 따른 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list =[
    {'color':'white', 'horsepower':400, 'price' : 8000},
    {'color':'Black', 'horsepower':300, 'price' : 5000},
    {'color':'RED', 'horsepower':400, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 방법3. 딕셔너리 구조
# 단점
# 1. 코드 반복사용
# 2. 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company' : 'Ferarry', 'car_detail' : {'color':'white', 'horsepower':400, 'price' : 8000}},
    {'car_company' : 'BMW', 'car_detail' : {'color':'Black', 'horsepower':300, 'price' : 5000}},
    {'car_company' : 'AUDI', 'car_detail' : {'color':'RED', 'horsepower':400, 'price' : 6000}},
]

print(car_dicts)
del car_dicts[1]
print(car_dicts)

# 방법4. 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # def __str__(self):
    #     return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price' : 8000})
car2 = Car('BMW', {'color':'Black', 'horsepower':300, 'price' : 5000})
car3 = Car('AUDI', {'color':'RED', 'horsepower':400, 'price' : 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 파이썬에 구현된 매직 메소드(스페셜 메소드)
# 반복문(__str__)이지만 repr을 호출하여 사용할 수 있다.
for x in car_list:
    print(x)


