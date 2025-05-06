import random
from player import Player
from multideck import MultiDeck

class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        self.deck = None

    def start_new_game(self):
        """Starts a new game by selecting a random number of decks."""
        num_decks = random.choice([2, 4, 6, 8])
        self.deck = MultiDeck(num_decks)
        self.player.hand = []
        self.dealer.hand = []

    def deal_initial_cards(self):
        """Deals two cards each to the player and the dealer."""
        self.player.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())

    def play_round(self):
        """Plays a round of Blackjack."""
        self.start_new_game()
        self.deal_initial_cards()

        print(f"Player's hand: {self.player}")
        print(f"Dealer's hand: {self.dealer.hand[0]} and [hidden]")

        # Player's turn
        while not self.player.is_busted():
            action = input("Do you want to hit or stay? ").lower()
            if action == "hit":
                self.player.add_card(self.deck.draw_card())
                print(f"Player's hand: {self.player}")
            elif action == "stay":
                break

        if self.player.is_busted():
            print("Player busted!")
            return "Dealer wins!"

        # Dealer's turn
        print(f"Dealer's hand: {self.dealer}")
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.draw_card())
            print(f"Dealer's hand: {self.dealer}")

        if self.dealer.is_busted():
            print("Dealer busted!")
            return "Player wins!"

        # Determine the winner
        if self.player.score > self.dealer.score:
            return "Player wins!"
        elif self.player.score < self.dealer.score:
            return "Dealer wins!"
        else:
            return "It's a tie!"
