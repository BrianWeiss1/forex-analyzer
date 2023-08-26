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
def grabHistoricalDataBTC(ticker = "BTCUSD"):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M')
        # for item in data:
        #     del item['ticker']
        return data
    startDate = "2023-07-30 9:45"
    endDate = '2023-08-23 10:14'
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
