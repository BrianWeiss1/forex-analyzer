import yfinance as yf
import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import pyautogui

buy = 1118, 387
sell = 1123, 462
def checkTime(lastMin = -1):
    if lastMin == datetime.now().minute:
        return False
    lastMin = datetime.now().minute
    if (datetime.now().second >= 1 and datetime.now().second <= 2):
        return True
    else:
        return False
def grabData(forexSymbol):
    forex_data_minute = yf.download(f'{forexSymbol}=X', period='m', interval='1m')
    values = {}
    values['Low'] = forex_data_minute['Low']
    values['Close'] = forex_data_minute['Close']
    values['High'] = forex_data_minute['High']
    return values
def rsiNumbers(close_prices):
    # Calculate price changes
    price_changes = close_prices.diff().dropna()

    # Separate gains and losses
    gains = price_changes.apply(lambda x: max(0, x))
    losses = price_changes.apply(lambda x: max(0, -x))

    # Calculate average gains and losses (EMA)
    average_gain = gains.ewm(span=14, adjust=False).mean()
    average_loss = losses.ewm(span=14, adjust=False).mean()

    # Calculate relative strength (RS)
    relative_strength = average_gain / average_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + relative_strength))

    # Convert RSI DataFrame to an array
    rsi_array = rsi.values

    print("Array of RSI values:")
    print(rsi_array)


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
    return 100-df['SlowD'], 100-df['SlowK'] #Swapped due to error in calulation
def compareGetStoch(kValue, dValue, pointOfError):
    def findBuy(kValue, dValue):
        if kValue < dValue and kValue+pointOfError < dValue and kValue < 20 and dValue < 20:
            return True
        else:
            if (kValue+20 < dValue):
                return True
            else:
                return False
        
    def findSell(kValue, dValue):
        if kValue > dValue and kValue > dValue+pointOfError and kValue > 80 and dValue < 80:
            return True
        else:
            if (kValue > dValue+20):
                return True
            else:
                return False
    signals = {}
    signals['buy'] = findBuy(kValue, dValue)
    signals['sell'] = findSell(kValue, dValue)
    return signals
def automaticBuy():
    pyautogui.click(buy)
def automaticSell():
    pyautogui.click(sell)

if __name__ == "__main__":
    symbol = 'EURJPY'
    symbolInformation = {}
    while True:
        if checkTime() == True:
            print(datetime.now())
            now = datetime.now()
            symbolInformation['%k'], symbolInformation['%d'] = get_stoch(symbol, 4, 3, now)
            print("%K:" + str(symbolInformation['%k'][0]))
            print("%D:" + str(symbolInformation['%d'][0]))
            pointOfError = 9
            stochSignals = compareGetStoch(symbolInformation['%k'][0], symbolInformation['%d'][0], pointOfError)

            if (stochSignals['buy']):
                print('Buy: ' + str(now))
                automaticBuy()
            if (stochSignals['sell']):
                print('Sell ' + str(now))
                automaticSell()
                