from hand_values import Three_of_a_kind, Two_pairs

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def __str__(self):
        return f'{self.suit[0]}{self.rank[0]}'

class Game:
    def __init__(self):

        # Suits and rank declaration
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9','Jack', 'Queen', 'King','Ace']

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


if __name__ == '__main__':

    three_of_a_kind = Three_of_a_kind(None)
    two_pairs = Two_pairs(None)

    print(three_of_a_kind)
