class Round:
    def __init__(self,players,deck,dealer,blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.blind = blind
        self.pot = 0 # This could be created later after the Setup stage, but I wanted to make it more clear here
        self.minimal_bet = blind # Same comment as for self.pot

    def proceed(self):
        self.stage = Setup() #TODO: Finish
