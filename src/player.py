from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self):
        self.credit = None
        self.hole_cards = None
        self.bet = None
        self.all_in_amount = 0
        self.actions = []
        self.folded = False

    def can_bet_that_amount(self, bet_amount):
        if bet_amount <= self.credit:
            return True
        else:
            return False

    def place_bet(self, bet_amount):
        pass

    def action(self, allowed_actions):

        # Returns either of:
        # ('Call')
        #('Raise',bet)
        #('Fold')
        #('All in',bet)
        #('Check')

        pass

    def clear_actions(self):
        self.actions = []
        return