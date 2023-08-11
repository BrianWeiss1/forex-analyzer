import requests
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
        "slowdperiod": smoothing_period
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract %K and %D values
    try:
        percentk_values = data["Technical Analysis: STOCH"]
        last_date = list(percentk_values.keys())[0]
        # print(last_percentk)
        last_percentk = percentk_values[last_date]["SlowK"]
        last_percentd = percentk_values[last_date]["SlowD"]
        print(last_date)
        return float(last_percentk), float(last_percentd)
    except:
        print(data)
        
    return float(last_percentk), float(last_percentd)

def compareGetStoch(kValue, dValue, pointOfError):
    specialPointOfError = 5
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
def get_list_solastic(forex_symbol, k_period=5, d_period=3, smoothing_period=3, api_key='d3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9'):
    base_url = "https://www.alphavantage.co/query"
    
    # Request parameters
    params = {
        'month': '2009-01',
        "function": "STOCH",
        "symbol": forex_symbol,
        "interval": "1min",
        "apikey": api_key,
        "fastkperiod": k_period,
        "slowkperiod": d_period,
        "slowdperiod": smoothing_period
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract %K and %D values
    try:
        percentk_values = data["Technical Analysis: STOCH"]
        return percentk_values
    except:
        print(data)

        
    # return float(last_percentk), float(last_percentd)
# symbol = 'AUDCHF'
# get_list_solastic('d3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9', symbol)