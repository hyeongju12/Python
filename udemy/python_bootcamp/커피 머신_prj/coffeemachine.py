def init_person(name, money):
	obj = {'name':name, 'money':money}
	obj['give_money'] = Person[1]
	obj['receive_money'] = Person[2]
	obj['show_info'] = Person[3]
	return obj

def give_money(self, other, money):
    self['money'] -= money
    other['receive_money'](other, money)
    
def receive_money(self, money):
    self['money'] += money
    
def show_info(self):
    print(f"{self['name']}, {self['money']}")
    

Person = init_person, give_money, receive_money, show_info

if __name__ == '__main__':
    j = Person[0]('john', 10000)
    m = Person[0]('mark', 6000)
    
    j['show_info'](j)
    m['show_info'](m)
    
    print('')
    
    j['give_money'](j, m, 3000)
    
    j['show_info']
    m['show_info']
    
    
    
    