from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Straight_flush(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 8
        self.highest_card = None
        straight_counter = 0
        for key in range(14, 1, -1):
            if len(self.hand_table[key]) == 1:
                straight_counter += 1
            else:
                straight_counter = 0
            if straight_counter > 1 and self.hand_table[key][0].suit != self.hand_table[key + 1][0].suit:
                return
            if (key == 2 and straight_counter == 4 and len(self.hand_table[14]) == 1 and self.hand_table[2][0].suit ==
                    self.hand_table[14][0].suit):  # case for low-ace (bicycle)
                self.highest_card = self.hand_table[5][0]
                return
            if straight_counter == 5:
                self.highest_card = self.hand_table[key + 4][0]
                break
        return

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.highest_card.rank == other.highest_card.rank:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.highest_card.rank < other.highest_card.rank:
            return True
        else:
            return False