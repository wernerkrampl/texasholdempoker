from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Two_pairs(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 2
        self.pairs = []
        self.kicker = None
        for key in range(14, 1, -1):
            if len(self.hand_table[key]) == 2:
                self.pairs.append(self.hand_table[key])
            elif len(self.hand_table[key]) == 1:
                self.kicker = self.hand_table[key][0]
                break #so it won't uselessly run
        return

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.pairs[0][0].rank == other.pairs[0][0].rank and self.pairs[1][0].rank == other.pairs[1][0].rank:
            if self.kicker.rank == other.kicker.rank:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.pairs[0][0].rank < other.pairs[0][0].rank:
            return True
        elif self.pairs[0][0].rank > other.pairs[0][0].rank:
            return False
        elif self.pairs[1][0].rank < other.pairs[1][0].rank:
            return True
        elif self.pairs[1][0].rank > other.pairs[1][0].rank:
            return False
        else:
            if self.kicker.rank < other.kicker.rank:
                return True
            else:
                return False
