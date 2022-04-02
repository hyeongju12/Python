class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def give_money(self, other, money):
        self.money -= money
        other.get_money(money)

    def get_money(self, money):
        self.money += money

    def show(self):
        print(f'{self.name} {self.money}')

if __name__ == '__main__':
    g = Person('John', 5000)
    h = Person('Mark', 6000)

    g.give_money(h, 3000)

    g.show()
    h.show()

    print(dir(g.give_money.__func__))
    print(dir(g.give_money.__self__ is g))