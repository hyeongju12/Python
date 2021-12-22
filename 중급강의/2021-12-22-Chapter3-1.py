# Chapter3-1
# Special Method(Magic Method)
# 파이썬 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print("called >>  __add__")
        return self._price + x._price

    def __sub__(self, x):
        print("called >>  __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("Called >> __sub__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("Called >> __ge__")
        if self._price >= x._price:
            return True
        else:
            return False

    
# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1+s2)

print(s1 >= s2)
print(s1 <= s2)
