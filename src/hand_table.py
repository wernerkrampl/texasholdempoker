from src.hand_values import Hand_values


class Hand_table:
    def __init__(self,cards):
        self.table = {key:[] for key in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']}
        for card in cards:
            self.table[card.rank].append(card)
        return