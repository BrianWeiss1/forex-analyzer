import yfinance as yf

def grabData(forexSymbol):
    forex_data_minute = yf.download(f'{forexSymbol}=X', period='m', interval='1m')
    values = {}
    values['Low'] = forex_data_minute['Low']
    values['Close'] = forex_data_minute['Close']
    values['High'] = forex_data_minute['High']
    return values

import requests
import pandas as pd
from datetime import datetime, timedelta
def get_SMA(closedValues):
    close_prices = closedValues
    # Calculate the Simple Moving Average (SMA)
    sma_period = 14  # Adjust the period as needed
    sma = close_prices.rolling(window=sma_period).mean()
    return sma

def get_stoch(symbol, k_period, d_period, start_date):
    api_key = open(r'src/api_key.txt').read().strip()
    end_date = start_date - timedelta(hours=1)  # Get data for the past hour
    url = f'https://www.alphavantage.co/query?function=STOCH&symbol={symbol}&interval=1min&fastkperiod={k_period}&slowdperiod={d_period}&apikey={api_key}'
    raw = requests.get(url).json()
    data = raw['Technical Analysis: STOCH']
    df = pd.DataFrame(data).T
    df.index = pd.to_datetime(df.index)
    df = df.tz_localize(None)  # Convert to timezone-naive index
    df = df[df.index >= end_date]  # Filter data for the past hour
    df = df.astype(float)
    return df['SlowK'], df['SlowD']

usdEUR = {}
usdEUR['Close'] = grabData('EURUSD')['Close']
# print(get_SMA(usdEUR['Close']))

now = datetime.now()
usdEUR['%k'], usdEUR['%d'] = get_stoch('EURUSD', 2, 3, now)
print(usdEUR['%d']) # + 6 hours
print(usdEUR['%k'])
# nflx = pd.DataFrame(usdEUR).dropna()
# nflx.head()

   