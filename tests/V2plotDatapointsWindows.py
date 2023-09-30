import pandas as pd
import matplotlib.pyplot as plt

from SpecialFunctions import formatDataset

# Sample price data (replace with your own data)
f = open("documents/dataCryptoTest.txt", "r")
data = f.readlines()
data = eval(data[0])
f.close()
data = data[len(data)-100: len(data)]
df = formatDataset(data)

periodK = 14
smoothK = 10
periodD = 3

# Calculate %K
df['%K'] = (df['close'] - df['low'].rolling(window=periodK).min()) / (
    df['high'].rolling(window=periodK).max() - df['low'].rolling(window=periodK).min()
) * 100

# Smooth %K
df['%K'] = df['%K'].rolling(window=smoothK).mean()

# Calculate %D
df['%D'] = df['%K'].rolling(window=periodD).mean()

# Plot %K and %D
plt.plot(df['%K'], label='%K')
plt.plot(df['%D'], label='%D')

# Add overbought and oversold lines
plt.axhline(80, color='red', linestyle='--', label='Overbought')
plt.axhline(20, color='green', linestyle='--', label='Oversold')

plt.legend()
plt.title('Stochastic Oscillator')
plt.xlabel('Period')
plt.ylabel('Value')
plt.show()