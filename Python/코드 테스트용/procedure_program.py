from openpyxl import load_workbook

def person_init(name, money):
    obj = {'name' : name, 'money' : money}
    obj['give_money'] = Person[1]
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]

    return obj

def give_money(self, other, money):
    self['money'] -= money
    other['get_money'](other, money)

def get_money(self, money):
    self['money'] += money

def show(self):
    print(f'{self["name"]}, {self["money"]}')

Person = person_init, give_money, get_money, show

if __name__ == "__main__":
    g = Person[0]('John', 5000)
    h = Person[0]('Mark', 6000)

    g['show'](g)
    h['show'](h)

    g['give_money'](g, h, 2000)

    g['show'](g)
    h['show'](h)