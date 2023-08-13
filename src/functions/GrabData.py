import requests
from datetime import datetime, timedelta
import yfinance as yf
#AlphaVantage
def GrabCloseData(symbol, api_key='d3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9'):
    endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}&month=2009-03&outputsize=full'
    endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&month=2020-03&outputsize=full&apikey={api_key}'



    # Send a GET request to the API
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()

        # Extract the most recent data point
        prices = {}
        times = []
        prices['low'] = []
        prices['open'] = []
        prices['high'] = []
        prices['Close'] = []
        try:
            for value in data['Time Series (1min)'].values():
                prices['low'].append(float(value['3. low']))
                prices['open'].append(float(value['1. open']))
                prices['high'].append(float(value['2. high']))
                prices['Close'].append(float(value['4. close']))
            for time in data['Time Series (1min)'].keys():
                times.append(time[:-3])
            # UpdatedTimes = times[0:len(times)-27]
            Closeprices = prices['Close']
            # UpdatedClosePrice = Closeprices[0:len(Closeprices)-27]
            # latest_data = data['Time Series (1min)'][latest_timestamp]

            # Print the most recent data with more decimal places
            # print(f"Timestamp: {latest_timestamp}")
            # print(f"Open: {float(latest_data['1. open'])}")
            # print(f"High: {float(latest_data['2. high'])}") 
            # print(f"Low: {float(latest_data['3. low'])}")   
            # print(f"Close: {float(latest_data['4. close'])}") 
            return Closeprices, times
        except:
            print(data)
            print(data.keys())
    else:
        print('Error occurred while fetching data')
def GrabAllData(symbol, api_key='YOUR_API_KEY'):
    end_time = datetime.utcnow() - timedelta(minutes=1)
    start_time = end_time - timedelta(minutes=55) # grabs data from 55 minutes ago till now
    endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}&outputsize=full'

    # Send a GET request to the API
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()

        # Extract the most recent data point
        prices = {}
        times = []
        prices['low'] = []
        prices['open'] = []
        prices['high'] = []
        prices['Close'] = []
        latest_timestamp = max(data['Time Series (1min)'].keys())
        for value in data['Time Series (1min)'].values():
            times.append(value)
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
        return prices, times
    else:
        print('Error occurred while fetching data')
#YahooFinance
def graYahooData(forexSymbol):
    forex_data_minute = yf.download(f'{forexSymbol}=X', period='m', interval='1m')
    values = {}
    values['Low'] = forex_data_minute['Low']
    values['Close'] = forex_data_minute['Close']
    values['High'] = forex_data_minute['High']
    return values