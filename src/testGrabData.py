import datetime
import requests
import json
import ccxt
import yfinance as yf
import pandas as pd

def grabHistoricalData(ticker = "EURJPY"):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M')
        for item in data:
            del item['ticker']
        return data
    startDate = "2023-07-30 9:45"
    endDate = '2023-08-23 10:14'
    apikey = '54e4aae1277e71d6e2dd03ba604720662055a9f4'
    apikey2 = 'a94f963a602203b1ade0d6f3e63a5954740870f3'
    timeFrame = "1min"

    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?startDate={startDate}&endDate={endDate}&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?startDate={startDate}&resampleFreq={timeFrame}&token={apikey}"
    url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?resampleFreq={timeFrame}&token={apikey2}"

    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = json.loads(response.content)
        # if type(data) == NoneType

        return dataConvertor(data)
    else:
        print("Error: API request failed. Code: {}. Message: {}".format(response.status_code, response.text))

def findSpecificData(ticker, date):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M')
        for item in data:
            del item['ticker']
        return data
    endDate = date #Format: '2023-08-23 10:14'
    apikey = '54e4aae1277e71d6e2dd03ba604720662055a9f4'
    apikey2 = 'a94f963a602203b1ade0d6f3e63a5954740870f3'
    timeFrame = "1min"

    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?startDate={startDate}&endDate={endDate}&resampleFreq={timeFrame}&token={apikey}"
    url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?&endDate={endDate}&resampleFreq={timeFrame}&token={apikey2}"
    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?resampleFreq={timeFrame}&token={apikey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)

        return dataConvertor(data)
    else:
        print("Error: API request failed. Code: {}. Message: {}".format(response.status_code, response.text))


def grabHistoricalDataBTC(ticker, startDate='2023-07-30 9:45', timeFrame='1min', apikey="54e4aae1277e71d6e2dd03ba604720662055a9f4"):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M')
        # for item in data:
        #     del item['ticker']
        return data
    endDate = '2023-07-30 9:45'
    apikey = '54e4aae1277e71d6e2dd03ba604720662055a9f4'
    apikey2 = 'a94f963a602203b1ade0d6f3e63a5954740870f3'
    timeFrame = "1min"
    url = f'https://api.tiingo.com/tiingo/crypto/prices?tickers={ticker}&startDate={startDate}&resampleFreq={timeFrame}&token={apikey}'
    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?startDate={startDate}&endDate={endDate}&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?startDate={startDate}&resampleFreq={timeFrame}&token={apikey}"

    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?resampleFreq={timeFrame}&token={apikey2}"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)
        # if type(data) == NoneType
        data = data[0]['priceData']
        # return data
        return dataConvertor(data)
    else:
        print("Error: API request failed. Code: {}. Message: {}".format(response.status_code, response.text))

