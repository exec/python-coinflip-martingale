import click
from martingale import simulate

@click.command()
@click.option('--balance', default=1000, help='Starting balance.')
@click.option('--bet', default=1, help='Base bet.')
@click.option('--iterations', default=100, help='Number of iterations.')
@click.option('--limit', default=float('inf'), help='Upper limit balance.')
@click.option('--stop', default=0, help='Stop loss value.')
@click.option('--runs', default=100, help='Number of simulation runs.')

def run_simulations(balance=1000, bet=1, iterations=100, limit=float('inf'), stop=0, runs=100):
    """
    This program runs the 'simulate' function multiple times and calculates the win/loss rate.
    A win is considered when the final balance is more than the starting balance.
    A loss is considered when the final balance is less than the starting balance.
    It also calculates the net balance after all runs.
    """
    wins = 0
    losses = 0
    net_balance = 0

    for _ in range(runs):
        result = simulate(balance, bet, iterations, limit, stop, graph=False)
        net_balance += result - balance  # calculate net balance

        if result > balance:
            wins += 1
        elif result < balance:
            losses += 1

    win_rate = wins / runs * 100
    loss_rate = losses / runs * 100
    average_net_balance = net_balance / runs

    print('Win rate: {}%, Loss rate: {}%'.format(win_rate, loss_rate))
    print('Net balance after all runs: {}'.format(net_balance))
    print('Average net balance per run: {}'.format(average_net_balance))

if __name__ == '__main__':
    run_simulations()