from ta.trend import IchimokuIndicator
import pandas as pd
import pandas_ta as ta

def get_ichimoku(data, window=9, window2=26, window3=52):
    ich_ind = IchimokuIndicator(data['high'], data['low'], window, window2, window3)
    ich_b = IchimokuIndicator.ichimoku_a(ich_ind)
    ich_a = IchimokuIndicator.ichimoku_b(ich_ind)
    ich_base = IchimokuIndicator.ichimoku_base_line(ich_ind)
    ich_cover = IchimokuIndicator.ichimoku_conversion_line(ich_ind)
    return pd.DataFrame({
        'cover': ich_cover,
        'a': ich_a,
        'b': ich_b,
        'base': ich_base,
    })
def get_itch(df, cl_period=9, bl_period=26, lead_span_b_period=52):
    # cl_period = 20 

    # # Define length of Kijun Sen or Base Line
    # bl_period = 60  

    # # Define length of Senkou Sen B or Leading Span B
    # lead_span_b_period = 120  

    # Define length of Chikou Span or Lagging Span
    lag_span_period = 30  

    # Calculate conversion line
    high_20 = df['High'].rolling(cl_period).max()
    low_20 = df['Low'].rolling(cl_period).min()
    df['conversion_line'] = (high_20 + low_20) / 2

    # Calculate based line
    high_60 = df['High'].rolling(bl_period).max()
    low_60 = df['Low'].rolling(bl_period).min()
    df['base_line'] = (high_60 + low_60) / 2

    # Calculate leading span A
    df['lead_span_A'] = ((df.conversion_line + df.base_line) / 2).shift(lag_span_period)

    # Calculate leading span B
    high_120 = df['High'].rolling(120).max()
    low_120 = df['High'].rolling(120).min()
    df['lead_span_B'] = ((high_120 + low_120) / 2).shift(lead_span_b_period)

    # Calculate lagging span
    df['lagging_span'] = df['Close'].shift(-lag_span_period)
    return df