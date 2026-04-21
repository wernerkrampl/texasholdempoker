from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Pair(Hand_values):
    def __init__(self, hand_table, pair, sorted_kickers):
        super().__init__(hand_table)
        self.value = 1
        self.pair = pair
        self.sorted_kickers = sorted_kickers
        return

    @classmethod
    def check_and_create(cls, hand_table):
        pair = None
        sorted_kickers = []
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 2:
                pair = hand_table[key]
            elif len(hand_table[key]) > 0:
                sorted_kickers += hand_table[key]
        if not pair is None:
            return cls(hand_table, pair, sorted_kickers)
        else:
            return None

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        if self.pair[0].rank == other.pair[0].rank:
            for i in range(3):
                if self.sorted_kickers[i].rank == other.sorted_kickers[i].rank:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Pair):
            return False
        if self.pair[0].rank < other.pair[0].rank:
            return True
        elif self.pair[0].rank > other.pair[0].rank:
            return False
        else:
            for i in range(3):
                if self.sorted_kickers[i].rank < other.sorted_kickers[i].rank:
                    return True
                elif self.sorted_kickers[i].rank > other.sorted_kickers[i].rank:
                    return False
                else:
                    continue
        return False  # In case they are equal