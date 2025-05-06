from card import Card, Rank

class Player:
    def __init__(self):
        self.hand = []  # List of cards
        self.score = 0  # Current score

    def add_card(self, card: Card):
        """Adds a card to the player's hand and updates the score."""
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        """Calculates the score of the player's hand."""
        score = 0
        ace_count = 0

        for card in self.hand:
            if card.rank == Rank.ACE:
                ace_count += 1
                score += 11
            elif card.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
                score += 10
            else:
                score += int(card.rank.value)

        # Adjust for Aces
        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1

        self.score = score

    def is_busted(self):
        """Checks if the player has busted (score over 21)."""
        return self.score > 21

    def __str__(self):
        """Displays the player's hand as a string."""
        return ', '.join(str(card) for card in self.hand)
