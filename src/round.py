import random

class Round:
    def __init__(self,players,deck,dealer,half_blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pot = 0 # This could be created later after the Setup stage, but I wanted to make it more clear here
        self.half_blind = half_blind # Same comment as for self.pot
        self.community_cards = None

    def betting(self):
        for i in range(len(self.players)):
            player_number = (self.dealer + i + 3) % len(self.players)
            action = self.players[player_number].action(self.minimal_bet)
            #TODO Finish action
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

