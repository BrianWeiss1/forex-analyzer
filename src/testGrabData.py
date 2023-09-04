import datetime
import requests
import json
import matplotlib
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
        lst.append(grabHistoricalDataBTC(ticker, time, "5m", apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest5min.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()

