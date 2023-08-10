import requests
from datetime import datetime, timedelta

api_key = 'YOUR_API_KEY' # You don't need an API key for AlphaVantage
currency_pair = 'EURUSD' 
end_time = datetime.utcnow() - timedelta(minutes=1)
start_time = end_time - timedelta(minutes=55) # grabs data from 55 minutes ago till now

# Convert timestamps to UNIX timestamps (poch time)
end_timestamp = int(end_time.timestamp())
start_timestamp = int(start_time.timestamp())

# Endpoint for the intraday forex data
endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={currency_pair}&interval=1min&apikey={api_key}&outputsize=full'

# Send a GET request to the API
response = requests.get(endpoint)

if response.status_code == 200:
    try:
        data = response.json()

        # Extract the most recent data point
        prices = {}
        prices['low'] = []
        prices['open'] = []
        prices['high'] = []
        prices['close'] = []
        latest_timestamp = max(data['Time Series (1min)'].keys())
        for value in data['Time Series (1min)'].values():
            # print(value)
            prices['low'].append(value['3. low'])
            prices['open'].append(value['1. open'])
            prices['high'].append(value['2. high'])
            prices['close'].append(value['4. close'])
        print(prices)
        valuesList = list(data['Time Series (1min)'].values())
        # print(valuesList)
        latest_data = data['Time Series (1min)'][latest_timestamp]

        # Print the most recent data with more decimal places
        print(f"Timestamp: {latest_timestamp}")
        print(f"Open: {float(latest_data['1. open'])}")
        print(f"High: {float(latest_data['2. high'])}") 
        print(f"Low: {float(latest_data['3. low'])}")   
        print(f"Close: {float(latest_data['4. close'])}") 
    except KeyError:
        print(data)
else:
    print('Error occurred while fetching data')
