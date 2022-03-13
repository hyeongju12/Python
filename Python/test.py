import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

beer_card = Card(7, 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(choice(deck))

print(deck[:3])
print(deck[12::13])

# __getitem__() 특별 메서드를 구현하여 deck 반복
for card in deck: # doctest : + ELLIPSIS
    print(card)