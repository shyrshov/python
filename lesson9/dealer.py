from hand import Hand


class Dealer():
    def __init__(self):
        self.hand = Hand()

    def get_str_hand(self, show_first_card=True):
        if show_first_card:
            return str(self.hand.cards[0]) + ", Unknown"
        else:
            return str(self.hand)

    def hit(self, deck):
        if self.hand.get_value() < 17:
            self.hand.add_to_hand(deck.deal(1))
            return True
        return False