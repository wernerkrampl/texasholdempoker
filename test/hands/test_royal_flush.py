import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.royal_flush import Royal_flush


class TestRoyal_flush(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Royal_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Clubs',14),\
                            Card('Clubs',13),\
                            Card('Clubs',11),\
                            Card('Clubs',12),\
                            Card('Clubs',10)]))

        self.hand_2 = Royal_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Diamonds', 13),\
                            Card('Diamonds', 11),\
                            Card('Diamonds', 10),\
                            Card('Diamonds', 12),\
                            Card('Diamonds', 14)]))

        self.hand_3 = Royal_flush.check_and_create(Hand_table_generator.generate_hand_table(\
                            [Card('Spades', 14), \
                            Card('Spades', 13), \
                            Card('Spades', 12), \
                            Card('Spades', 11), \
                            Card('Spades', 10)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 == self.hand_2
        assert self.hand_2 == self.hand_3
