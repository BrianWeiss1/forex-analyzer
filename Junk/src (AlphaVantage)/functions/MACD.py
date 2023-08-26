# import requests
# import datetime

# def getMACD(symbol, interval='1min', exchange='FXCM', outputSize=1):
#     apiKeys = []
#     fapi = open('documents/TweleveData.txt', 'r')
#     for line in fapi:
#         apiKeys.append(line.strip('\n'))

#     # Get your API key from https://twelvedata.com/apikey
#     api_key = apiKeys[1]

#     # Define the URL for the MACD data endpoint
#     url = "https://api.twelvedata.com/macd"

#     # Define the parameters for the request
#     params = {
#         "symbol": "EUR/JPY",
#         "interval": "1min",
#         "fast_period": 1,
#         "slow_period": 15,
#         "signal_period": 1,
#         'outputsize': 10,
#         'apikey': api_key,
#         'start_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
#     }

#     # Make the request
#     response = requests.get(url, params=params)

#     # Check the response status code
#     if response.status_code == 200:
#         # The request was successful, get the MACD data
#         macd_data = response.json()
#         # Print the MACD data
#         macValues = macd_data['values']
#         formattedmacValues = change_format(macValues)
#         return formattedmacValues
#     else:
#         # The request failed, print the error message
#         print(response.status_code, response.text)

# def change_format(data):
#     # Create an empty dictionary
#     result = {}

#     # Iterate over the data
#     for item in data:
#         # Get the datetime
#         datetime = item['datetime']

#         # Create a dictionary for the current datetime
#         current_data = {
#             'macd': item['macd'],
#             'macd_signal': item['macd_signal'],
#             'macd_hist': item['macd_hist']
#         }

#         # Add the dictionary to the result
#         result[datetime] = current_data

#     return result

import requests
def get_MACD(symbol):
    url = f"https://api.polygon.io/v1/indicators/macd/{symbol}"
    params = {
        "timespan": "minute",
        "adjusted": "true",
        "short_window": 1,
        "long_window": 15,
        "signal_window": 1,
        "series_type": "close",
        "order": "desc",
        "limit": 1,
        "apiKey": "9DnUwrfAQpzTUzK4FIvg8PHLmbB4geVB"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        if "results" in data:
            print(data)
            macd_data = data["results"]['values'][len(data["results"]['values'])-1]['value']
            return macd_data
        else:
            print("No MACD data found.")
    else:
        print("Failed to fetch data. Status code:", response.status_code)
    return None


# def grabSignal(symbol):
#     data = get_MACD(symbol)
if __name__ == '__main__':
    data = get_MACD('C:EURJPY')
    print(data)



