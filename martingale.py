import random
from faker import Faker
import plotly.graph_objects as go
from plotly.offline import plot

def simulate(balance=1000, bet=1, iterations=100, limit=float('inf'), stop=0, graph=False):
    base_bet = bet
    balances = [balance]

    for i in range(iterations):
        while bet <= balance:
            # Flip a coin
            flip = random.randint(0, 1)

            if flip == 0:  # Loss
                balance -= bet
                bet *= 2  # Double the bet
            else:  # Win
                balance += bet
                bet = base_bet  # Return to base bet

            balances.append(balance)

            # Stop if balance reaches the stop loss value or the upper limit
            if balance <= stop:
                print('Reached the stop loss value.')
                return balance, balances, False
            elif balance >= limit:
                print('Reached the upper limit.')
                return balance, balances, True

        # Print the iteration results
        print('Iteration: {}, Balance: {}, Bet: {}'.format(i+1, balance, bet))

        # Reset bet to base bet if busted
        if bet > balance:
            print("Busted with bet of {} and money left {}".format(bet, balance))
            bet = base_bet

    # Return final balance, balances and whether the person left happy
    return balance, balances, balance > stop

if __name__ == '__main__':
    import click

    @click.command()
    @click.option('--balance', default=1000, help='Starting balance.')
    @click.option('--bet', default=1, help='Base bet.')
    @click.option('--iterations', default=100, help='Number of iterations.')
    @click.option('--limit', default=float('inf'), help='Upper limit balance.')
    @click.option('--stop', default=0, help='Stop loss value.')
    @click.option('--graph', is_flag=True, help='If set, draw a graph.')
    def cli(balance, bet, iterations, limit, stop, graph):
        """Simulates a number of coinflip scenarios following the martingale betting strategy to recover losses and reset on wins."""

        sim_result, balances, happy = simulate(balance, bet, iterations, limit, stop, graph)
        print('Final balance: {}'.format(sim_result))
        print('Profit: {}'.format(sim_result - balance))
        print('Left happy: {}'.format(happy))
        return sim_result, balances, happy

    cli()