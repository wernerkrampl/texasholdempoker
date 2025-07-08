from functools import total_ordering

from src.hands.hand_values import Hand_values

@total_ordering
class Pair(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 1
        return

    def __eq__(self, other):
        if isinstance(other, Hand_values):
            return self.cards_ordered_by_rank[0].value == other.cards_ordered_by_rank[0].value
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Hand_values):
            return self.cards_ordered_by_rank[0].value < other.cards_ordered_by_rank[0].value
        else:
            return False