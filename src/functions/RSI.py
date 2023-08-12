import requests

from src.functions.specialFunctions import automaticBuy, automaticSell

def RSI(symbol, api_key="YOUR_API_KEY", rsi_period=3):
    base_url = "https://www.alphavantage.co/query"

    params = {
        "function": "RSI",
        "symbol": symbol,
        "interval": "1min",
        "time_period": rsi_period,
        "series_type": "close",
        "apikey": api_key,
        'month': '2009-02',
        "outputsize": 'full',
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

    return total / time_frame - rsi_values[0]


def simpleCheckRSI(RSIinput):
    if RSIinput < 30:
        return "Sell"
    elif RSIinput > 70:
        return "Buy"


# print(RSI("AAPL")[-1])


# Must have buying time at 5min
"""
-Make RSI period 3 :)
-if crosses from bottom to 35, buy, if crosses under 35, sell

If crosses over 65, buy, if crosses under 65, sell


Make it 37 and 63
"""


def checkPusdo(current, RSI):
    if RSI < 37:
        if current.get("<37") == 0 or current.get("<37") == None:
            current["<37"] = 1
        else:
            current["<37"] += 1
    else:
        current["<37"] = 0
    if RSI > 37:
        if current.get(">37") == 0 or current.get(">37") == None:
            current[">37"] = 1
        else:
            current[">37"] += 1
    else:
        current[">37"] = 0
    if RSI < 67:
        if current.get("<67") == 0 or current.get("<67") == None:
            current["<67"] = 1
        else:
            current["<67"] += 1
    else:
        current["<67"] = 0
    if RSI > 67:
        if current.get(">67") == 0 or current.get(">67") == None:
            current[">67"] = 1
        else:
            current[">67"] += 1
    else:
        current[">67"] = 0
    return current


def findCandleNumber(current, number):
    if current[">67"] >= number:
        checkNextCandle = 1
    elif current["<67"] >= number:
        checkNextCandle = 2
    elif current[">37"] >= number:
        checkNextCandle = 3
    elif current["<37"] >= number:
        checkNextCandle = 4
    else:
        checkNextCandle = 0
    return checkNextCandle


def obtainResult(checkNextCandle, RSIvalue):
    if checkNextCandle > 0:
        if checkNextCandle == 1:
            if RSIvalue < 67:
                return "SELL"
        if checkNextCandle == 2:
            if RSIvalue > 67:
                return "BUY"
        if checkNextCandle == 3:
            if RSIvalue < 37:
                return "SELL"
        if checkNextCandle == 4:
            if RSIvalue > 37:
                return "BUY"
    return None


# if (last 5 candles < 37 and now >=37):
#     Buy
# elif (last 5 candles > 37 and now <= 37):
#     Sell
# if (last 2 candles < 67 and now >= 67):
#     Buy
# elif (last 2 candles > 67 and now < 67):
#     Sell


def main(symbol, number):
    symbol = "AAPL"
    current = {}
    checkNextCandle = 0
    while True:
        RSIvalue = RSI(symbol)[-1]
        current = checkPusdo(current, RSIvalue)
        signal = obtainResult(checkNextCandle, RSIvalue)
        if signal == "BUY":
            automaticBuy()
        if signal == "SELL":
            automaticSell()
        checkNextCandle = findCandleNumber(current, number)