from hand import Hand
from deck import Deck
from lesson9.dealer import Dealer
from player import Player


class Game:
    MINIMUM_BET = 1

    def __init__(self, player: Player, dealer: Dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        print(f"You are starting with ${self.player.balance}.")

        while self.player.balance >= Game.MINIMUM_BET:
            play_hand = input("Would you like to play a hand? (yes/no): ").lower()

            if play_hand != 'yes':
                break

            self.deck.create_deck()
            self.deck.shuffle()

            self.bet = self.get_bet()

            self.player.hand = Hand()
            self.dealer.hand = Hand()

            self.deal_initial_cards()

            if self.check_natural_blackjack():
                continue

            self.player_turn()
            if self.player.hand.get_value() > 21:
                self.lose_hand()
                continue

            self.dealer_turn()
            self.determine_winner()

        print("Your game has ended. Please restart this program to try again. Goodbye.")

    def get_bet(self):
        while True:
            try:
                bet = float(input(f"Place your bet (${Game.MINIMUM_BET} - ${self.player.balance}): "))
                if bet < Game.MINIMUM_BET or bet > self.player.balance:
                    raise ValueError()
                return bet
            except ValueError:
                print(f"The bet must be between ${Game.MINIMUM_BET} and ${self.player.balance}.")

    def deal_initial_cards(self):
        self.player.hand.add_to_hand(self.deck.deal(2))
        self.dealer.hand.add_to_hand(self.deck.deal(2))

        print(f"You are dealt: {self.player.get_str_hand()}")
        print(f"The dealer is dealt: {self.dealer.get_str_hand()}")

    def check_natural_blackjack(self):
        if self.player.hand.get_value() == 21 and self.dealer.hand.get_value() != 21:
            self.win_blackjack()
            return True
        elif self.dealer.hand.get_value() == 21 and self.player.hand.get_value() != 21:
            self.lose_hand()
            return True
        elif self.player.hand.get_value() == 21 and self.dealer.hand.get_value() == 21:
            self.tie()
            return True
        return False

    def player_turn(self):
        while True:
            action = input("Would you like to hit or stay? ").lower()
            if action == 'hit':
                self.player.hand.add_to_hand(self.deck.deal(1))
                print(f"You are dealt: {self.player.get_str_hand()}")
                if self.player.hand.get_value() > 21:
                    break
            elif action == 'stay':
                break
            else:
                print("That is not a valid option.")

    def dealer_turn(self):
        print(f"The dealer has: {self.dealer.get_str_hand(show_first_card=False)}")
        while self.dealer.hit(self.deck):
            print(f"The dealer hits and is dealt: {self.dealer.hand.cards[-1]}")
            if self.dealer.hand.get_value() > 21:
                break

    def determine_winner(self):
        if self.dealer.hand.get_value() > 21:
            self.win_hand()
        elif self.player.hand.get_value() > self.dealer.hand.get_value():
            self.win_hand()
        elif self.player.hand.get_value() < self.dealer.hand.get_value():
            self.lose_hand()
        else:
            self.tie()

    def win_blackjack(self):
        winnings = self.bet + self.bet * 1.5
        self.player.balance += winnings
        print(f"Blackjack! You win ${winnings:.2f} :)")
        print(f"You are starting with ${self.player.balance}.")

    def win_hand(self):
        winnings = self.bet * 2
        self.player.balance += winnings
        print(f"You win ${winnings:.2f}!")
        print(f"You are starting with ${self.player.balance}.")

    def lose_hand(self):
        self.player.balance -= self.bet
        print(f"Your hand value is over 21. Or your value is less than dealer has. You lose ${self.bet:.2f} :(")
        print(f"You are starting with ${self.player.balance}.")

    def tie(self):
        self.player.balance += self.bet
        print("You tie. Your bet has been returned.")
        print(f"You are starting with ${self.player.balance}.")