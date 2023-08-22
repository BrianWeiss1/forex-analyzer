import numpy as np


def hma(df, period):
 wma_1 = df['close'].rolling(period//2).apply(lambda x: \
 np.sum(x * np.arange(1, period//2+1)) / np.sum(np.arange(1, period//2+1)), raw=True)
 wma_2 = df['close'].rolling(period).apply(lambda x: \
 np.sum(x * np.arange(1, period+1)) / np.sum(np.arange(1, period+1)), raw=True)
 diff = 2 * wma_1 - wma_2
 hma = diff.rolling(int(np.sqrt(period))).mean()
 df[f'hma_{period}'] = hma