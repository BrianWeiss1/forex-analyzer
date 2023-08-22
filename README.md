# forex-analyzer

This repository analyzes forex buy and sell opportunities based on four indicators:
  - RSI (Relative Strength Index)
  - Stochastic Oscillator
  - EMA (Exponential Moving Average)
  - Supertrend

The repository also includes a simulator that allows you to test different trading strategies. The simulator starts with a balance of $5 and uses a random number generator to simulate the results of 100 trades.

The following are the results of two different trading strategies:

Strategy 1: 82% success rate, trading 5% of the time.
Mean result: $2972.39
Median result: $1619.05
Best result: $37346.30
Worst result: $57.16
Strategy 2: 77% success rate, trading 15% of the time.
Mean result: $9009628.24
Median result: $1194560.12
Best result: $150114495.60
Worst result: $18250.17

The results of the simulator are just estimates and should not be taken as guarantees of future profits. However, they can be used to help you choose a trading strategy that is right for you.

To use the simulator, clone the repository and install the dependencies. Then, run the following command:

```
python3 tests/functionTests/simulator.py
```
