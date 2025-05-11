import random

from src.hand_table import Hand_table
from src.hand_values import Royal_flush, Hand_values


class Round:
    def __init__(self,players,deck,dealer,blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pot = 0 # This could be created later after the Setup stage, but I wanted to make it more clear here
        self.minimal_bet = blind # Same comment as for self.pot
        self.community_cards = None

    def check_royal_flush(self, cards):
        hand_table = Hand_table(cards)
        if not len(hand_table.table['10']) == len(hand_table.table['Jack']) == len(hand_table.table['Queen']) == \
                len(hand_table.table['King']) == len(hand_table.table['Ace']) == 1:
            return False
        if hand_table.table['10'][0].rank == hand_table.table['Jack'][0].rank == hand_table.table['Queen'][0].rank == \
            hand_table.table['King'][0].rank == hand_table.table['Ace'][0].rank:
            return True
        else:
            return False



    def check_hand(self, cards):
        on_hand = []

        # High card
        # Pair
        # Two pairs
        # Three of a kind
        # Straight
        # Flush
        # Full house
        # Four of a kind
        # Straight flush
        # 9: Royal flush
        royal_flush = self.check_royal_flush(cards)
        if royal_flush:
            on_hand.append(9)
        return

    def betting(self):
        for i in range(len(self.players)):
            player_number = (self.dealer + i + 3) % len(self.players)
            bet, self.minimal_bet = self.players[player_number].place_bet(self.minimal_bet)
            self.pot += bet

    def proceed(self):
        # TODO: Finish
        # 1. Setup
        stage = 'Setup'
        bet, self.minimal_bet = self.players[self.small_blind].place_bet(self.minimal_bet)
        self.pot += bet
        self.minimal_bet *= 2
        bet, self.minimal_bet = self.players[self.big_blind].place_bet(self.minimal_bet)
        self.pot += bet

        # 2. Pre-Flop
        stage = 'Pre-Flop'
        random.shuffle(self.deck) # Shuffling the deck
        for i in range(len(self.players)): # Dealing the cards
            player_number = (self.dealer + i + 1) % len(self.players)
            hole_cards = (self.deck.pop(),self.deck.pop())
            self.players[player_number].hole_cards = hole_cards

        ## First round of betting
        self.betting()

        # 3. Flop,  4. Turn, 5. River

        for stage in ['Flop', 'Turn', 'River']:
            if stage == 'Flop':
                self.community_cards = [self.deck.pop() for i in range(3)]
            else:
                self.community_cards.append(self.deck.pop())
            self.betting()

        # 6. Showdown

