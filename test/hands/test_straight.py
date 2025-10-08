import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.straight import Straight


class TestStraight(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Straight.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs',4),\
                            Card('Diamonds',3),\
                            Card('Hearts',5),\
                            Card('Spades',2),\
                            Card('Hearts',14)]))

        self.hand_2 = Straight.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs', 13),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 10),\
                            Card('Spades', 12),\
                            Card('Hearts', 14)]))

        self.hand_3 = Straight.check_and_create(Hand_table_generator.generate_hand_table([Card('Diamonds', 3), \
                            Card('Clubs', 4), \
                            Card('Hearts', 5), \
                            Card('Hearts', 2), \
                            Card('Spades', 14)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 < self.hand_2
        assert self.hand_2 > self.hand_3
