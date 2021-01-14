import matplotlib.pyplot as plt
from random import shuffle, randint

from engine import Auction
from players import MiddleBidder, AllInBidder, IncreaseBidder, SameBidder, DoubleUpBidder, DistributeBidder

TRIALS = 100
START_BALANCE = 10e6
BIDDERS = [
    {
        'strategy': MiddleBidder,
        'name': 'Soula'
    },
    {
        'strategy': DoubleUpBidder,
        'name': 'Koula'
    },
    {
        'strategy': DistributeBidder,
        'name': 'Loulis'
    },
    {
        'strategy': IncreaseBidder,
        'name': 'Makis'
    },
    {
        'strategy': SameBidder,
        'name': 'Lakis'
    },
    {
        'strategy': AllInBidder,
        'name': 'Toula'
    },
]

players = {}
for bidder in BIDDERS:
    players[bidder['name']] = bidder['strategy'](bidder['name'], START_BALANCE, TRIALS)

print(players)

def get_random_baseline_amount(prev_baseline_amount):
    return prev_baseline_amount + randint(1, 10000)

def main():
    winners = {}
    baseline_amount = 0

    for _ in range(TRIALS):
        baseline_amount = get_random_baseline_amount(baseline_amount)

        auction = Auction(baseline_amount, players.copy())
        winner = auction.run()
        [player.announce_winner(winner) for player in players.values()]
        winners[winner] = winners[winner] + 1 if winner in winners else 1

    plt.bar(list(winners.keys()), list(winners.values()))
    plt.show()

main()
