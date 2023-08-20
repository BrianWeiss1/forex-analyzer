import pandas_ta as ta

def get_stoch(df, k_period, d_period):

    # Adds a "n_high" column with max value of previous 14 periods
    df['n_high'] = df['high'].rolling(k_period).max()
    # Adds an "n_low" column with min value of previous 14 periods
    df['n_low'] = df['low'].rolling(k_period).min()
    # Uses the min/max values to calculate the %k (as a percentage)
    df['%K'] = (df['close'] - df['n_low']) * 100 / (df['n_high'] - df['n_low'])
    # Uses the %k to calculates a SMA over the past 3 values of %k
    df['%D'] = df['%K'].rolling(d_period).mean()
    # Add some indicators
    df.ta.stoch(high='high', low='low', k=k_period, d=d_period, append=True)
    return df
def get_stoch2(df, k_period, d_period):
    df['14-high'] = df['high'].rolling(k_period).max()
    df['14-low'] = df['low'].rolling(k_period).min()
    df['%K'] = (df['close'] - df['14-low'])*100/(df['14-high'] - df['14-low'])
    df['%D'] = df['%K'].rolling(d_period).mean()
    df.ta.stoch(high='High', low='Low',close= 'Close', k=k_period, d=d_period, append=True)
    return df
def getSTOCHdata(df, length, difference):
    last_datapoints_K = df['STOCHk_100_3_3'].tail(length)
    last_datapoints_D = df['STOCHd_100_3_3'].tail(length)
    countSELL = 0
    countBUY = 0
    for i in range(length):
        if last_datapoints_D[i] > last_datapoints_K[i]+difference:
            countSELL+=1
        if last_datapoints_D[i]+difference < last_datapoints_K[i]:
            countBUY+=1
    if countSELL == length:
        return "SELL"
    if countBUY == length:
        return "BUY"
    return None
def getSTOCHdataSIM(df, length, difference, i, j):
    last_datapoints_K = df[f'STOCHk_{j}_3_3'][i:i+length]
    last_datapoints_D = df[f'STOCHd_{j}_3_3'][i:i+length]
    countSELL = 0
    countBUY = 0
    for i in range(length):
        if last_datapoints_D[i] > last_datapoints_K[i]+difference:
            countSELL+=1
        if last_datapoints_D[i]+difference < last_datapoints_K[i]:
            countBUY+=1
    if countSELL == length:
        return "SELL"
    if countBUY == length:
        return "BUY"
    return None