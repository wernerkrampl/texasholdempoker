from src.hands.hand_values import Hand_values


class Royal_flush(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 9
        if len(self.hand_table[14]) == 1 and len(self.hand_table[13]) == 1 and \
                len(self.hand_table[12]) == 1 and len(self.hand_table[11]) == 1 and len(self.hand_table[10]) == 1:
            if self.hand_table[14][0].suit == self.hand_table[13][0].suit == self.hand_table[12][0].suit == \
                self.hand_table[11][0].suit == self.hand_table[10][0].suit:
                return
            else:
                return
        return

    def __eq__(self, other):
        if not isinstance(other, Hand_values):
            return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Hand_values):
            return False
        return False