def calltimes(ticker, times, startTime='2023-07-30 9:45'):
    def combine_lists(lst):
        combined_list = []
        for sublist in lst:
            combined_list.extend(sublist)
        return combined_list

    input_format = "%Y-%m-%d %H:%M"

    initial_time = datetime.datetime.strptime(startTime, input_format)
    duration_to_add = datetime.timedelta(minutes=5001)
    lst = []
    apikey2 = 'a9b4c87998c9ca386388f1eceaf3e64391f61f8d'
    time = initial_time
    for i in range(times):
        lst.append(grabHistoricalDataBTC(ticker, time, "1min", apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()


def calltimes5m(ticker, times, startTime='2023-07-30 9:45'):
    def combine_lists(lst):
        combined_list = []
        for sublist in lst:
            combined_list.extend(sublist)
        return combined_list

    input_format = "%Y-%m-%d %H:%M"

    initial_time = datetime.datetime.strptime(startTime, input_format)
    duration_to_add = datetime.timedelta(minutes=(5001*30))
    lst = []
    apikey2 = 'a9b4c87998c9ca386388f1eceaf3e64391f61f8d'
    time = initial_time
    for i in range(times):
        lst.append(grabHistoricalDataBTC(ticker, time, "30min", apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest5min.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()





def grabCurrentDataBTC(ticker, timeFrame='1min', apikey="54e4aae1277e71d6e2dd03ba604720662055a9f4"):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M')
        # for item in data:
        #     del item['ticker']
        return data
    apikey = '54e4aae1277e71d6e2dd03ba604720662055a9f4'
    apikey2 = 'a94f963a602203b1ade0d6f3e63a5954740870f3'
    timeFrame = "1min"
    url = f'https://api.tiingo.com/tiingo/crypto/prices?tickers={ticker}&resampleFreq={timeFrame}&token={apikey}'
    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?startDate={startDate}&endDate={endDate}&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?startDate={startDate}&resampleFreq={timeFrame}&token={apikey}"

    # url = f"https://api.tiingo.com/tiingo/crypto/{ticker}/prices?resampleFreq={timeFrame}&token={apikey2}"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)
        # if type(data) == NoneType
        data = data[0]['priceData']
        # return data
        return dataConvertor(data)
    else:
        print("Error: API request failed. Code: {}. Message: {}".format(response.status_code, response.text))

def calltimes(ticker, times, startTime='2023-07-30 9:45', apikey2= 'a9b4c87998c9ca386388f1eceaf3e64391f61f8d'):
    def combine_lists(lst):
        combined_list = []
        for sublist in lst:
            combined_list.extend(sublist)
        return combined_list

    input_format = "%Y-%m-%d %H:%M"

    initial_time = datetime.datetime.strptime(startTime, input_format)
    duration_to_add = datetime.timedelta(minutes=5001)
    lst = []
    time = initial_time
    for i in range(times):
        lst.append(grabHistoricalDataBTC(ticker, time, "1min", apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()
    return lst


def calltimes5m(ticker, times, startTime='2023-07-30 9:45'):
    def combine_lists(lst):
        combined_list = []
        for sublist in lst:
            combined_list.extend(sublist)
        return combined_list

    input_format = "%Y-%m-%d %H:%M"

    initial_time = datetime.datetime.strptime(startTime, input_format)
    duration_to_add = datetime.timedelta(minutes=(5001*5))
    lst = []
    apikey2 = 'a9b4c87998c9ca386388f1eceaf3e64391f61f8d'
    time = initial_time
    for i in range(times):
        lst.append(grabHistoricalDataBTC(ticker, time, "5min", apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest5min.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()
def calltimes15m(ticker, amount):
    binance = ccxt.binance()
    ticker = ticker.split("USD")
    ticker = ticker[0]
    symbol = f'{ticker}/USDT'
    timeframe = '30m'

    limit = amount 
    # amount = 

    # Fetch historical data
    ohlcv = binance.fetch_ohlcv(symbol, timeframe, limit=1000)

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

    # print(len(formatted_data))

    f = open('documents/dataCryptoTest15min.txt', 'w')
    f.write(str(formatted_data))
    f.close()
    return formatted_data

def getYahoo():
    aapl= yf.Ticker("BTC-USD")
    aapl_historical = aapl.history(start="2023-07-13", end="2023-09-20", interval="30m")
    aapl = pd.DataFrame(aapl_historical)
    return aapl
def calltimes30(symbol, start_time = '2030-02-23'):
    endpoint = "https://api.binance.com/api/v1/klines"

    api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtle" # 0imfnc8mVLWwsAawjYr4RxAf50DDqtlx
    symbol.split()
    symbol = symbol
    interval = "30m"
    start_time = '2023-08-27' # prev 2023-02-23
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
    # print(formatted_data)
    f = open('documents/binance30.txt', 'w')
    f.write(str(formatted_data))
    f.close()
    return formatted_data
def calltimes30(symbol, start_time = '2023-02-23'):
    endpoint = "https://api.binance.com/api/v1/klines"

    api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtle" # 0imfnc8mVLWwsAawjYr4RxAf50DDqtlx
    symbol.split()
    symbol = symbol
    interval = "30m"
    start_time = start_time # prev 2023-02-23, '2023-05-23
    date_obj = datetime.datetime.strptime(start_time, "%Y-%m-%d")
    timestamp_ms = int(date_obj.timestamp()) * 1000
    end_time = '2023-09-30'
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
    f = open('documents/binance30.txt', 'w')
    f.write(str(formatted_data))
    f.close()
    return formatted_data
def calltimes30FIXED(symbol, start_time = '2030-02-23'):
    endpoint = "https://api.binance.com/api/v1/klines"

    api_key = "0imfnc8mVLWwsAawjYr4RxAf50DDqtle" # 0imfnc8mVLWwsAawjYr4RxAf50DDqtlx
    symbol.split()
    symbol = symbol
    interval = "30m"
    start_time = '2023-08-27' # prev 2023-02-23
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
    # print(formatted_data)
    f = open('documents/binance30.txt', 'w')
    f.write(str(formatted_data))
    f.close()
    return formatted_data