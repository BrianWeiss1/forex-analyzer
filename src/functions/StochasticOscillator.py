import requests
def get_stochastic_oscillator(api_key, forex_symbol, k_period=24, d_period=3, smoothing_period=3):
    base_url = "https://www.alphavantage.co/query"
    
    # Request parameters
    params = {
        "function": "STOCH",
        "symbol": forex_symbol,
        "interval": "daily",
        "apikey": api_key,
        "fastkperiod": k_period,
        "slowkperiod": d_period,
        "slowdperiod": smoothing_period
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract %K and %D values
    percentk_values = data["Technical Analysis: STOCH"]
    last_date = list(percentk_values.keys())[0]
    last_percentk = percentk_values[last_date]["SlowK"]
    last_percentd = percentk_values[last_date]["SlowD"]
    
    return float(last_percentk), float(last_percentd)

# Replace with your Alpha Vantage API key
# api_key = (r'api_key.txt')[0]
api_key = 'd3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc3'

# Replace with the forex symbol and the desired periods
forex_symbol = "AUDUSD"

percentk, percentd = get_stochastic_oscillator(api_key, forex_symbol)
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