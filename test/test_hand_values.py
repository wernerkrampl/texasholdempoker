import unittest
from src.hands.hand_values import High_card, Pair, Two_pairs, Three_of_a_kind, Straight, Flush, Full_house, Four_of_a_kind, \
    Straight_flush, Royal_flush


class TestHand_values(unittest.TestCase):
    def setUp(self):
        self.high_card = High_card(None)
        self.pair = Pair(None)
        self.two_pairs = Two_pairs(None)
        self.three_of_a_kind = Three_of_a_kind(None)
        self.straight = Straight(None)
        self.flush = Flush(None)
        self.full_house = Full_house(None)
        self.four_of_a_kind = Four_of_a_kind(None)
        self.straight_flush = Straight_flush(None)
        self.royal_flush = Royal_flush(None)
        self.list_hand_values = [self.high_card, self.pair, self.two_pairs, self.three_of_a_kind,self.straight,
                                 self.flush, self.full_house, self.four_of_a_kind,self.straight_flush, self.royal_flush]
    def test_compare_hand_values(self):
        for i in range(len(self.list_hand_values)):
            for j in range(i, len(self.list_hand_values)):
                self.assertLessEqual(self.list_hand_values[i],self.list_hand_values[j])

    def test_string_conversion(self):
        assert str(self.high_card) == 'High card'
        assert str(self.pair) == 'Pair'
        assert str(self.two_pairs) == 'Two pairs'
        assert str(self.three_of_a_kind) == 'Three of a kind'
        assert str(self.straight) == 'Straight'
        assert str(self.flush) == 'Flush'
        assert str(self.full_house) == 'Full house'
        assert str(self.four_of_a_kind) == 'Four of a kind'
        assert str(self.straight_flush) == 'Straight flush'
        assert str(self.royal_flush) == 'Royal flush'

