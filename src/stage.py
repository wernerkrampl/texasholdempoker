from abc import ABC, abstractmethod

class Stage(ABC):
    def __init__(self, players, deck, dealer, pot, minimal_bet):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pot = pot
        self.minimal_bet = minimal_bet
        return

    @abstractmethod
    def proceed(self):
        pass

    def __str__(self): #TODO: Finish
        pass

class Setup(Stage):
    def __init__(self, players, deck, dealer, pot, minimal_bet):
        Stage.__init__(self, players, deck, dealer, pot, minimal_bet)
        self.small_blind = (dealer + 1) % len(self.players)
        self.big_blind = (dealer + 2) % len(self.players)
        return


    def proceed(self):
        self.pot, self.minimal_bet = self.players[self.small_blind].bet(minimal_bet)
        self.minimal_bet *= 2
        self.pot, self.minimal_bet = self.players[self.big_blind].bet(minimal_bet)
        print(self)
        return
