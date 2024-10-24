from abc import ABC, abstractmethod

class Hand_values(ABC):
    def __init__(self, cards):
        self.cards = cards
        self.value = None
        return
#   FIXME: This needs to be fixed
#
#    @property
#    def value(self):
#        return self.value
#
#    @value.setter
#    def value(self, value):
#        self._value = value

    def __str__(self):
        return self.__class__.__name__.replace('_', ' ')

    def __eq__(self, other):
        if isinstance(other, Hand_values):
            return self.value == other.value
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Hand_values):
            return self.value >= other.value
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Hand_values):
            return self.value > other.value
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Hand_values):
            return self.value <= other.value
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Hand_values):
            return self.value < other.value
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Hand_values):
            return self.value != other.value
        else:
            return False


class High_card(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 0
        return

class Pair(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 1
        return

class Two_pairs(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 2
        return

class Three_of_a_kind(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 3
        return

class Straight(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 4
        return

class Flush(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 5
        return

class Full_house(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 6
        return

class Four_of_a_kind(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 7
        return

class Straight_flush(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 8
        return

class Royal_flush(Hand_values):
    def __init__(self, cards):
        super().__init__(cards)
        self.value = 9
        return
