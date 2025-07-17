import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.full_house import Full_house

class TestFull_house(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Full_house(Hand_table_generator.generate_hand_table([Card('Spades',13),\
                            Card('Diamonds',13),\
                            Card('Hearts',13),\
                            Card('Spades',12),\
                            Card('Spades',12)]))

        self.hand_2 = Full_house(Hand_table_generator.generate_hand_table([Card('Clubs', 11),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 11),\
                            Card('Clubs', 13),\
                            Card('Hearts', 13)]))

        self.hand_3 = Full_house(Hand_table_generator.generate_hand_table([Card('Hearts',13), \
                            Card('Spades', 13), \
                            Card('Clubs', 13), \
                            Card('Hearts', 12), \
                            Card('Spades', 12)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
