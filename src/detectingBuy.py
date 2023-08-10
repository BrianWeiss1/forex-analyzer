try:
    import yfinance as yf
    import requests
    import pandas as pd
    from datetime import datetime, timedelta
    import time
    import pyautogui

    buy = 1118, 387
    sell = 1123, 462
    def checkTime(lastMin = -1):
        if lastMin == datetime.now().minute:
            return False
        lastMin = datetime.now().minute
        if (datetime.now().second >= 1 and datetime.now().second <= 2):
            return True
        else:
            return False
    def grabData(forexSymbol):
        forex_data_minute = yf.download(f'{forexSymbol}=X', period='m', interval='1m')
        values = {}
        values['Low'] = forex_data_minute['Low']
        values['Close'] = forex_data_minute['Close']
        values['High'] = forex_data_minute['High']
        return values
    
    def get_rsi_data(symbol, api_key, rsi_period=14):
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
    def get_SMA(closedValues):
        close_prices = closedValues
        # Calculate the Simple Moving Average (SMA)
        sma_period = 14  # Adjust the period as needed
        sma = close_prices.rolling(window=sma_period).mean()
        return sma

    def get_stochastic_oscillator(api_key, forex_symbol, k_period=24, d_period=3, smoothing_period=3):
        base_url = "https://www.alphavantage.co/query"
        
        # Request parameters
        params = {
            "function": "STOCH",
            "symbol": forex_symbol,
            "interval": "1min",
            "apikey": api_key,
            "fastkperiod": k_period,
            "slowkperiod": d_period,
            # "slowdperiod": smoothing_period
        }
        
        # Make the API request
        response = requests.get(base_url, params=params)
        data = response.json()
        
        # Extract %K and %D values
        percentk_values = data["Technical Analysis: STOCH"]

        # print(percentk_values)
        last_date = list(percentk_values.keys())[0]
        print(percentk_values[last_date])
        # print(last_date)
        last_percentk = percentk_values[last_date]["SlowK"]
        last_percentd = percentk_values[last_date]["SlowD"]
        
        return float(last_percentk), float(last_percentd)
    def compareGetStoch(kValue, dValue, pointOfError):
        specialPointOfError = 10
        def findBuy(kValue, dValue):
            if kValue < dValue and kValue+pointOfError < dValue and kValue < 20 and dValue < 20:
                return True
            else:
                if (kValue+specialPointOfError < dValue):
                    return True
                # elif (RSIVeryPos() and kValue+5 < dValue):
                #     return True
                else:
                    return False
            
        def findSell(kValue, dValue):
            if kValue > dValue and kValue > dValue+pointOfError and kValue > 80 and dValue < 80:
                return True
            else:
                if (kValue > dValue+specialPointOfError):
                    return True
                else:
                    return False
        signals = {}
        signals['buy'] = findBuy(kValue, dValue)
        signals['sell'] = findSell(kValue, dValue)
        return signals
    def automaticBuy():
        pyautogui.click(buy)
    def automaticSell():
        pyautogui.click(sell)

    if __name__ == "__main__":
        symbol = 'AUDCHF'
        infoSTOCH = {}
        while True:
            if checkTime() == True:
                print(datetime.now())
                now = datetime.now()
                infoSTOCH['%k'], infoSTOCH['%d'] = get_stochastic_oscillator((r'api_key.txt')[0], symbol)
                print("%K:" + str(infoSTOCH['%k']))
                print("%D:" + str(infoSTOCH['%d']))
                pointOfError = 5
                stochSignals = compareGetStoch(infoSTOCH['%k'], infoSTOCH['%d'], pointOfError)
                lst = []
                if (stochSignals['buy']):
                    print('Buy: ' + str(now))
                    automaticBuy()
                    lst.append(now)

                if (stochSignals['sell']):
                    print('Sell ' + str(now))
                    automaticSell()
                    lst.append(now)
                    
except KeyboardInterrupt:
    print(lst)