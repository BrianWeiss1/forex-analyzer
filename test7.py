import requests
from datetime import datetime
endpoint = "https://api.binance.com/api/v1/klines"

api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtlx"
symbol = "BTCUSDT"
interval = "30m"
start_time = '2023-01-01'
date_obj = datetime.strptime(start_time, "%Y-%m-%d")
timestamp_ms = int(date_obj.timestamp()) * 1000
end_time = '2023-08-11'
date_obj = datetime.strptime(end_time, "%Y-%m-%d")
timestamp_ms2 = int(date_obj.timestamp()) * 1000

# Define the initial time range (adjust startTime and endTime)
start_time = timestamp_ms  # Replace with your desired start time in milliseconds
end_time = timestamp_ms2    # Replace with your desired end time in milliseconds

limit = 1000
all_data = []

while start_time < end_time:
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
    }

    headers = {
        "X-MBX-APIKEY": api_key,
    }

    response = requests.get(endpoint, params=params, headers=headers)

    if response.status_code == 200:
        historical_data = response.json()
        if not historical_data:
            break
        all_data.extend(historical_data)
        start_time = historical_data[-1][0] + 1  # Set the new startTime for the next request

    else:
        print(f"Error: {response.status_code}, {response.text}")
        break

# Process and save all_data as needed

for candle in all_data:
    timestamp = candle[0] / 1000  # Convert milliseconds to seconds
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
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

