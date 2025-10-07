from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Full_house(Hand_values):
    def __init__(self, hand_table, three, pair):
        super().__init__(hand_table)
        self.value = 6
        self.three = three
        self.pair = pair
        return

    @classmethod
    def check_and_create(cls, hand_table):
        three = None
        pair = None
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 3:
                three = hand_table[key]
            elif len(hand_table[key]) == 2:
                pair = hand_table[key]
        if not three is None:
            return cls(hand_table, three, pair)
        else:
            return None

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