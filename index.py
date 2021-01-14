import matplotlib.pyplot as plt
from random import shuffle, randint

from engine import Auction
from players import MiddleBidder, AllInBidder, IncreaseBidder

TRIALS = 300
START_BALANCE = 10e6
BIDDERS = [
    {
        'strategy': MiddleBidder,
        'name': 'Soula'
    },
    {
        'strategy': AllInBidder,
        'name': 'Koula'
    },
    {
        'strategy': IncreaseBidder,
        'name': 'Makis'
    }
]

players = {}
for bidder in BIDDERS:
    players[bidder['name']] = bidder['strategy'](bidder['name'], START_BALANCE)

print(players)

def get_random_baseline_amount():
    return randint(50, 10000)

def main():
    winners = {}

    for _ in range(TRIALS):
        baseline_amount = get_random_baseline_amount()

        auction = Auction(baseline_amount, players.copy())
        winner = auction.run()

        winners[winner] = winners[winner] + 1 if winner in winners else 1

    plt.bar(list(winners.keys()), list(winners.values()))
    plt.show()

main()
