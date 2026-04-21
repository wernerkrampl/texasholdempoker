from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Flush(Hand_values):
    def __init__(self, hand_table, ordered_flush):
        super().__init__(hand_table)
        self.value = 5
        self.ordered_flush = ordered_flush
        return

    @classmethod
    def check_and_create(cls, hand_table):
        ordered_flush = []
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 1:
                ordered_flush += hand_table[key]
            elif len(hand_table[key]) > 1:
                ordered_flush = None
                return
        if len(set([card.suit for card in ordered_flush])) > 1:
            return None
        else:
            return cls(hand_table, ordered_flush)

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        for i in range(5):
            if self.ordered_flush[i].rank == other.ordered_flush[i].rank:
                continue
            else:
                return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        for i in range(5):
            if self.ordered_flush[i].rank < other.ordered_flush[i].rank:
                return True
            elif self.ordered_flush[i].rank > other.ordered_flush[i].rank:
                return False
            else:
                continue
        return False  # In case they are equal