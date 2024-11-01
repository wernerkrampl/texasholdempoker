from src.hand_values import Three_of_a_kind, Two_pairs
from src.card import Card

class Game:
    def __init__(self):

        # Suits and rank declaration
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9','10','Jack', 'Queen', 'King','Ace']

        self.deck = []

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def check_hand(self, player, hand):
        # High card
        # Pair
        # Two pairs
        # Three of a kind
        # Straight
        # Flush
        # Full house
        # Four of a kind
        # Straight flush
        # Royal flush
        pass



