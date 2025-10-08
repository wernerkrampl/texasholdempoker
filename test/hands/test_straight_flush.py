import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.straight_flush import Straight_flush


class TestStraight_flush(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Straight_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Clubs',4),\
                            Card('Clubs',3),\
                            Card('Clubs',5),\
                            Card('Clubs',2),\
                            Card('Clubs',14)]))

        self.hand_2 = Straight_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Diamonds', 13),\
                            Card('Diamonds', 11),\
                            Card('Diamonds', 10),\
                            Card('Diamonds', 12),\
                            Card('Diamonds', 14)]))

        self.hand_3 = Straight_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Spades', 3), \
                            Card('Spades', 4), \
                            Card('Spades', 5), \
                            Card('Spades', 2), \
                            Card('Spades', 14)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 < self.hand_2
        assert self.hand_2 > self.hand_3
