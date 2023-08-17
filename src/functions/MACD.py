import requests

# Get your API key from https://twelvedata.com/apikey
api_key = "your_api_key"

# Define the URL for the MACD data endpoint
url = "https://api.twelvedata.com/technical_indicators/macd"

# Define the parameters for the request
params = {
    "symbol": "AAPL",
    "interval": "1d",
    "fast_period": 12,
    "slow_period": 26,
    "signal_period": 9,
}

# Make the request
response = requests.get(url, params=params, headers={"Authorization": f"Bearer {api_key}"})

# Check the response status code
if response.status_code == 200:
    # The request was successful, get the MACD data
    macd_data = response.json()
else:
    # The request failed, print the error message
    print(response.status_code, response.text)

# Print the MACD data
print(macd_data)