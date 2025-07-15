from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Three_of_a_kind(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 3
        self.three = None
        self.sorted_kickers = []
        for key in range(14, 1, -1):
            if len(self.hand_table[key]) == 3:
                self.three = self.hand_table[key]
            elif len(self.hand_table[key]) > 0:
                self.sorted_kickers += self.hand_table[key]
        return

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
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
        if not isinstance(other, Hand_values):
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
