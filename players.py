# Just increased amount by 10 each time

class AbstractBidder:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        return self.balance > 0

    def receive(self, amount):
        self.balance += amount 

    def get_balance(self):
        return self.balance

    def set_auction_info(self, rounds, start_price, round_fee):
        self.rounds = rounds
        self.start_price = start_price
        self.round_fee = round_fee 

    def bid(self, max_bid_amount):
        bid = self.make_bid(max_bid_amount)
        if bid > self.balance:
            raise Exception("Bidder bidding money he cannot afford")

        return bid

    # Main strategy implementation
    def make_bid(self, max_bid_amount):
        raise Exception("Should be implemented")

# If player has money then increase max_bid by 10 else quit
class DummyBidder(AbstractBidder):
    def make_bid(self, max_bid_amount):
        if max_bid_amount < self.balance - 10:
            return max_bid_amount + 10

        return 0

# Give all of his money to the first product
class RiskyBidder(AbstractBidder):
    # Main strategy implementation
    def make_bid(self, max_bid_amount):
        if self.balance > 0:
            return self.balance

        return 0
