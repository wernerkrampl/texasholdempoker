import random

class Round:
    def __init__(self,players,deck,dealer,blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pot = 0 # This could be created later after the Setup stage, but I wanted to make it more clear here
        self.minimal_bet = blind # Same comment as for self.pot
        self.community_cards = []

    def betting(self):
        for i in range(len(self.players)):
            player_number = (self.dealer + i + 3) % len(self.players)
            self.pot, self.minimal_bet = self.players[player_number].place_bet(self.minimal_bet)

    def proceed(self):
        # TODO: Finish
        # 1. Setup - TODO: The function minimal_bet should change to post_blind
        self.pot, self.minimal_bet = self.players[self.small_blind].place_bet(self.minimal_bet)
        self.minimal_bet *= 2
        self.pot, self.minimal_bet = self.players[self.big_blind].place_bet(self.minimal_bet)

        # 2. Pre-Flop
        random.shuffle(self.deck) # Shuffling the deck
        for i in range(len(self.players)): # Dealing the cards
            player_number = (self.dealer + i + 1) % len(self.players)
            hole_cards = (self.deck.pop(),self.deck.pop())
            self.players[player_number].hole_cards = hole_cards

        # First round of betting
        self.betting()



        # 3. Flop
        # 4. Turn
        # 5. River
        # 6. Showdown

