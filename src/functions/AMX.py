import requests

def ADX(symbol, time_period=14, api_key="YOUR_API_KEY"):
    base_url = "https://www.alphavantage.co/query"


    params = {
        'function': 'ADX',
        'symbol': symbol,
        'interval': '1min',
        'time_period': time_period,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            adx_data = data["Technical Analysis: ADX"]
            return adx_data
        except:
            print(data.keys())
            print("Incorrect key")
            return None

def findADXslope(symbol, length, time_period=14, api_key="YOUR_API_KEY"):
    base_url = "https://www.alphavantage.co/query"


    params = {
        'function': 'ADX',
        'symbol': symbol,
        'interval': '1min',
        'time_period': time_period,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            adx_data = data["Technical Analysis: ADX"]
            key = list(adx_data.keys())
            lastKeys = (key[0:length])
            arr = []
            for key in lastKeys:
                arr.append(float((adx_data[key]['ADX'])))

            if len(arr) < 2:
                raise ValueError("The list must have at least 2 elements.")

            slope = (arr[-1] - arr[0]) / (len(arr) - 1)

            slope = round(slope, 2)

            return slope
        except:
            print(data.keys())
            print("Incorrect key")
            return None
def grabCurrentADXONLY(symbol, month='2021-03', time_period=10, api_key="YOUR_API_KEY"):
    base_url = "https://www.alphavantage.co/query"


    params = {
        'function': 'ADX',
        'symbol': symbol,
        'interval': '1min',
        'month': month,
        'time_period': time_period,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            adx_data = data["Technical Analysis: ADX"]
            last_datapoint = adx_data[list(adx_data.keys())[-1]]
            return last_datapoint
        except:
            print(data.keys())
            print("Incorrect key")
            return None
def GrabCurrentADX(adx_data):
    last_datapoint = adx_data[list(adx_data.keys())[-1]]
    return last_datapoint 