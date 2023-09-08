import ccxt
import datetime

# Initialize the Binance API client
binance = ccxt.binance()

# Define the symbol you want to fetch data for (e.g., BTC/USDT)
symbol = 'BTC/USDT'

# Define the timeframe (1 minute in this case)
timeframe = '15m'

# Define the number of data points you want to fetch
limit = 1000  # Adjust this number as needed

# Fetch historical data
ohlcv = binance.fetch_ohlcv(symbol, timeframe, limit=limit)

# Initialize a list to store the formatted data
formatted_data = []

# Format the data
for candle in ohlcv:
    timestamp = candle[0] / 1000  # Convert milliseconds to seconds
    date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
    open_price = candle[1]
    high_price = candle[2]
    low_price = candle[3]
    close_price = candle[4]
    volume = candle[5]

    formatted_candle = {
        'date': date,
        'open': open_price,
        'high': high_price,
        'low': low_price,
        'close': close_price,
        'volume': volume,
    }

    formatted_data.append(formatted_candle)

# Print or save the formatted data
print(formatted_data)
print(len(formatted_data))