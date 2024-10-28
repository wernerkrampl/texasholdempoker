class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def __str__(self):
        return f'{self.suit[0]}{self.rank[0]}'