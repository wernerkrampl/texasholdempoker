from functools import total_ordering
from src.hands.hand_values import Hand_values

@total_ordering
class Four_of_a_kind(Hand_values):
    def __init__(self, hand_table, four, kicker):
        super().__init__(hand_table)
        self.value = 7
        self.four = four
        self.kicker = kicker
        return

    @classmethod
    def check_and_create(cls, hand_table):
        four = None
        kicker = []
        for key in range(14, 1, -1):
            if len(hand_table[key]) == 4:
                four = hand_table[key]
            elif len(hand_table[key]) == 1:
                kicker = hand_table[key][0]
        if not four is None:
            return cls(hand_table, four, kicker)
        else:
            return None

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.four[0].rank == other.four[0].rank and self.kicker.rank == other.kicker.rank:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        if self.four[0].rank < other.four[0].rank:
            return True
        elif self.four[0].rank > other.four[0].rank:
            return False
        else:
            if self.sorted_kicker.rank < other.sorted_kicker.rank:
                return True
            else:
                return False  # In case they are equal
