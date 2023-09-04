from ta.momentum import StochasticOscillator
def get_STOCH(data, window1=14, window2=10, window3=3):
    stochind = StochasticOscillator(data['high'], data['low'], data['close'], window1, window3)
    k = StochasticOscillator.stoch(stochind)
    d = StochasticOscillator.stoch_signal(stochind)
    smoothed_k = k.rolling(window=10).mean()
    return smoothed_k, d

def getSTOCGH(data, window, window2):
    data.ta.stoch(high='High', low='Low',close= 'Close', k=window, d=window2, append=True)
def getSTOCHHH(data, period, period2):
    data['Lowest Low'] = data['low'].rolling(window=period).min()
    data['Highest High'] = data['high'].rolling(window=period).max()
    data['%K'] = 100 * (data['close'] - data['Lowest Low']) / (data['Highest High'] - data['Lowest Low'])
    data['%D'] = data['%K'].rolling(window=period2).mean()
def get_StochasticOscilator(df, periodK, smoothK, periodD):
    # Calculate %K
    df['%K'] = (df['close'] - df['low'].rolling(window=periodK).min()) / (
        df['high'].rolling(window=periodK).max() - df['low'].rolling(window=periodK).min()
    ) * 100

    # Smooth %K
    df['%K'] = df['%K'].rolling(window=smoothK).mean()

    # Calculate %D
    df['%D'] = df['%K'].rolling(window=periodD).mean()