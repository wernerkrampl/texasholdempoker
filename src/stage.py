# NOTE: In the first version, subclasses of Stage abstract class won't be used.
# This class will therefore stay unfinished for some time.

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

    def betting(self):
        for i in range(len(self.players)):
            player_number = (i + 3) % len(self.players)
            bet = self.players[player_number].place_bet(self.minimal_bet)

    def __str__(self): #TODO: Finish
        pass

class Setup(Stage):
    def __init__(self, players, deck, dealer, pot, minimal_bet):
        Stage.__init__(self, players, deck, dealer, pot, minimal_bet)
        self.small_blind = (dealer + 1) % len(self.players)
        self.big_blind = (dealer + 2) % len(self.players)
        return


    def proceed(self):
        self.pot, self.minimal_bet = self.players[self.small_blind].place_bet(self.minimal_bet)
        self.minimal_bet *= 2
        self.pot, self.minimal_bet = self.players[self.big_blind].place_bet(self.minimal_bet)
        print(self)
        return
