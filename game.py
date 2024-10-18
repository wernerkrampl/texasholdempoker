class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def __str__(self):
        return f'{self.suit[0]}{self.rank[0]}'

class Hand_values:
    def __init__(self):
        pass

    def check_hand(self, hand):
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

    def high_card(self,hand):


class Game:
    def __init__(self):

        # Suits and rank declaration
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9','Jack', 'Queen', 'King','Ace']

        self.deck = []

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

        # Hand values declaration



if __name__ == '__main__':
    game = Game()
    game.print()
