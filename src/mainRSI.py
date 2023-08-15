

from functions.GrabData import GrabCurrentData
from functions.RSI import RSI, checkPusdo, findCandleNumber, obtainResult
from functions.specialFunctions import automaticBuy, automaticSell, checkTime, obtainCurrentTime, obtainPastTimeFormatted
from datetime import datetime
import time

def main(symbol, number):
    timer = -1
    current = {}
    current[">67"] = 0
    current["<67"] = 0
    current["<37"] = 0
    current[">37"] = 0
    checkNextCandle = 0
    bol = False
    previousBuy = previousSell = False
    pos = neg = nuet = 0
    sumPos = sumNeut = sumNeg = 0
    difference = 0
    while (True):
        if (datetime.now().second >= 1 and datetime.now().second <= 2 and not datetime.now().minute == timer):
            bol, timer = checkTime(timer)
            bol = True
        if bol == True:
            if previousBuy == True or previousSell == True:
                dataClose = GrabCurrentData(symbol)
                f = open('documents/data.txt', 'w')
                f.write(str(dataClose))
                previousPrice = dataClose[obtainPastTimeFormatted(2)]['4. close']
                currentPrice = dataClose[(obtainPastTimeFormatted(1))]['4. close']
                print("previously" + str(previousPrice))
                print("currently: " + str(currentPrice))
                if previousBuy:
                    if previousPrice < currentPrice:
                        print("BOT GO BRRRRRRR")
                        pos+=1
                        sumPos += difference
                    elif previousPrice == currentPrice:
                        print("BOT GORRRRRRRR")
                        nuet+=1
                        sumNeut += difference
                    else:
                        print("BOT GRRRRRRRRRRRR")
                        neg+=1
                        sumNeg += difference
                if previousSell:
                    if previousPrice > currentPrice:
                        print("BOT GO BRRRRRRR")
                        pos+=1
                        sumPos += difference
                    elif previousPrice == currentPrice:
                        print("BOT GORRRRRRRR")
                        nuet+=1
                        sumNeut += difference
                    else:
                        print("BOT GRRRRRRRRRRRR")
                        neg+=1
                        sumNeg += difference
                previousBuy = False
                previousSell = False
            print(datetime.now())
            # print((RSI(symbol)))
            RSIvalue = float(RSI(symbol)[obtainCurrentTime(1)]['RSI'])
            print(datetime.now())
            # print(RSIvalue)
            # print(obtainCurrentTime())
            # print(RSIvalue[obtainCurrentTime()])
            checkNextCandle = findCandleNumber(current, number)
            checkPusdo(current, RSIvalue)
            print(current)
            signal = obtainResult(checkNextCandle, RSIvalue, current)
            if signal == "BUY":
                print("BUY")
                automaticBuy()
                previousBuy = True
            if signal == "SELL":
                print("SELL")
                automaticSell()
                previousSell = True
            bol = False
            if (datetime.now().second >= 1 and datetime.now().second <= 2):
                timer = datetime.now().minute
            try:
                print(str(pos), str(nuet), str(neg))
                print(str(sumPos), str(sumNeut), str(sumNeg))
                print(str(sumPos/pos), str(sumNeut/nuet), str(sumNeg/neg))
            except:
                print("")
            time.sleep(50)

if __name__ == "__main__":
    # symbol = input("Symbol: ")
    # number = input("Number: ")
    symbol = "CHFJPY"
    # symbol = "XAU"
    while(True):
        # try:
        main(symbol, 5)
        # except:
        #     print("EROR: PLEASE CHANGE VPN IN WAIT TIME")
        #     time.sleep(60)






'''


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

'''