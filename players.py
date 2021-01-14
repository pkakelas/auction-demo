from random import randint

class AbstractBidder:
    def __init__(self, name, balance, trials):
        self.name = name
        self.balance = balance
        self.trials = trials
        self.won_trials = 0
        self.won_prev_trial = False
        self.prev_win_amount = 0
        self.current_trial = 0
        self.prev_bid = 0

    def pay(self, amount):
        self.balance -= amount
        return self.balance > 0

    def announce_winner(self, winner, amount):
        self.current_trial += 1
        self.prev_win_amount = amount

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

# MartingaleBidder beds twice the amount he looses otherwise bets the baseline amount
class MartingaleBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.prev_bid == 0 or self.won_prev_trial:
            return baseline_amount
        else:
            return self.prev_bid * 2

# ScaleBidder bibs more money as the trials come to an end 
class ScaleBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.current_trial < self.trials / 2 or self.prev_bid == 0:
            return baseline_amount
        if self.current_trial < self.trials / 4: 
            return baseline_amount * 10
        if self.current_trial < self.trials / 8: 
            return baseline_amount * 50

        return baseline_amount * 100

# IncreaseBidder increases the winning bid of the previous round by 2
class IncreaseBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.balance < 2 * self.prev_win_amount:
            return 2 * self.prev_win_amount

        return self.balance

# DoubleUpBidder increases his bid by a factor of 2 on each trial
class DoubleUpBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.prev_bid == 0:
            return baseline_amount
        else: 
            return self.prev_bid * 2

# DrunkBidder bids a random unit of money between baseline and his self.balance / 10 
class DrunkBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if int(self.balance / 10) > baseline_amount:
            return randint(baseline_amount, int(self.balance / 10))

        return baseline_amount

# AllInBidder bids all of his money during the first round
class AllInBidder(AbstractBidder):
    def make_bid(self, max_bid_amount):
        return self.balance

# EvenBidder plays only on even rounds and splits his balance according to the function below
class EvenBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.current_trial % 2 == 0:
            return int(self.balance / (self.trials / 4))

        return 0

# DistributeBidder splits his balance evenly on the remaining trials if he losses
# otherwise he keeps his bid the same;
class DistributeBidder(AbstractBidder):
    def make_bid(self, baseline_amount):
        if self.prev_bid == 0:
            return baseline_amount

        trials_left = self.trials - self.current_trial
        return self.prev_bid if self.won_prev_trial else int(self.balance / trials_left)

