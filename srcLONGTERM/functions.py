from ta.momentum import StochasticOscillator
def get_STOCH(data, window1=14, window2=3):
    stochind = StochasticOscillator(data['high'], data['low'], data['close'], window1, window2)
    return StochasticOscillator.stoch(stochind), StochasticOscillator.stoch_signal(stochind)
def getSTOCGH(data, window, window2):
    data.ta.stoch(high='High', low='Low',close= 'Close', k=window, d=window2, append=True)
def getSTOCHHH(data, period, period2):
    data['Lowest Low'] = data['low'].rolling(window=period).min()
    data['Highest High'] = data['high'].rolling(window=period).max()
    data['%K'] = 100 * (data['close'] - data['Lowest Low']) / (data['Highest High'] - data['Lowest Low'])
    data['%D'] = data['%K'].rolling(window=period2).mean()