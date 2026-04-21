from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Three_of_a_kind(Hand_values):
    def __init__(self, hand_table, three, sorted_kickers):
        super().__init__(hand_table)
        self.value = 3
        self.three = three
        self.sorted_kickers = sorted_kickers
        return

    @classmethod
    def check_and_create(cls, hand_table):
        three = None
        sorted_kickers = []
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 3:
                three = hand_table[key]
            elif len(hand_table[key]) > 0:
                sorted_kickers += hand_table[key]
        if not three is None:
            return cls(hand_table, three, sorted_kickers)
        else:
            return None

    def __eq__(self, other):
        if not isinstance(other, Three_of_a_kind):
            return False
        if self.three[0].rank == other.three[0].rank:
            for i in range(2):
                if self.sorted_kickers[i].rank == other.sorted_kickers[i].rank:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Three_of_a_kind):
            return False
        if self.three[0].rank < other.three[0].rank:
            return True
        elif self.three[0].rank > other.three[0].rank:
            return False
        else:
            for i in range(2):
                if self.sorted_kickers[i].rank < other.sorted_kickers[i].rank:
                    return True
                elif self.sorted_kickers[i].rank > other.sorted_kickers[i].rank:
                    return False
                else:
                    continue
        return False  # In case they are equal
