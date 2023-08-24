from ta.momentum import williams_r
def STOCHF(df):
    williams_r(df['high'], df['low'], df['close'], 14)