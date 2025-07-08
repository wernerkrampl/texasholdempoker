import random

from src.hand_table import Hand_table


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
            return False
        if table['10'][0].rank == table['Jack'][0].rank == table['Queen'][0].rank == \
            table['King'][0].rank == table['Ace'][0].rank:
            return True
        else:
            return False

    def check_straight_flush(self, table):
        flush_counter = 0
        possible_flush_suit = None
        for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            if len(table[rank]) == 1 and possible_flush_suit == None:
                flush_counter += 1
                possible_flush_suit = table[rank][0].suit
            elif len(table[rank]) == 1 and possible_flush_suit == table[rank][0].suit:
                flush_counter += 1
            else:
                flush_counter = 0
            if flush_counter == 5:
                return True
        return False

    def check_four_of_a_kind(self,table):
        for rank in table.keys():
            if len(table[rank]) == 4:
                return True
        return False

    def check_full_house(self,table):
        triplet = False
        pair = False
        for rank in table.keys():
            if len(table[rank]) == 3:
                triplet = True
            if len(table[rank]) == 2:
                pair = True
        return triplet and pair

    def check_straight_flush(self, table):
        flush_counter = 0
        for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            if len(table[rank]) == 1:
                flush_counter += 1
            else:
                flush_counter = 0
            if flush_counter == 5:
                return True
        return False

    def check_three_of_a_kind(self,table):
        for rank in table.keys():
            if len(table[rank]) == 3:
                return True
        return False

    def check_two_pairs(self,table):
        pair_one = False
        pair_two = False
        for rank in table.keys():
            if len(table[rank]) == 2 and not pair_one:
                pair_one = True
            elif len(table[rank]) == 2 and not pair_two:
                pair_two = True
        return pair_one and pair_two

    def check_pair(self,table):
        for rank in table.keys():
            if len(table[rank]) == 2:
                return True
        return False

        # 0: High card
        on_hand.append(0)

        # 1: Pair
        if self.check_pair(table):
            on_hand.append(1)

        # 2: Two pairs
        if self.check_two_pairs(table):
            on_hand.append(2)
        # 3: Three of a kind
        if self.check_three_of_a_kind(table):
            on_hand.append(3)

        # 4: Straight
        if self.check_straight_flush(table):
            on_hand.append(4)

        # 5: Flush
        if cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit:
            on_hand.append(5)

        # 6: Full house
        if self.check_full_house(table):
            on_hand.append(6)
        # 7: Four of a kind
        if self.check_four_of_a_kind(table):
            on_hand.append(7)

        # 8: Straight flush
        if self.check_straight_flush(table):
            on_hand.append(8)

        # 9: Royal flush
        if self.check_royal_flush(table):
            on_hand.append(9)

        return on_hand

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

