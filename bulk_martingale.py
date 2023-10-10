import click
from martingale import simulate
from faker import Faker
import plotly.graph_objects as go

@click.command()
@click.option('--balance', default=1000, help='Starting balance.')
@click.option('--bet', default=1, help='Base bet.')
@click.option('--iterations', default=100, help='Number of iterations.')
@click.option('--limit', default=float('inf'), help='Upper limit balance.')
@click.option('--stop', default=0, help='Stop loss value.')
@click.option('--runs', default=100, help='Number of simulation runs.')
@click.option('--graph', is_flag=True, help='If set, draw a graph.')

def run_simulations(balance=1000, bet=1, iterations=100, limit=float('inf'), stop=0, runs=100, graph=False):
    faker = Faker()
    happy_people = 0
    sad_people = 0
    net_balance = 0
    final_balances = []  # list to store final balances
    fig = go.Figure()  # initialize plotly figure

    for _ in range(runs):
        name = faker.name()
        result, balances, happy = simulate(balance, bet, iterations, limit, stop, graph)
        final_balances.append(result)  # append final balance to the list
        net_balance += result - balance  # calculate net balance

        if happy:
            happy_people += 1
        else:
            sad_people += 1

        if graph:
            # add trace for each person
            fig.add_trace(go.Scatter(
                y=balances,
                mode='lines',
                name=name,
                line=dict(color='green' if happy else 'red'),
                hoverinfo='name'
            ))

    happy_rate = round(happy_people / runs * 100, 2)
    average_net_balance = net_balance / runs

    print('Happy rate: {}%'.format(happy_rate))
    print('Net balance after all runs: {}'.format(net_balance))
    print('Average net balance per run: {}'.format(average_net_balance))

    if graph:
        fig.show()

if __name__ == '__main__':
    run_simulations()