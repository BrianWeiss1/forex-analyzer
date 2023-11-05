import requests, json

apiSymbols = requests.get('https://api.binance.com/api/v3/exchangeInfo')
jsonApiSymbols = json.loads(apiSymbols.text)
jsonSymbols = jsonApiSymbols['symbols']

quoteAssets = {"BTC", "USDT"}
binStr = 'BINANCE:'
resList = []
res = ''

def createSpotList():
    global resList
    for symbol in jsonSymbols:
        symbolStatus = symbol['status']
        if symbolStatus == 'TRADING':
            if symbol['quoteAsset'] in quoteAssets and symbol['isSpotTradingAllowed'] == True:
                sym = symbol['symbol']
                resList.append(sym)

def createFutureList():
    global resList
    for symbol in jsonSymbols:
        symbolStatus = symbol['status']
        if symbolStatus == 'TRADING':
            if symbol['quoteAsset'] in quoteAssets and symbol['isMarginTradingAllowed'] == True:
                sym = symbol['symbol']
                resList.append(sym)

# user interaction
print('Binance symbol creation tool')
userSelect = input("Select: spot (s), future (f) or all (a) symbols: ")
print("Selection: " + userSelect)

if userSelect == 's':
    createSpotList()
elif userSelect == 'f':
    createFutureList()
elif userSelect == 'a':
    createSpotList()
    createFutureList()

# filter duplicates from list
resList = list(dict.fromkeys(resList))

# crete string from list
for item in resList:
    if res == '':
        res = res + binStr + item
    else:
        res = res + ',' + binStr + item

# # write result var in new file
filename = 'BinanceSymbols.txt'
new_file = open(filename, "w")
new_file.write(res)

print('BinanceSymbols.txt created with ' + str(len(resList)) + ' items.')
new_file.close()

# Initialize an empty list to store the extracted symbols
symbols = []

# Open the file for reading
with open('BinanceSymbols.txt', 'r') as file:
    # Read the first (and only) line from the file
    line = file.readline()
    
    # Split the line using ',' as the delimiter
    parts = line.split(',')
    
    # Iterate through the parts and process each one
    for part in parts:
        # Extract the symbol part and remove 'BTC' or 'USDT'
        symbol = part.replace('BINANCE:', '')
        if 'BTC' in symbol:
            symbol = symbol.replace('BTC', '')
        elif 'USDT' in symbol:
            symbol = symbol.replace('USDT', '')
        # Append the cleaned symbol to the list
        symbols.append(symbol + "USDT")

# Print the extracted symbols as an array
# print(symbols)
# print(len(symbols))

from collections import OrderedDict

# Remove duplicates while preserving order
symbols = list(OrderedDict.fromkeys(symbols))

# print(len(symbols))
filename = 'BinanceSymbols.txt'
new_file = open(filename, "w")
new_file.write(str(symbols))

print('BinanceSymbols.txt created with ' + str(len(symbols)) + ' items.')
new_file.close()