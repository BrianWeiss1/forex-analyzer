from functions import GrabData
from decimal import Decimal
import pandas as pd

def stochastic(df, period = 24, smoothK = 3, smoothD = 3, stoch_lower_band = 5, TYPE = 'Stoch', period_stochRSI = 5, stochRSI_lower_band = 5):
    if TYPE == 'Stoch':
        df_temp = df.copy()
        df_temp['n-High'] = df_temp['Close'].rolling(period).max()
        df_temp['n-Low'] = df_temp['Close'].rolling(period).min()
        df_temp['Stoch %K'] = (((df_temp['Close'] - df_temp['n-Low'])/(df_temp['n-High'] - df_temp['n-Low']))*100).rolling(smoothK).mean()
        df_temp['Stoch %D'] = df_temp['Stoch %K'].rolling(smoothD).mean()
        k = df_temp['Stoch %K']
        d = df_temp['Stoch %D']
        return k, d
        signals = []
        for i in range(len(k)):
            if k[i] > d[i] and k[i] > stoch_lower_band and k[i - 1] < stoch_lower_band:
                signals.append(1)
            else: signals.append(0)
        df_temp['Stoch Signal'] = signals
        df['Stoch Signal'] = df_temp['Stoch Signal'].diff()
        return df
    
    elif TYPE == 'StochRSI':
        period = period_stochRSI
        df_temp = df.copy()
        df_temp['n-High'] = df_temp['RSI'].rolling(period).max()
        df_temp['n-Low'] = df_temp['RSI'].rolling(period).min()
        df_temp['Stoch %K'] = (((df_temp['RSI'] - df_temp['n-Low'])/(df_temp['n-High'] - df_temp['n-Low']))*100).rolling(smoothK).mean()
        df_temp['Stoch %D'] = df_temp['Stoch %K'].rolling(smoothD).mean()
        k = df_temp['Stoch %K']
        d = df_temp['Stoch %D']
        return k, d
        signals = []
        for i in range(len(k)):
            # if k[i] > d[i] and k[i] > lower_band and k[i - 1] < lower_band:
            # if d[i] > lower_band and d[i] < upper_band:
            if k[i] > d[i] and k[i] < stochRSI_lower_band:
                signals.append(1)
    #         elif k[i] < d[i] and k[i] < lower_band:
            else: signals.append(0)
        df_temp['StochRSI Signal'] = signals
        df['StochRSI Signal'] = df_temp['StochRSI Signal']
        return df
# Replace with your Alpha Vantage API key

# Replace with your dataset of closing prices, %K period, %D period, and smoothing period
symbol = "AUDUSD"
closing_prices = GrabData.GrabData(symbol)
print(type(closing_prices))
# print(closing_prices)
k_period = 24
d_period = 3
smoothing_period = 3
closing_prices_series = pd.Series(closing_prices)
print(type(closing_prices_series))
percentK, percentD = stochastic(closing_prices_series)
percentK = round(percentK, 2)
percentD = round(percentD, 2)
print("Last %K:", percentK)
print("Last %D:", percentD)