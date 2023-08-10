import requests

def RSI(symbol, api_key, rsi_period=14):
    base_url = "https://www.alphavantage.co/query"
    outputsize = "compact"

    params = {
        "function": 'RSI',
        "symbol": symbol,
        "interval": "1min",
        "time_period": rsi_period,
        "series_type": "close",
        "apikey": api_key,
        "outputsize": outputsize
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "Technical Analysis: RSI" in data:
        rsi_values = []
        for timestamp, rsi_info in data["Technical Analysis: RSI"].items():
            rsi_values.append(float(rsi_info["RSI"]))

        return rsi_values

    return None

def findRSIslope(rsi_values, time_frame):
    total = 0
    for each in rsi_values[0:time_frame]:
        total += each
    return total/time_frame-rsi_values[0]