import matplotlib.pyplot as plt
from random import shuffle, randint

from engine import Auction
from players import DummyBidder, RiskyBidder

TRIALS = 100
START_BALANCE = 10e6

players = [
    {
        'strategy': DummyBidder,
        'name': 'kostas'
    },
    {
        'strategy': DummyBidder,
        'name': 'takis'
    }
]
players = [player['strategy'](player['name'], START_BALANCE) for player in players]

def get_random_auction_opts():
    rounds = randint (10, 1000)
    start_price = randint(50, 10000)
    round_fee = randint(10, 200)

    print("start_price: {}, round_fee: {}, rounds: {}".format(start_price, round_fee, rounds))

    return rounds,  start_price, round_fee

def main():
    winners = {}

    for _ in range(TRIALS):
        rounds, start_price, round_fee = get_random_auction_opts()
        [player.set_auction_info(rounds, start_price, round_fee) for player in players]

        shuffle(players)

        auction = Auction(start_price, 5, round_fee, players.copy())
        winner = auction.run()

        winners[winner] = winners[winner] + 1 if winner in winners else 1

    plt.bar(list(winners.keys()), list(winners.values()))
    plt.show()

main()
