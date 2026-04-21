import random
from queue import Queue

class Round:
    def __init__(self, players, dealer):

class Round:
    def __init__(self,players,deck,dealer,half_blind):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.pots = [] #TODO: Change to object of Pots class. Add first pot with correct position of players.
        self.actual_bet = 0
        self.half_blind = half_blind # Same comment as for self.pot
        self.community_cards = None
        self.game_state = {} #TODO: Add correct game state

    def add_bet(self,bets, player, bet):
        if player not in bets:
            bets[player] = bet
        else:
            bets[player] += bet
        return bets

    def isLegal(self):
        """
        TODO: Finish this first.
        :return:
        """
        pass

    def betting(self):
        """
        TODO: This is in the middle of refactor to actions dictionary
        :return:
        """
        pot = self.pots[-1]
        last_raise = -1
        actions = {}
        bet_occured = False
        players_to_play_queue = Queue()
        players_played_queue = Queue()
        for player in pot.players:
            if not player.folded:
                players_to_play_queue.put(player)
                actions[player] = []

        while not players_to_play_queue.empty():
            player = players_to_play_queue.get()
            action = player.action()
            #call,raise, fold, all in
            if action[0] == 'Check':
                if bet_occured:
                    while action[0] == 'Check':
                        action = player.action(self.minimal_bet)
                else:
                    players_played_queue.put(player)
                    actions[player].append(action)

            elif action[0] == 'Bet':
                while action[1] > player.credit:
                    action = player.action(self.minimal_bet)
                if
                bet_occured = True
                while not players_played_queue.empty():
                    players_to_play_queue.put(players_played_queue.get())
                players_played_queue.put(player)
                actions[player].append(action)

            elif action[0] == 'Call':







    def betting(self):
        pot = self.pots[-1]
        players = pot.players
        end_of_cycle = 0 #either player who last raised or, if nobody raised, it's the first player to make action
        still_betting = True
        while still_betting:
            if not self.players[player_number].folded:
                action = self.players[player_number].action(self.minimal_bet)
                if action[0] == 'Call':
                    pot.value += action[1]
                    print() # TODO: Finish the print
                elif action[0] == 'Raise':
                    pot.value += action[1]
                    self.actual_bet = action[2]
                    end_of_cycle = player_number
                    print()  # TODO: Finish the print
                elif action[0] == 'Fold':
                    print() #TODO: Finish the print
                elif action[0] == 'Check':
                    print() #TODO: Finish the print
                elif action[0] == 'All in':
                    pot.value += action[1]
                    self.actual_bet = action[2]

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
        self.betting(player_number)

        # 3. Flop,  4. Turn, 5. River

        for stage in ['Flop', 'Turn', 'River']:
            if stage == 'Flop':
                self.community_cards = [self.deck.pop() for i in range(3)]
            else:
                self.community_cards.append(self.deck.pop())
            self.betting()

        # 6. Showdown

