import datetime
import requests
import json
import matplotlib
def grabHistoricalData(ticker = "EURUSD"):
    def dataConvertor(data):
        for item in data:
            item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M')
        for item in data:
            del item['ticker']
        return data
    startDate = "2023-01-23 9:45"
    endDate = '2023-08-23 10:14'
    apikey = '54e4aae1277e71d6e2dd03ba604720662055a9f4'
    timeFrame = "1min"

    url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?startDate={startDate}&endDate={endDate}&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?startDate={startDate}&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices&resampleFreq={timeFrame}&token={apikey}"
    # url = f"https://api.tiingo.com/tiingo/fx/{ticker}/prices?resampleFreq={timeFrame}&token={apikey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)

        return dataConvertor(data)
    else:
        print("Error: API request failed. Code: {}. Message: {}".format(response.status_code, response.text))