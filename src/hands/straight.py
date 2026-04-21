from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Straight(Hand_values):
    def __init__(self, hand_table, highest_card):
        super().__init__(hand_table)
        self.value = 4
        self.highest_card = highest_card
        return

    @classmethod
    def check_and_create(cls, hand_table):
        highest_card = None
        flush_counter = 0
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 1:
                flush_counter += 1
            else:
                flush_counter = 0
            if key == 2 and flush_counter == 4 and len(hand_table[14]) == 1:  # case for low-ace (bicycle)
                highest_card = hand_table[5][0]
                break
            elif flush_counter == 5:
                highest_card = hand_table[key + 4][0]
                break
        if not highest_card is None:
            return cls(hand_table, highest_card)
        else:
            return None

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