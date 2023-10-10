# python-coinflip-martingale

![Martingale](img/martingale.png)
![Bulk Martingale](img/bulk_martingale.png)

This project contains two python scripts, `martingale.py` and `bulk_martingale.py`, that simulate the Martingale betting strategy on a simple coin flip game.

## martingale.py

`martingale.py` is a script that simulates a single run of the Martingale betting strategy. The player starts with a certain balance and a base bet. The player then flips a coin. If the player wins, they gain the amount of their bet and the bet resets to the base bet. If the player loses, they lose the amount of their bet and the bet doubles. The game ends after a certain number of iterations, or if the player's balance reaches a stop loss value or an upper limit.

The script also has the option to graph the player's balance over time.

## bulk_martingale.py

`bulk_martingale.py` is a script that runs the `simulate` function from `martingale.py` multiple times and calculates the win/loss rate and the net balance after all runs. A win is considered when the final balance is more than the starting balance. A loss is considered when the final balance is less than the starting balance.

## How to run

Both scripts use the `click` library for command line interfaces. To run a script, navigate to the directory containing the script and type `python <script name>`. You can also specify options like balance, bet, iterations, limit, stop, and graph (for `martingale.py`) or runs (for `bulk_martingale.py`).

## Dependencies

- Python 3
- Click
- Matplotlib (for `martingale.py`'s `--graph` flag)

## Disclaimer

This project is for educational purposes only. The Martingale betting strategy is a high risk strategy and should not be used for actual betting.