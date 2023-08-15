import requests

def STOCH(symbol, fastkperiod=5, slowkperiod=3, slowdperiod=3, api_key="YOUR_API_KEY"):
    base_url = "https://www.alphavantage.co/query"

    params = {
        'function': 'STOCH',
        'symbol': symbol,
        'interval': '1min',
        'fastkperiod': fastkperiod,
        'slowkperiod': slowkperiod,
        'slowdperiod': slowdperiod,
        'apikey': api_key,
        "outputsize": 'full'
    }

    response = requests.get(base_url, params=params)

    data = response.json()
    try:
        percentKandD = data['Technical Analysis: STOCH']
        print(data.keys())
        return percentKandD
    except KeyError:
        print(data)
        print(data.keys())

def checkPusdo(current, percentK, percentD):
    if percentK < percentD:
        if current.get("<percentD") == 0 or current.get("<percentD") == None:
            current["<percentD"] = 1
        else:
            current["<percentD"] += 1
    else:
        current["<percentD"] = 0
    if percentK > percentD:
        if current.get(">percentD") == 0 or current.get(">percentD") == None:
            current[">percentD"] = 1
        else:
            current[">percentD"] += 1
    else:
        current[">percentD"] = 0
    return current


def findCandleNumber(current, number=1):
    if current[">percentD"] >= number:
        checkNextCandle = 1
    elif current["<percentD"] >= number:
        checkNextCandle = 2
    else:
        checkNextCandle = 0
    return checkNextCandle


def obtainResult(checkNextCandle, current, percentK, percentD):
    if checkNextCandle > 0:
        if checkNextCandle == 1:
            if percentK < percentD:
                current[">percentD"] = 0
                difference = abs(percentK-percentD)
                return "SELL", difference
        if checkNextCandle == 2:
            if percentK > percentD:
                current["<percentD"] = 0
                difference = abs(percentK-percentD)
                return "BUY", difference
        # if int(checkNextCandle) == 3:
        #     if RSIvalue < percentK:
        #         current[">percentK"] = 0
        #         return "SELL"
        # if checkNextCandle == 4:
        #     if RSIvalue > percentK:
        #         current["<percentK"] = 0
        #         return "BUY"
    return None, 0


def main():
    symbol = input("what is the symbol of your pair?")
    stochlist = STOCH(symbol)
