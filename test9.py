# grab list of data from binance
# grab

import requests

# Replace with your Binance API key and secret
api_key = '0imfnc8mVLWwsAawjYr4RxAf50DDqtld'
api_secret = 'YOUR_API_SECRET'

import requests

# Define the API endpoint for Binance's trading pairs
api_url = "https://api.binance.com/api/v3/exchangeInfo"

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the symbol pairs against USDT or USD
    top_symbols = []
    for symbol_info in data["symbols"]:
        symbol = symbol_info["symbol"]
        if symbol_info["quoteAsset"] in ["USDT", "USD"]:
            top_symbols.append(symbol)

    # Take the top 100 symbols
    print(len(top_symbols))
    top_100_symbols = top_symbols[:100]
    f = open('documents/binanceSymbols.txt', 'w')
    f.write(str(top_symbols))
    f.close()
    # Print the top 100 symbols
    for symbol in top_100_symbols:
        print(symbol)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


