from abc import ABC, abstractmethod

class Hand_values(ABC):
    def __init__(self, hand_table):
        self.value = None
        self.hand_table = hand_table
        return

    def __str__(self):
        return self.__class__.__name__.replace('_', ' ')
