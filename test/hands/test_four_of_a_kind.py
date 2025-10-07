import unittest

from src.card import Card
from src.hands.four_of_a_kind import Four_of_a_kind
from src.hands.hand_table_generator import Hand_table_generator


class TestFour_of_a_kind(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Four_of_a_kind.check_and_create(Hand_table_generator.generate_hand_table([Card('Spades',13),\
                            Card('Diamonds',13),\
                            Card('Hearts',13),\
                            Card('Clubs',13),\
                            Card('Hearts',8)]))

        self.hand_2 = Four_of_a_kind.check_and_create(Hand_table_generator.generate_hand_table([Card('Clubs', 11),\
                            Card('Diamonds', 11),\
                            Card('Hearts', 11),\
                            Card('Spades', 11),\
                            Card('Hearts', 10)]))

        self.hand_3 = Four_of_a_kind.check_and_create(Hand_table_generator.generate_hand_table([Card('Spades',13), \
                            Card('Diamonds', 13), \
                            Card('Clubs', 13), \
                            Card('Hearts', 13), \
                            Card('Spades', 8)]))

        self.hand_4 = Four_of_a_kind.check_and_create(Hand_table_generator.generate_hand_table([Card('Spades', 13), \
                                                                               Card('Diamonds', 13), \
                                                                               Card('Clubs', 13), \
                                                                               Card('Hearts', 13), \
                                                                               Card('Spades', 9)]))

    def test_ordering(self):
        assert self.hand_1 == self.hand_3
        assert self.hand_1 > self.hand_2
        assert self.hand_2 < self.hand_3
        assert self.hand_4 > self.hand_2