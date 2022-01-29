class Account:
    num_anct = 0

    @classmethod
    def get_num_acnt(cls):
        return cls.num_anct

    def __init__(self, name, money):
        self.name = name
        self.balance = money
        Account.num_anct += 1

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None
    def transfer(self, other, money):
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False


    def __str__(self):
        return 'user : {}, balance : {}'.format(self.name, self.balance)


    def __docs__(self):
        return "test"

if __name__ == "__main__":
    #객체 생성
    my_anct = Account("greg", 5000)
    your_anct = Account("john", 1000)

    print('object created')
    print(my_anct)
    print(your_anct)

    print()

    # 인스턴스 메서드 호출
    my_anct.deposit(5000)

    print('deposit')
    print(my_anct)
    print()

    print('withdraw')
    money = my_anct.withdraw(1500)

    if money:
        print('withdraw money : {}'.format(money))
    else:
        print('Not enough money')
    print()

    print('class member')

    print('Account.num_acnt')

    print()


    print('classMethod')
    n_acnt = Account.get_num_acnt()

    print('The number of accounts : {}'.format(n_acnt))

    # 메세지 패싱
    print('message passing')
    print(my_anct)
    print(your_anct)
    res = my_anct.transfer(your_anct, 1500)
    if res:
        print("transfer succeed")
    else:
        print("transfer failed")

    print(my_anct)
    print(your_anct)