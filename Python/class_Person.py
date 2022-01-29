class Person:
    def __init__(self, name, money):
        self.money = money
        self.name = name

    def give_money(self, other, money):
        self.money -= money
        other.get_money(money)

    def get_money(self, money):
        self.money += money

    def show(self):
        print('{} : {}'.format(self.name, self.money))


if __name__ == "__main__":
    g = Person("greg", 3000)
    j = Person("john", 500)

    g.show()
    j.show()

    print()

    g.give_money(j, 2000)

    g.show()
    j.show()

    print(type(Person.__init__))
    print(type(Person.give_money))
    print(type(Person.get_money))
    print(type(Person.show))

    print(type(g.give_money))
    print(type(g.get_money))
    print(type(g.show))

    print(dir(g.give_money))
    print(g.give_money.__func__)
    print(g.give_money.__self__ is g)