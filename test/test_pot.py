import unittest
from src.pot import Pot


class TestPot(unittest.TestCase):
    def setUp(self):
        self.pot = Pot([None, None, None, None])
        self.pot.value += 1

    def test_init(self):
        self.assertEqual(len(self.pot.players) ,4)
        self.assertEqual(self.pot.value,1)