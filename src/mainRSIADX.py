from functions.AMX import findADXslope
from functions.GrabData import GrabCurrentData
from functions.RSI import RSI, checkPusdo, findCandleNumber, obtainResult
from functions.specialFunctions import automaticBuy, automaticSell, checkTime, obtainCurrentTime, obtainPastTimeFormatted
from datetime import datetime
import time
import multiprocessing



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
                    print("Symbol: " + str(symbol))

                    if previousPrice < currentPrice:
                        print("CORRECT")
                        pos+=1
                        sumPos += difference
                    elif previousPrice == currentPrice:
                        print("NUETROL")
                        nuet+=1
                        sumNeut += difference
                    else:
                        print("INCORRECT")
                        neg+=1
                        sumNeg += difference
                if previousSell:
                    print("Symbol: " + str(symbol))
                    if previousPrice > currentPrice:
                        print("CORRECT")
                        pos+=1
                        sumPos += difference
                    elif previousPrice == currentPrice:
                        print("NUETROL")
                        nuet+=1
                        sumNeut += difference
                    else:
                        print("INCORRECT")
                        neg+=1
                        sumNeg += difference
                previousBuy = False
                previousSell = False
            # print(datetime.now())
            # print((RSI(symbol)))
            RSIvalue = float(RSI(symbol)[obtainCurrentTime(1)]['RSI'])
            print(obtainPastTimeFormatted(0))
            # print(RSIvalue)
            # print(obtainCurrentTime())
            # print(RSIvalue[obtainCurrentTime()])
            checkNextCandle = findCandleNumber(current, number)
            checkPusdo(current, RSIvalue)
            print(current)
            signal = obtainResult(checkNextCandle, RSIvalue, current)
            slope = findADXslope("EURJPY", 5)
            if slope > 0.1:
                opp = True
            elif slope < -0.1:
                opp = False
            else:
                opp = None

            if opp != None:
                if (signal == "BUY" and opp == False) or (opp == True and signal == "SELL"):
                    print("BUY")
                    # automaticBuy()
                    previousBuy = True
                if (signal == "SELL" and opp == False) or (opp == True and signal == 'BUY'):
                    print("SELL")
                    # automaticSell()
                    previousSell = True
            bol = False
            if (datetime.now().second >= 1 and datetime.now().second <= 2):
                timer = datetime.now().minute
            try:
                print(str(pos), str(nuet), str(neg))
            except:
                print("")
            time.sleep(50)


if __name__ == "__main__":
    symbol = 'EURGBP'
    symbol2 = 'EURUSD'
    symbol3 = "EURJPY"
    # Create two processes, each running the `my_function` with different inputs
    process_1 = multiprocessing.Process(target=main, args=(symbol, 1))
    process_2 = multiprocessing.Process(target=main, args=(symbol2, 4))

    # Start the two processes
    process_1.start()
    process_2.start()

    # Wait for the two processes to finish
    process_1.join()
    process_2.join()






#IDEAS: 

#1. swap the slope
#2. swap the buy and SELL


# 2 min: 7 0 5
# 1min: 7 0 4
# 1 trade after: 3 0 3