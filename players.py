# Just increased amount by 10 each time

class AbstractBidder:
    def __init__(self, name, balance, trials):
        self.name = name
        self.balance = balance
        self.trials = trials
        self.won_trials = 0
        self.won_prev_trial = False
        self.current_trial = 0
        self.prev_bid = 0

    def pay(self, amount):
        self.balance -= amount
        return self.balance > 0

    def announce_winner(self, winner):
        self.current_trial += 1

        if winner == self.name:
            self.won_prev_trial = True
            self.won_trials += 1
        else:
            self.won_prev_trial = False

    def get_balance(self):
        return self.balance

    def bid(self, baseline_amount):
        bid = self.make_bid(baseline_amount)
        self.prev_bid = bid

        # Check if cannot afford the bid
        return bid if bid <= self.balance else 0

    # Main strategy implementation
    def make_bid(self, max_bid_amount):
        raise Exception("Should be implemented")

class DoubleUpBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.prev_bid == 0:
            bid = baseline_amount

        bid = self.prev_bid if self.won_prev_trial else self.prev_bid * 2
        return bid

class IncreaseBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        return baseline_amount + (.1 * baseline_amount)

class MiddleBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        return baseline_amount + (self.balance / 2)

class AllInBidder(AbstractBidder):
    def make_bid(self, max_bid_amount):
        return self.balance

class SameBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        return 5000

class DistributeBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.prev_bid == 0:
            self.prev_bid = baseline_amount

        trials_left = self.trials - self.current_trial
        bid = self.prev_bid if self.won_prev_trial else int(self.balance / trials_left)

        return bid
