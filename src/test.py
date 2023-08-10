# import yfinance as yf
# import pandas_datareader as pdr
# import datetime
# import decimal
# decimal.getcontext().prec = 10

# # Set the forex symbol and the start/end dates for the data
# forexSymbol = "EURUSD=X"

# #SETUP
# def SMA(data, period):
#     sma_values = []
    
#     for i in range(period - 1, len(data)):
#         sma = sum(data[i - period + 1:i + 1]) / period
#         sma_values.append(sma)
    
#     return sma_values
# def grabData(forexSymbol):
#     forex_data_minute = (yf.download(f'{forexSymbol}=X', period='m', interval='1m'))
#     forex_data_minute = list(forex_data_minute)
#     values = {}
#     # for i in range(forex_data_minute):
#     values['Low'] = forex_data_minute['Low']
#     values['Close'] = forex_data_minute['Close']
#     values['High'] = forex_data_minute['High']
#     return values
# #WORKING ON FUCTIONS
# def getArrayOfKs(closingPrices, Kperiod):
#     listK = []
#     print(closingPrices)
#     print(len(closingPrices))
#     for i in range(len(closingPrices)):
#         check = []
#         for i in range(len(closingPrices)-Kperiod-i, len(closingPrices)-i):
#             check.append(closingPrices[i])
        
#         # print(check)
#         print(get_k(check))
#         listK.append(get_k(check))
#     return listK
# def get_k(closingKperiod):
#     round1 = closingKperiod[0] - min(closingKperiod)
#     round2 = max(closingKperiod) - min(closingKperiod)
#     currentK = (round1/round2)*100
#     return (currentK)  

# def findcurrentSTOCH(closingPrices, Kperiod, Dperiod):
#     closingKperiod = closingPrices[0:Kperiod]

#     round1 = closingKperiod[0] - min(closingKperiod)
#     round2 = max(closingKperiod) - min(closingKperiod)
#     currentK = (round1/round2)*100
#     print(currentK)
#     D = SMA(currentK, Dperiod)

# import pandas as pd
# import numpy as np

# def calculate_KD_lines(df, kperiods=14, dperiods=3):
#     """
#     Calculate %K and %D lines using given CSV data.

#     Parameters:
#     - csv_file_path (str): Path to the CSV file containing necessary data.
#     - kperiods (int, optional): Number of periods for %K calculations. Default is 14.
#     - dperiods (int, optional): Number of periods for %D calculations. Default is 3.

#     Returns:
#     - Kvalue (list): List of %K line values.
#     - Dvalue (list): List of %D line values.
#     """    # Extract data arrays

#     array_close = np.array(df['Close'])
#     array_low = np.array(df['Low'])
#     array_high = np.array(df['High'])

#     # Calculate Highest and Lowest values within kperiods
#     array_highest = [max(array_high[i:i+kperiods]) for i in range(len(array_high) - kperiods + 1)]
#     array_lowest = [min(array_low[i:i+kperiods]) for i in range(len(array_low) - kperiods + 1)]

#     # Calculate %K Line Values
#     Kvalue = [((array_close[x] - array_lowest[x - kperiods]) * 100) / (array_highest[x - kperiods] - array_lowest[x - kperiods])
#               for x in range(kperiods, len(array_close))]

#     # Calculate %D Line Values
#     Dvalue = [None, None]
#     for x in range(len(Kvalue) - dperiods + 1):
#         mean = sum(Kvalue[x: x + dperiods]) / dperiods
#         mean = 100-mean
#         Dvalue.append(mean)
#     # for each in Kvalue:
#     #     each = 100-each
#     return Kvalue, Dvalue

# # Example usage
# symbol = 'AUDNZD'
# a = grabData(symbol), 4
# b = grabData(symbol), 4
# print(a)
# print(b)
# # Kvalue, Dvalue = calculate_KD_lines(grabData(symbol), 4)
# # print("Length of Kvalue:", len(Kvalue))
# # print(Kvalue)
# # print("Length of Dvalue:", len(Dvalue))
# # print(Dvalue)
# # symbol = 'EURJPY'
# # dataPoints = grabData(symbol)['Close']
# # print(getArrayOfKs(dataPoints, 4))\

