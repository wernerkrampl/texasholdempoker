from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Two_pairs(Hand_values):
    def __init__(self, hand_table, pairs, kicker):
        super().__init__(hand_table)
        self.value = 2
        self.pairs = pairs
        self.kicker = kicker
        return

    @classmethod
    def check_and_create(cls, hand_table):
        pairs = []
        kicker = None
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 2:
                pairs.append(hand_table[key])
            elif len(hand_table[key]) == 1:
                kicker = hand_table[key][0]
                break  # so it won't uselessly run
        if not kicker is None:
            return cls(hand_table, pairs, kicker)
        else:
            return None

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
