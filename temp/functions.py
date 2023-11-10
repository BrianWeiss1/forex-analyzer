from ta.momentum import StochRSIIndicator
from temp.SpecialFunctions import formatDataset
import pandas_ta as ta
import numpy as np

def get_StochasticOscilator(df, periodK, smoothK, periodD):
    # Calculate %K
    df['%K'] = (df['close'] - df['low'].rolling(window=periodK).min()) / (
        df['high'].rolling(window=periodK).max() - df['low'].rolling(window=periodK).min()
    ) * 100
    df['%K'] = df['%K'].rolling(window=smoothK).mean()
    df['%D'] = df['%K'].rolling(window=periodD).mean()

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k().values, stochRSIind.stochrsi_d().values
def get_supertrend(data, length, multiplier):
    st = ta.supertrend(data['high'], data['low'], data['close'], length, multiplier)
    st['data'] = data['close']
    print(st)
    df_filtered = st[[f'SUPERT_{length}_{multiplier}.0']]
    st['supertrend'] = df_filtered[f'SUPERT_{length}_{multiplier}.0']
    return st    

if __name__ == '__main__':
    f = open("documents/dataCryptoTest15min.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(data, 14, 3, 3)
    print(stochRSIK, stochRSID)