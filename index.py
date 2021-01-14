import matplotlib.pyplot as plt

from engine import Auction
from players import IncreaseBidder, EvenBidder, DrunkBidder, ScaleBidder, DoubleUpBidder, DistributeBidder, MartingaleBidder, AllInBidder

TRIALS = 1000
START_BALANCE = 10e6
BASELINE_AMOUNT = 1000
BIDDERS = [
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



def plot_results(winners):
    winner_freq = {}
    for name in winners:
        if name in winner_freq: 
            winner_freq[name] += 1
        else:
            winner_freq[name] = 1

    for name in set(winners):
        win_cnt = [0]
        for i in range(1, TRIALS):
            win_cnt.append(win_cnt[i - 1] + 1) if winners[i] == name else win_cnt.append(win_cnt[i - 1])

        plt.plot(win_cnt, label=name)

    plt.title("Cumulative lineplot of winners per trial")
    plt.ylabel("Wins sum")
    plt.xlabel("Trials")
    plt.legend()
    plt.show()
    
    plt.title("Hist plot of the winners")
    plt.bar(list(winner_freq.keys()), list(winner_freq.values()))
    plt.show()

def main():
    winners = []

    players = {}
    for bidder in BIDDERS:
        players[bidder['name']] = bidder['strategy'](bidder['name'], START_BALANCE, TRIALS)

    for _ in range(TRIALS):
        auction = Auction(BASELINE_AMOUNT, players.copy())
        winner, max_bid = auction.run()
        [player.announce_winner(winner, max_bid) for player in players.values()]

        winners.append(winner)

    plot_results(winners)

main()
