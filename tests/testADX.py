import pandas as pd
from ta.trend import ADXIndicator

def grabADX(df, lookback):
    def get_adx(high, low, close, lookback):
        plus_dm = high.diff()
        minus_dm = low.diff()
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm > 0] = 0
        
        tr1 = pd.DataFrame(high - low)
        tr2 = pd.DataFrame(abs(high - close.shift(1)))
        tr3 = pd.DataFrame(abs(low - close.shift(1)))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
        atr = tr.rolling(lookback).mean()
        
        plus_di = 100 * (plus_dm.ewm(alpha = 1/lookback).mean() / atr)
        minus_di = abs(100 * (minus_dm.ewm(alpha = 1/lookback).mean() / atr))
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (lookback - 1)) + dx) / lookback
        adx_smooth = adx.ewm(alpha = 1/lookback).mean()
        return plus_di, minus_di, adx_smooth

    df['plus_di'] = pd.DataFrame(get_adx(df['high'], df['low'], df['close'], lookback)[0]).rename(columns = {0:'plus_di'})
    df['minus_di'] = pd.DataFrame(get_adx(df['high'], df['low'], df['close'], lookback)[1]).rename(columns = {0:'minus_di'})
    df['adx'] = pd.DataFrame(get_adx(df['high'], df['low'], df['close'], lookback)[2]).rename(columns = {0:'adx'})
    df = df.dropna()
    df.tail()
    return df
def get_adx(df, window=4):
    A_ind = ADXIndicator(df['high'], df['low'], df['close'], window)
    df['adx'] = pd.DataFrame(ADXIndicator.adx(A_ind)[0]).rename(columns = {0:'adx'})
    df = df.dropna()
    return df
    


 