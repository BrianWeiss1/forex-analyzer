# # import quandl

# # quandl.ApiConfig.api_key = "AGvv7E67_4d4cntuufrt"

# # data = quandl.get("FRED/DEXUSEU", start_date="2001-01-01", end_date="2001-01-02", data_frequency="1m")
# # print(data)


# import tickdata

# # Create a connection to the TickData API.
# conn = tickdata.connect("YOUR_API_KEY")

# # Request the historical data for the EURUSD pair from January 2001 to January 2005.
# data = conn.get_historical_data("EURUSD", "2001-01-01", "2005-01-01", "1m")

# # Print the data.
# for row in data:
#     print(row)

import requests
import pandas as pd
API_KEY = 'YOUR_API_KEY'
start_date = '2001-01-01'
end_date = '2001-02-28'
pair = 'EURUSD'
time_frame = 'M1'

url = 'https://api.tickdata.com/v1/historical/{}/{}/{}/{}'.format(
    time_frame, pair, start_date, end_date
)

headers = {'X-API-Key': API_KEY}

response = requests.get(url, headers=headers)

data = response.content.decode('utf-8')

print(data)



