import requests

from src.functions.specialFunctions import automaticBuy, automaticSell

def RSI(symbol, rsi_period=3, api_key="AH1AA678VJ1UI7LD"):
    base_url = "https://www.alphavantage.co/query"

    params = {
        "function": "RSI",
        "symbol": symbol,
        "interval": "1min",
        "time_period": rsi_period,
        "series_type": "close",
        "apikey": api_key,
        "outputsize": 'full',
    }
    

    response = requests.get(base_url, params=params)
    data = response.json()
    try:
        rsi_data = data["Technical Analysis: RSI"]
        # print(rsi_data)
        return rsi_data
    except:
        print(data)
        print(data.keys())
    #removed some data here IF RSI doesnt work add it back


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


def findCandleNumber(current, number=5):
    lst = []
    if current[">67"] >= number:
        checkNextCandle = 1
        lst.append(1)
    if current["<67"] >= number:
        checkNextCandle = 2
        lst.append(2)
    if current[">37"] >= number:
        checkNextCandle = 3
        lst.append(3)
    if current["<37"] >= number:
        checkNextCandle = 4
        lst.append(4)
    else:
        checkNextCandle = 0
    return checkNextCandle, lst


def obtainResult(lst, RSIvalue, current):
    lst2 = []
    for checkNextCandle in lst:
        if checkNextCandle == 1:
            if RSIvalue < 67:
                current[">67"] = 0
                # return "BUY" # with: 56%
        if int(checkNextCandle) == 2:
            if RSIvalue > 67:
                current["<67"] = 0
                lst2.append("BUY")
                # return "BUY" #59%
        if int(checkNextCandle) == 3:
            if RSIvalue < 37:
                current[">37"] = 0
                lst2.append("SELL")
                # return "SELL"
        if checkNextCandle == 4:
            if RSIvalue > 37:
                current["<37"] = 0
                # lst2.append("BUY")
                # return "BUY"
    if lst2 == []:
        return None
    return lst2


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