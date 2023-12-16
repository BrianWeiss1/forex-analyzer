import datetime
import requests
from SpecialFunctions import formatDataset, formatDataset3
def calltimes30(symbol, start_time = '2015-11-17'):
    endpoint = "https://api.binance.com/api/v1/klines"

    api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtle" # 0imfnc8mVLWwsAawjYr4RxAf50DDqtlx
    symbol.split()
    symbol = symbol
    interval = "30m"
    start_time = start_time # prev 2023-02-23, '2023-05-23
    date_obj = datetime.datetime.strptime(start_time, "%Y-%m-%d")
    timestamp_ms = int(date_obj.timestamp()) * 1000
    end_time = '2023-12-15'
    date_obj = datetime.datetime.strptime(end_time, "%Y-%m-%d")
    timestamp_ms2 = int(date_obj.timestamp()) * 1000

    # Define the initial time range (adjust startTime and endTime)
    start_time = timestamp_ms  # Replace with your desired start time in milliseconds
    end_time = timestamp_ms2    # Replace with your desired end time in milliseconds
    formatted_data = []

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


    for candle in all_data:
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
    # print(formatted_data)
    split_pair = symbol.split("USDT")
    f = open(f'documents/{split_pair[0]}Data.txt', 'w')
    f.write(str(formatted_data))
    f.close()
    return formatted_data
def calltimes30FIXED(symbol, start_time = '2023-08-27'):
    endpoint = "https://api.binance.com/api/v1/klines"

    api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtle" # 0imfnc8mVLWwsAawjYr4RxAf50DDqtlx
    symbol.split()
    symbol = symbol
    interval = "30m"
    start_time = start_time # prev 2023-02-23
    date_obj = datetime.datetime.strptime(start_time, "%Y-%m-%d")
    timestamp_ms = int(date_obj.timestamp()) * 1000
    end_time = '2030-02-23'
    date_obj = datetime.datetime.strptime(end_time, "%Y-%m-%d")
    timestamp_ms2 = int(date_obj.timestamp()) * 1000

    # Define the initial time range (adjust startTime and endTime)
    start_time = timestamp_ms  # Replace with your desired start time in milliseconds
    end_time = timestamp_ms2    # Replace with your desired end time in milliseconds
    formatted_data = []

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


    for candle in all_data:
        timestamp = candle[0] / 1000  # Convert milliseconds to seconds
        date = (datetime.datetime.utcfromtimestamp(timestamp)  - datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
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
    # # print(formatted_data)
    # f = open('documents/binance30.txt', 'w')
    # f.write(str(formatted_data))
    # f.close()
    return formatted_data

def grabForex(values):
    # Define your API key
    api_key = "d6e8542914aa439e92fceaccca1c2708"

    # Define the API endpoint URL
    base_url = "https://api.twelvedata.com/time_series"

    # Define the parameters for the request
    params = {
        "symbol": "EUR/USD",  # The forex symbol you want to retrieve
        "interval": "30min",   # Time interval (e.g., 1min, 1day)
        "outputsize": values,     # Number of data points to retrieve
        "apikey": api_key     # Your Twelve Data API key
        
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data['values']
    
if __name__ == '__main__':
    print(formatDataset3(grabForex(100)))