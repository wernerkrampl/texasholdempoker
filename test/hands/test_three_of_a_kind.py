import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.three_of_a_kind import Three_of_a_kind


class TestThree_of_a_kind(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Three_of_a_kind(Hand_table_generator.generate_hand_table([Card('Spades',13),\
                            Card('Diamonds',13),\
                            Card('Hearts',13),\
                            Card('Spades',12),\
                            Card('Hearts',2)]))

        self.hand_2 = Three_of_a_kind(Hand_table_generator.generate_hand_table([Card('Clubs', 11),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 11),\
                            Card('Clubs', 13),\
                            Card('Hearts', 10)]))

        self.hand_3 = Three_of_a_kind(Hand_table_generator.generate_hand_table([Card('Spades',13), \
                            Card('Diamonds', 13), \
                            Card('Clubs', 13), \
                            Card('Hearts', 12), \
                            Card('Spades', 2)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
