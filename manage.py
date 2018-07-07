from argparse import ArgumentParser

from app.data.fred import run as fred
from app.data.iex import symbols, history
from app.data.coinmarketcap import get_capitalization
from app.models.playground import run_play
from app.stats import run_analyze

parser = ArgumentParser(description="BlueBlood management point.")

parser.add_argument('--collect')
parser.add_argument('--play')
parser.add_argument('--analyze')
args = parser.parse_args()

if __name__ == '__main__':
    if args.collect:
        fred()
        #get_capitalization()
        symbols()

    if args.play:
        run_play(args.play)

    if args.analyze:
        run_analyze(args.analyze)