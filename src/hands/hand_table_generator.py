from src.hands.hand_values import Hand_values


class Hand_table_generator:
    def generate_hand_table(cards):
        table = {key:[] for key in [i for i in range(2,15)]}
        for card in cards:
            table[card.rank].append(card)
        return table