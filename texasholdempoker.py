import src.game as game
import argparse

parser = argparse.ArgumentParser(description = "Texas Hold'em Poker")
parser.add_argument('-m', '--mode', choices = ['normal', 'master', 'god'],  help=
                    'Mode of the game. Available options: "normal", "master", "god". Default is "normal',
                    default = 'normal')
parser.add_argument('-p', '--players', type = str, default = 'human,random_ai',
                    help = 'Comma-separated list of players for this game. Available options are human, random_ai.'
                            'Switch --names can be used to set names for each player, otherwise numbers will be used.')
parser.add_argument('-n', '--names', type = str, help = 'Comma-separated list of names of players. ')


if __name__ == '__main__':
    args = parser.parse_args()
    game = game.Game(args.mode, args.players, args.names)