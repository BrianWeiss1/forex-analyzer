
from functions.GrabData import GrabCloseData
from functions.STOCHredo import STOCH, checkPusdo, findCandleNumber, obtainResult
from decimal import Decimal

def solveForAverageSTOCH(percentKandD, dataPoints, closeDatatime):
    pos = 0
    neu = 0
    neg = 0
    number = 5
    current = {}
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

symbol = "USDJPY"
month = "2019-07"
listOfKD = STOCH(symbol, month)
closeData, closeDatatime = GrabCloseData(symbol, month)
solveForAverageSTOCH(listOfKD, closeDatatime)