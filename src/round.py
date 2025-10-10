import random

class Round:
    def __init__(self,players,deck,dealer,half_blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pot = 0 # This could be created later after the Setup stage, but I wanted to make it more clear here
        self.actual_bet = 0
        self.half_blind = half_blind # Same comment as for self.pot
        self.community_cards = None

    def betting(self):
        player_number = (self.dealer + 3) % len(self.players)
        still_betting = True
        end_of_cycle = player_number #either player who last raised or, if nobody raised, it's the first player to make action
        while still_betting:
            if not self.players[player_number].folded:
                action = self.players[player_number].action(self.minimal_bet)
                if action[0] == 'Call':
                    self.pot += action[1]
                    print() # TODO: Finish the print
                elif action[0] == 'Raise':
                    self.pot += action[1]
                    self.actual_bet = action[2]
                    end_of_cycle = player_number
                    print()  # TODO: Finish the print
                elif action[0] == 'Fold':
                    print() #TODO: Finish the print
                elif action[0] == 'All in':
                    self.pot += action[1]
                    self.actual_bet = action[2]
                elif action[0] == 'Check':
                    print() #TODO: Finish the print

            player_number = (player_number) + 1 % len(self.players)
            if player_number == end_of_cycle:
                still_betting = False
            #TODO Finish action


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

