import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        # Suits and rank declaration
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = [i for i in range(2,15)]
        self.ranks_representation = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = []

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def test_deck_size(self):
        self.assertEqual(len(self.deck),52)

    def test_string_conversion(self):
        for i in range(len(self.suits)):
            for j in range(len(self.ranks)):
                self.assertEqual(f'{self.suits[i][0]}{self.ranks_representation[j][0] 
                if self.ranks_representation[j] != '10' else '10'}', str(self.deck[i * 13 + j]))