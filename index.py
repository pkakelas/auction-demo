import matplotlib.pyplot as plt

from engine import Auction
from players import IncreaseBidder, EvenBidder, DrunkBidder, EqualDistributeBidder, ScaleBidder, DoubleUpBidder, DistributeBidder, MartingaleBidder, AllInBidder

TRIALS = 1000
START_BALANCE = 10e6
BIDDERS = [
    {
        'strategy': EqualDistributeBidder,
        'name': 'Soula'
    },
    {
        'strategy': IncreaseBidder,
        'name': 'Valantis'
    },
    {
        'strategy': DrunkBidder,
        'name': 'Voula'
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
        'strategy': ScaleBidder,
        'name': 'Makis'
    },
    {
        'strategy': MartingaleBidder,
        'name': 'Lakis'
    },
    {
        'strategy': AllInBidder,
        'name': 'Toula'
    },
    {
        'strategy': EvenBidder,
        'name': 'Notis'
    },
]

players = {}
for bidder in BIDDERS:
    players[bidder['name']] = bidder['strategy'](bidder['name'], START_BALANCE, TRIALS)

print(players)

def main():
    winners = {}
    baseline_amount = 1000

    for _ in range(TRIALS):
        auction = Auction(baseline_amount, players.copy())
        winner, max_bid = auction.run()
        [player.announce_winner(winner, max_bid) for player in players.values()]
        winners[winner] = winners[winner] + 1 if winner in winners else 1

    plt.bar(list(winners.keys()), list(winners.values()))
    plt.show()

main()
