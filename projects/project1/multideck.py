import random
from card import Card, Suit, Rank

class MultiDeck:
    def __init__(self, num_decks=2):
        self.num_decks = num_decks
        self.deck = []
        self._initialize_deck()

    def _initialize_deck(self):
        """Creates multiple decks and shuffles them together."""
        ranks = [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]
        suits = [Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS, Suit.SPADES]
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits] * self.num_decks
        random.shuffle(self.deck)

    def draw_card(self):
        """Draw a card from the deck."""
        if len(self.deck) == 0:
            self._initialize_deck()  # Reshuffle if the deck is empty
        return self.deck.pop()
