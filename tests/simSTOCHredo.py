
from src.functions.GrabData import GrabCloseData
from src.functions.STOCHredo import STOCH, checkPusdo, findCandleNumber, obtainResult
from decimal import Decimal
import time
# 1 is at 80.06674757281553%
def solveForAverageSTOCH(percentKandD, dataPoints, closeDatatime, kValue, dValue, smoothing_value):
    pos = 0
    neu = 0
    neg = 0
    number = 1
    current = {}
    nextCandle = None
    checkNextCandle = 0
    for i in range(len(list(percentKandD))-1, 0, -1):
        if nextCandle == True:
            if Decimal(dataPoints[i+1]) > Decimal(dataPoints[i+2]):
                pos += 1
            elif dataPoints[i+1] == dataPoints[i+2]:
                neu += 1
            else:
                neg += 1
            nextCandle = None
        if nextCandle == False:
            if Decimal(dataPoints[i+1]) < Decimal(dataPoints[i+2]):
                pos += 1
            elif dataPoints[i+1] == dataPoints[i+2]:
                neu += 1
            else:
                neg += 1
            nextCandle = None
        percentK = float(percentKandD[closeDatatime[i]]['SlowK'])
        percentD = float(percentKandD[closeDatatime[i]]['SlowD'])
        signal = obtainResult(checkNextCandle, current, percentK, percentD) # check 1 data BUY
        checkPusdo(current, percentK, percentD) # check 1 data
        checkNextCandle = findCandleNumber(current, number) # solves for candle   
        if signal == "BUY":
            nextCandle = True
        elif signal == 'SELL':
            nextCandle = False     

    return pos, neu, neg

symbol = "AAPL"
month = "2019-07"
closeData, closeDatatime = GrabCloseData(symbol, month)
bestWinPercent = 0
besti = 0
bestj = 0
bestk = 0
try:
    for i in range(1, (100)):
        print(i)
        for j in range(1, (10)):
            for k in range(1, 10):
                try:
                    listOfKD = STOCH(symbol, month, i, j, k)
                    pos, neu, neg = (solveForAverageSTOCH(listOfKD, closeData, closeDatatime, 1, 1, 1))
                except:
                    print("eror")
                    time.sleep(61)
                    listOfKD = STOCH(symbol, month, i, j, k)
                    pos, neu, neg = (solveForAverageSTOCH(listOfKD, closeData, closeDatatime, 1, 1, 1))
                    # yautogui
                    # openVPN()
                    # chooseOption()
                print("Candles: " + str(len(listOfKD)))
                print("Total Trades: " + str(pos+neg+neu))
                print("Positive Trades: " + str(pos))
                print("Neutrol Trades: " + str(neu))
                print("Negitive Trades: " + str(neg))
                print("Trade %: " + str(round((Decimal(pos+neg+neu)/Decimal(len(listOfKD))*100), 2)) + "%")
                if neg+pos == 0 or pos == 0:
                    print("Diison by 0")
                else:
                    nuetPercent = round((neu/(pos+neg+neu))*100, 2)
                    print("Neut %: " + str(nuetPercent) + "%")

                    winPercent = (pos/(neg+pos))*100
                    print("Win %: " + str(round((pos/(neg+pos))*100, 2)) + "%")
                    if winPercent > bestWinPercent:
                        bestWinPercent = winPercent
                        besti = i
                        bestj = j
                        bestk = k
    print(bestWinPercent)
    print(besti)
    print(bestj)
except KeyboardInterrupt:
    print(bestWinPercent)
    print(besti)
    print(bestj) 