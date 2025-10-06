import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.pair import Pair


class TestPair(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Pair.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs',13),\
                            Card('Diamonds',13),\
                            Card('Hearts',5),\
                            Card('Spades',12),\
                            Card('Hearts',2)]))

        self.hand_2 = Pair.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs', 3),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 11),\
                            Card('Spades', 13),\
                            Card('Hearts', 10)]))

        self.hand_3 = Pair.check_and_create(Hand_table_generator.generate_hand_table([Card('Spades',13), \
                            Card('Hearts', 13), \
                            Card('Diamonds', 5), \
                            Card('Hearts', 12), \
                            Card('Spades', 2)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
