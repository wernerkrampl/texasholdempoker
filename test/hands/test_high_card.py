import unittest

from src.card import Card
from src.hands.hand_table_generator import Hand_table_generator
from src.hands.high_card import High_card


class TestHigh_card(unittest.TestCase):
    def setUp(self):
        self.hand_1 = High_card.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs',2),\
                            Card('Diamonds',14),\
                            Card('Hearts',5),\
                            Card('Spades',12),\
                            Card('Hearts',10)]))

        self.hand_2 = High_card.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs', 3),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 4),\
                            Card('Spades', 13),\
                            Card('Hearts', 10)]))

        self.hand_3 = High_card.check_and_create(Hand_table_generator.generate_hand_table([Card('Diamonds', 2), \
                            Card('Clubs', 14), \
                            Card('Spades', 5), \
                            Card('Hearts', 12), \
                            Card('Spades', 10)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
