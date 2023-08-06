class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self):
        value = 0

        for card in self.cards:
            if card.value in ['T', 'J', 'Q', 'K']:
                value += 10
            elif card.value in ['A']:
                value += 11
            else:
                value += int(card.value)

        return value

    def add_to_hand(self, cards):
        self.cards.extend(cards)

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


