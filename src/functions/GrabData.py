import requests
from datetime import datetime, timedelta
import yfinance as yf
#AlphaVantage
def GrabData(symbol, api_key='YOUR_API_KEY'):
    end_time = datetime.utcnow() - timedelta(minutes=1)
    start_time = end_time - timedelta(minutes=55) # grabs data from 55 minutes ago till now
    endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}&outputsize=full'

    # Send a GET request to the API
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()

        # Extract the most recent data point
        prices = {}
        prices['low'] = []
        prices['open'] = []
        prices['high'] = []
        prices['Close'] = []
        latest_timestamp = max(data['Time Series (1min)'].keys())
        for value in data['Time Series (1min)'].values():
            prices['low'].append(float(value['3. low']))
            prices['open'].append(float(value['1. open']))
            prices['high'].append(float(value['2. high']))
            prices['Close'].append(float(value['4. close']))
        
        latest_data = data['Time Series (1min)'][latest_timestamp]

        # Print the most recent data with more decimal places
        print(f"Timestamp: {latest_timestamp}")
        print(f"Open: {float(latest_data['1. open'])}")
        print(f"High: {float(latest_data['2. high'])}") 
        print(f"Low: {float(latest_data['3. low'])}")   
        print(f"Close: {float(latest_data['4. close'])}") 
        return prices
    else:
        print('Error occurred while fetching data')
#YahooFinance
def grabData(forexSymbol):
    forex_data_minute = yf.download(f'{forexSymbol}=X', period='m', interval='1m')
    values = {}
    values['Low'] = forex_data_minute['Low']
    values['Close'] = forex_data_minute['Close']
    values['High'] = forex_data_minute['High']
    return values
