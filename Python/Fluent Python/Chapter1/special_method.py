import collections

'''
collenctions.namedtuple : rank, suit 속성을 가진 클래스를 생성한다. 
'''
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		'''
			_card = suits와 ranks 리스트 컴프리헨션을 이용하여 Card객체를 생성한다.
		'''
		self._card = [Card(rank, suit) for suit in self.suits
					  for rank in self.ranks]

	def __len__(self):
		return len(self._card)

	def __getitem__(self, position):
		return self._card[position]

# rank = 7, suit = diamond인 카드 객체를 beer_card 할당
beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
# __getitem__(특별메서드)가 호출되어 해당 인덱스의 카드 정보를 리턴해준다.
print(deck[0])

from random import choice
print(choice(deck))

# 특별메서드를 사용할때 장점 두가지
# 1. 사용자가 표준 연산을 수행하기 위해 클래스 자체에 구현한 메서드를 암기할 필요가 없다.
# 2. <이건 특별메서드에 관한 장점은 아닌듯> 파이썬 표준 라이브러리에서 제공하는 기능이 풍부하여,
#     프로그래머가 별도로 구현하지 않아도되는 부분이 있다.

# print(deck[:3])
# print(deck[12::13])
#
# for card in deck:
# 	print(card)
#
# for card in reversed(deck): # doctest: + ELLIPSIS
# 	print(card)

# 정렬
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
	print(card)