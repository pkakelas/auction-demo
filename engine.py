class Auction:
    def __init__(self, baseline_amount, players):
        print("-- Starting new auction! --")
        print("players: {}, baseline_amount: {}\n".format(len(players), baseline_amount))

        self.players = players
        self.baseline_amount = baseline_amount

    def verify_bid(self, player, bid):
        return bid <= player.get_balance()

    def collect_bids(self):
        bids = {}

        for name, player in self.players.items():
            bid = player.bid(self.baseline_amount)
            print("[BIDDING] Player {} bidded {}".format(name, bid))

            if self.verify_bid(player, bid):
                bids[name] = bid

        return bids

    def get_max_bidder(self, bids):
        max_bid = -1
        max_bidder = None

        for name, bid in bids.items():
            if bid > max_bid:
                max_bidder = name
                max_bid = bid

        return max_bidder, max_bid

    def run(self):
        bids = self.collect_bids()
        max_bidder, max_bid = self.get_max_bidder(bids)
        self.players[max_bidder].pay(max_bid)

        print("[AUCTION] Winner {} bidded {}".format(max_bidder, max_bid))

        return max_bidder, max_bid
