from abc import ABC, abstractmethod

class Hand_values(ABC):
    def __init__(self, hand_table):
        self.hand_table = hand_table
        return
#   TODO: This needs to be fixed
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
