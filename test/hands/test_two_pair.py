import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.two_pairs import Two_pairs


class TestTwo_pair(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Two_pairs(Hand_table_generator.generate_hand_table([Card('Clubs',13),\
                            Card('Diamonds',13),\
                            Card('Hearts',12),\
                            Card('Spades',12),\
                            Card('Hearts',2)]))

        self.hand_2 = Two_pairs(Hand_table_generator.generate_hand_table([Card('Clubs', 3),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 11),\
                            Card('Spades', 7),\
                            Card('Hearts', 7)]))

        self.hand_3 = Two_pairs(Hand_table_generator.generate_hand_table([Card('Spades',13), \
                            Card('Hearts', 13), \
                            Card('Diamonds', 12), \
                            Card('Clubs', 12), \
                            Card('Spades', 2)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
