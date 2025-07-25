from src.hands.hand_values import Hand_values
from functools import total_ordering

@total_ordering
class High_card(Hand_values):
    def __init__(self, hand_table):
        super().__init__(hand_table)
        self.value = 0
        self.sorted_cards = []
        for key in range(14, 1, -1):
            if len(hand_table[key]) > 0:
                self.sorted_cards += hand_table[key]
        return

    def __eq__(self, other):
        if isinstance(other, Hand_values):
            return False
        for i in range(5):
            if self.sorted_cards[i].rank == other.sorted_cards[i].rank:
                continue
            else:
                return False
        return True


    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        for i in range(5):
            if self.sorted_cards[i].rank < other.sorted_cards[i].rank:
                return True
            elif self.sorted_cards[i].rank > other.sorted_cards[i].rank:
                return False
            else:
                continue
        return False #In case they are equal