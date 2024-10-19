class Hand_values(ABC):
    def __init__(self, cards):
        self.cards = cards
        self.value = None
        return

    @property
    def value(self):
        return self.value

class High_card(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 0
        return

class Pair(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 1
        return

class Two_pairs(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 2
        return

class Three_of_a_kind(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 3
        return

class Straight(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 4
        return

class Flush(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 5
        return

class Full_house(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 6
        return

class Four_of_a_kind(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 7
        return

class Straight_flush(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 8
        return

class Royal_flush(Hand_values):
    def __init__(self):
        super().__init__(self.cards)
        self.value = 9
        return
