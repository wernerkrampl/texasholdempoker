from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Royal_flush(Hand_values):
    def __init__(self, hand_table):
        super().__init__(hand_table)
        self.value = 9
        return

    @classmethod
    def check_and_create(cls, hand_table):
        if len(hand_table[14]) == 1 and len(hand_table[13]) == 1 and \
                len(hand_table[12]) == 1 and len(hand_table[11]) == 1 and len(hand_table[10]) == 1:
            if hand_table[14][0].suit == hand_table[13][0].suit == hand_table[12][0].suit == \
                    hand_table[11][0].suit == hand_table[10][0].suit:
                return cls(hand_table)
            else:
                return None

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        return False