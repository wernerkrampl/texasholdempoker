import unittest

from src.card import Card
from src.hands.flush import Flush
from src.hands.hand_table_generator import Hand_table_generator



class TestFlush(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Clubs',13),\
                            Card('Clubs',6),\
                            Card('Clubs',10),\
                            Card('Clubs',4),\
                            Card('Clubs',5)]))

        self.hand_2 = Flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Diamonds', 3),\
                            Card('Diamonds', 12),\
                            Card('Diamonds', 11),\
                            Card('Diamonds', 8),\
                            Card('Diamonds', 2)]))

        self.hand_3 = Flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Spades',13), \
                            Card('Spades', 6), \
                            Card('Spades', 10), \
                            Card('Spades', 4), \
                            Card('Spades', 5)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
