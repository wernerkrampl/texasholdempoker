from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Full_house(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 6
        self.three = None
        self.pair = None
        for key in range(14, 1, -1):
            if len(self.hand_table[key]) == 3:
                self.three = self.hand_table[key]
            elif len(self.hand_table[key]) == 2:
                self.pair = self.hand_table[key]
        return

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.three[0].rank == other.three[0].rank and self.pair[0].rank == other.pair[0].rank:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.three[0].rank < other.three[0].rank:
            return True
        elif self.three[0].rank > other.three[0].rank:
            return False
        else:
            if self.pair[0].rank < other.pair[0].rank:
                return True
            else:
                return False