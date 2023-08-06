import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards = [Card(suit, value) for suit in Card.SUIT_SYMBOLS.values() for value in Card.VALUE_NAMES.values()]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]
    
d = Deck()
d.create_deck()
print(len(d.cards))