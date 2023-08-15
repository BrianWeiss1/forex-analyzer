

from decimal import Decimal
from src.functions.AMX import ADX
from src.functions.GrabData import GrabCloseData
from src.functions.RSI import RSI, checkPusdo, findCandleNumber, obtainResult

symbol = "AUDCAD"
symbol = "EURUSD"
symbol = "XAU"
month = '2023-02'
def calculate_supremeRSIaverage(RSIvalues, AMXlist, dataPoints, time, amountOfCandles, ADXlow, ADXhigh):

    checkNextCandle = 0
    NextCandle = None
    current = {}
    pos = 0
    neg = 0
    neu = 0
    for i in range(len(list(AMXlist))-1, 0, -1):
        # Go through, 
        if NextCandle == True or NextCandle == False:
            if NextCandle == True:
                now = dataPoints[i+1]
                previous = dataPoints[i+2]
                if Decimal(dataPoints[i+1]) > Decimal(dataPoints[i+2]):
                    pos += 1
                elif dataPoints[i+1] == dataPoints[i+2]:
                    neu += 1
                else:
                    neg += 1
                NextCandle = None
            else:
                now = dataPoints[i+1]
                previous = dataPoints[i+2]
                if dataPoints[i+1] < dataPoints[i+2]:
                    pos += 1
                elif dataPoints[i+1] == dataPoints[i+2]:
                    neu += 1
                else:
                    neg += 1
                NextCandle = None
        RSIvalue = float(RSIvalues[time[i]]['RSI'])
        signal = obtainResult(checkNextCandle, RSIvalue, current) # check 1 data BUY
        checkPusdo(current, RSIvalue) # check 1 data
        checkNextCandle = findCandleNumber(current, amountOfCandles) # solves for candle
        AMXvalue = AMXlist[time[i]]['ADX']
        if signal == "BUY":
            if AMXvalue > ADXlow and AMXvalue < ADXhigh:
                NextCandle = True
        if signal == "SELL":
            if AMXvalue > ADXlow and AMXvalue < ADXhigh:
                NextCandle = False
    return pos, neu, neg


# while True:
#     current = checkPusdo(current, RSIvalue) # check 1 data
#     signal = obtainResult(checkNextCandle, RSIvalue) # check 1 data
#     if signal == "BUY":
#         automaticBuy()
#     if signal == "SELL":
#         automaticSell()
#     checkNextCandle = findCandleNumber(current, number)
#     break
# EURJPY 0% GBPJPY 0%
#USDCNH 1.17%
# 'USDCNH', 'EURJPY', 
prevouisBestPercent = 100
symbols = ['EURJPY', 'USDCNH', 'GBPJPY', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDUSD', 'CADCHF', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURGBP', 'EURUSD', 'GBPAUD', 'GDPCAD', 'GDPCHF', 'GDPUSD', 'USDCHF', 'USDJPY', 'EURCHF', 'CADJPY', 'USDCAD']
symbolsBest = ['EURJPY', 'GBPJPY', 'AUDJPY', 'CHFJPY', 'USDJPY', 'CADJPY']
symbolsSorted = ['USDJPY', 'CADJPY', 'GBPJPY', 'CHFJPY', 'EURJPY', 'AUDJPY']
symbolsSorted2 = ['USDJPY', 'CADJPY', 'GBPJPY', 'CHFJPY', 'EURJPY', 'AUDJPY']
symbolsSorted3 = ['USDJPY', 'CADJPY', 'GBPJPY', 'CHFJPY', 'EURJPY', 'AUDJPY']
stocks = ['APPL']
for symbol in stocks:
    closeData, time2 = GrabCloseData(symbol, month)
    current = {}
    checkNextCandle = 0
    RSIvalues = RSI(symbol, month)
    AMXlist = ADX(symbol, month)
    pos, neu, neg = calculate_supremeRSIaverage(RSIvalues, AMXlist, closeData, time2, 5)
    print(symbol)
    print("Candles: " + str(len(RSIvalues)))
    print("Total Trades: " + str(pos+neg+neu))
    print("Positive Trades: " + str(pos))
    print("Neutrol Trades: " + str(neu))
    print("Negitive Trades: " + str(neg))
    if not pos == 0:
        nuetPercent = round((neu/(pos+neg+neu))*100, 2)
        if nuetPercent < prevouisBestPercent:
            prevouisBestPercent = nuetPercent
            prevouisBestSymbol = symbol
        print("Trade %: " + str(round((Decimal(pos+neg+neu)/Decimal(len(RSIvalues))*100), 2)) + "%")
        print("Trade %: " + str(round((Decimal(pos+neg+neu)/Decimal(len(RSIvalues))*100), 2)) + "%")
        print("Trade %: " + str(round((Decimal(pos+neg+neu)/Decimal(len(RSIvalues))*100), 2)) + "%")

        print("Neut %: " + str(nuetPercent) + "%")
        print("Win %: " + str((pos/(neg+pos))*100) + "%")
    print("\n\n\n\n")