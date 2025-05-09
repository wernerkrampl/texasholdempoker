class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def __str__(self):
        if self.rank == '11':
            return f'{self.suit[0]}{"J"}'
        elif self.rank == '12':
            return f'{self.suit[0]}{"Q"}'
        elif self.rank == '13':
            return f'{self.suit[0]}{"K"}'
        elif self.rank == '14':
            return f'{self.suit[0]}{"A"}'
        else:
            return f'{self.suit[0]}{self.rank}'