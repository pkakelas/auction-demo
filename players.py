# Just increased amount by 10 each time

class AbstractBidder:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        return self.balance > 0

    def get_balance(self):
        return self.balance

    def bid(self, baseline_amount):
        bid = self.make_bid(baseline_amount)
        if bid > self.balance:
            raise Exception("Bidder bidding money he cannot afford")

        return bid

    # Main strategy implementation
    def make_bid(self, max_bid_amount):
        raise Exception("Should be implemented")

# If player has money then increase max_bid by 10 else quit
class RationalBidder(AbstractBidder):
    def make_bid(self, max_bid_amount):
        to_bet = max_bid_amount + (.1 * max_bid_amount)
        if to_bet <= self.balance:
            return to_bet

        return 0

# Give all of his money to the first product
class RiskyBidder(AbstractBidder):
    # Main strategy implementation
    def make_bid(self, max_bid_amount):
        return self.balance

class IncreaseBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        to_bet = baseline_amount + (.1 * baseline_amount)

        return to_bet if to_bet <= self.balance else 0

class MiddleBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        to_bet = baseline_amount + (self.balance / 2)

        return to_bet if to_bet <= self.balance else 0

class AllInBidder(AbstractBidder):
    def make_bid(self, max_bid_amount):
        return self.balance
