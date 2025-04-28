from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self):
        self.credit = None
        self.hole_cards = None

    def can_bet_that_amount(self, bet_amount):
        if bet_amount <= self.credit:
            return True
        else:
            return False

    def place_bet(self, bet_amount):
        pass
