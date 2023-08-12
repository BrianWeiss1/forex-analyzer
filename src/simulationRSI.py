

from decimal import Decimal
from functions.GrabData import GrabCloseData
from functions.RSI import RSI, checkPusdo, findCandleNumber, obtainResult

symbol = "AAPL"
def calculate_supremeRSIaverage(RSIvalues, dataPoints, time, number):
    checkNextCandle = 0
    NextCandle = None
    current = {}
    pos = 0
    neg = 0
    neu = 0
    for i in range(len(list(RSIvalues))-1, 0, -1):
        # Go through, 
        if NextCandle == True or NextCandle == False:
            if NextCandle == True:
                if dataPoints[i+1] > dataPoints[i+2]:
                    pos += 1
                elif dataPoints[i+1] == dataPoints[i+2]:
                    neu += 1
                else:
                    neg += 1
                NextCandle = None
            else:
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
        checkNextCandle = findCandleNumber(current, number) # solves for candle
        # print(type(checkNextCandle))
        if signal != None:
            print(signal)
        if signal == "BUY":
            # print("a")
            NextCandle = True
        if signal == "SELL":
            NextCandle = False
    return pos, neu, neg

closeData, time2 = GrabCloseData(symbol)
current = {}
checkNextCandle = 0
RSIvalues = RSI(symbol)
# while True:
#     current = checkPusdo(current, RSIvalue) # check 1 data
#     signal = obtainResult(checkNextCandle, RSIvalue) # check 1 data
#     if signal == "BUY":
#         automaticBuy()
#     if signal == "SELL":
#         automaticSell()
#     checkNextCandle = findCandleNumber(current, number)
#     break

pos, neu, neg = calculate_supremeRSIaverage(RSIvalues, closeData, time2, 5)
print("Candles: " + str(len(RSIvalues)))
print("Total Trades: " + str(pos+neg+neu))
print("Positive Trades: " + str(pos))
print("Neutrol Trades: " + str(neu))
print("Negitive Trades: " + str(neg))
if not pos == 0:
    print("Win %: " + str((pos/(neg+pos))*100) + "%")