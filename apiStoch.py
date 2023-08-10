import requests

def get_stochastic_oscillator(api_key, forex_symbol, k_period, d_period, smoothing_period):
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
    last_date = list(percentk_values.keys())[-1]
    last_percentk = percentk_values[last_date]["SlowK"]
    last_percentd = percentk_values[last_date]["SlowD"]
    
    return float(last_percentk), float(last_percentd)

# Replace with your Alpha Vantage API key
api_key = (r'api_key.txt')[0]

# Replace with the forex symbol and the desired periods
forex_symbol = "EURUSD"
k_period = 14
d_period = 3
smoothing_period = 3

percentk, percentd = get_stochastic_oscillator(api_key, forex_symbol, k_period, d_period, smoothing_period)
print("Last %K:", percentk)
print("Last %D:", percentd)
