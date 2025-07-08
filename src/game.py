from src.card import Card

class Game:

    def __init__(self, mode, players, names):
        # Create players
        self.players = self.add_players(players, names)

        # Suits and rank declaration
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = [i for i in range(2,15)]

        # Create deck of cards
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

        return

    def add_players(self, players, names): #TODO
        pass





