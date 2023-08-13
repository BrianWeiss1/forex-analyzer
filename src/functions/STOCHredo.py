import requests

def STOCH(symbol, month='2021-03', fastkperiod=5, slowkperiod=3, slowdperiod=3, api_key="YOUR_API_KEY"):
    base_url = "https://www.alphavantage.co/query"

    params = {
        'function': 'STOCH',
        'symbol': symbol,
        'interval': '1min',
        'month': month,
        'fastkperiod': fastkperiod,
        'slowkperiod': slowkperiod,
        'slowdperiod': slowdperiod,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    data = response.json()
    try:
        percentKandD = data['Technical Analysis: STOCH']
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


def findCandleNumber(current, number=5):
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
                return "SELL"
        if checkNextCandle == 2:
            if percentK > percentD:
                current["<percentD"] = 0
                return "BUY"
        # if int(checkNextCandle) == 3:
        #     if RSIvalue < percentK:
        #         current[">percentK"] = 0
        #         return "SELL"
        # if checkNextCandle == 4:
        #     if RSIvalue > percentK:
        #         current["<percentK"] = 0
        #         return "BUY"
    return None


def main():
    symbol = input("what is the symbol of your pair?")
    stochlist = STOCH(symbol)
