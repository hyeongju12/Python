'''
 파이썬에서 프로그래머의 실수를 막을 수 있는 방법을 제공해 주는데
 아래와 같다.

 1. 숨기려하는 멤버(변수) 앞에 언더바 두개 붙이기
    언더바 2개를 멤버 앞에 붙이면 객체가 만들어 질때 멤버명이 변경된다
    _클래스명__멤버명, 또한 __dict__을 통해서 변경이 가능하다.
 2. 프로퍼티 기법
'''

# 언더바 두개 이용
class Account:
    def __init__(self, name, money):
        self.user = name
        self.balance = money

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, money):
        if money < 0:
            return
        self._balance = money

if __name__=="__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000

    print(my_acnt.get_balance())
    # __balance라는 멤버를 하나 더가지게 된다.