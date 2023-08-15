from functions.GrabData import GrabCurrentData
from functions.specialFunctions import automaticBuy, automaticReset, automaticSell, obtainCurrentTime, obtainPastTimeFormatted
from src.functions.STOCHredo import STOCH, checkPusdo, findCandleNumber, obtainResult
from datetime import datetime, timedelta
import time
# 1 is at 80.06674757281553%
#EURUSD
def main(symbol):

    current = {}
    current[">percentD"] = 0
    current["<percentD"] = 0
    checkNextCandle = 0
    timer = -1
    bol = False
    previousBuy = False
    previousSell = False
    i = pos = nuet = neg = 0
    sumPos = sumNeut = sumNeg = 0
    difference = 0
    try:
        while(True):
            if (datetime.now().second >= 1 and datetime.now().second <= 2 and not datetime.now().minute == timer):
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
                    
                listOfKD = STOCH(symbol, 2, 1, 2)
                # print(listOfKD)
                # print(listOfKD)
                f = open('documents/listofKDkeys.txt', 'w')
                f.write(str(listOfKD))
                percentK = float(listOfKD[obtainCurrentTime(1)]['SlowK'])
                percentD = float(listOfKD[obtainCurrentTime(1)]['SlowD'])
                checkNextCandle = findCandleNumber(current) # check next candle 
                signal, difference = obtainResult(checkNextCandle, current, percentK, percentD) # gives output of BUY or SELL
                checkPusdo(current, percentK, percentD) # change current
                # goodLocation = (1443, 484)
                # badlocation = (1455, 625)
                print(difference)
                # 7 is low: wrong
                # is low diviosn
                if signal == "BUY":
                    # if i >= 1:
                    #     automaticReset((1459, 494))
                    if difference < 10:
                        print("BUY: LOW" )
                    elif difference > 10:
                        print("BUY: MID")
                    else:
                        print("BUY: HIGH")
                    # automaticBuy((1443, 484))
                    previousBuy = True
                    i+=1
                elif signal == 'SELL':
                    # if i >= 1:
                        # automaticReset((1459, 494))
                    print("SELL")
                    previousSell = True
                    # automaticSell((1455, 625))
                    i+=1
                else:
                    print("NONE")
                if (datetime.now().second >= 1 and datetime.now().second <= 2):
                    timer = datetime.now().minute
                bol = False
                print(datetime.now())
                time.sleep(50)
    except:
        print(str(pos), str(nuet), str(neg))
        print(str(sumPos), str(sumNeut), str(sumNeg))
        print(str(sumPos/pos), str(sumNeut/nuet), str(sumNeg/neg))

if __name__ == "__main__":
    main("EURJPY")
