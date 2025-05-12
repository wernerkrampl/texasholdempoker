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

    def check_royal_flush(self, table):
        if not len(table['10']) == len(table['Jack']) == len(table['Queen']) == \
                len(table['King']) == len(table['Ace']) == 1:
            return (False, None)
        if table['10'][0].rank == table['Jack'][0].rank == table['Queen'][0].rank == \
            table['King'][0].rank == table['Ace'][0].rank:
            return (True, None)
        else:
            return (False, None)

    def check_straight_flush(self, table):
        flush_counter = 0
        possible_flush_suit = None
        for card in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            if len(table[card]) == 1 and possible_flush_suit == None:
                flush_counter += 1
                possible_flush_suit = table[card][0].suit
            elif len(table[card]) == 1 and possible_flush_suit == table[card][0].suit:
                flush_counter += 1
            else:
                flush_counter = 0
            if flush_counter == 5:
                return (True, card)
        return (False, None)

    def check_hand(self, cards):
        on_hand = []
        table = {key: [] for key in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']}
        for card in cards:
            table[card.rank].append(card)

        # High card
        # Pair
        # Two pairs
        # Three of a kind
        # Straight
        # Flush
        # Full house
        # Four of a kind

        # 8: Straight flush
        straight_flush, highest_card = self.check_straight_flush(table)
        if straight_flush:
            on_hand.append((8,highest_card))

        # 9: Royal flush
        royal_flush, highest_card = self.check_royal_flush(table)
        if royal_flush:
            on_hand.append((9,highest_card))
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

