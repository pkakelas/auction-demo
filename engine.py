class Auction:
    def __init__(self, start_price, rounds, round_fee, players):
        print("-- Starting new auction! --")
        print("players: {}, start_price: {}, rounds: {}, round_fee: {}\n".format(len(players), start_price, rounds, round_fee))

        self.rounds = rounds
        self.round_fee = round_fee
        self.players = players
        self.max_bid = { 'player_name': None, 'amount': start_price }

    def get_entry_fee(self):
        print("[FEE] Players paying entry fee...")

        for player in self.players:
            if not player.pay(self.round_fee):
                print("[FEE] Player quitted this auction:", player.name)
                self.players.remove(player) 

    def verify_bid(self, player, bid):
        if bid == 0:
            print("Player quitted:", player.name)
            self.players.remove(player)
            return True

        if bid < self.max_bid['amount'] or bid > player.get_balance():
            print("Player bidded an invalid amount:", player.name)
            return False

        return True
    
    def update_max_bid(self, player, amount):
        self.max_bid['player_name'] = player.name
        self.max_bid['amount'] = amount

    def play_round(self):
        for player in self.players:
            bid = player.bid(self.max_bid['amount'])
            print("[BIDDING] Player {} bidded {}".format(player.name, bid))

            if self.verify_bid(player, bid):
                self.update_max_bid(player, bid)

    def run(self):
        for round in range(self.rounds):
            self.get_entry_fee()
            if len(self.players) == 1:
                break

            self.play_round()

        print("[AUCTION] Winner", self.max_bid) 
        return self.max_bid['player_name']
