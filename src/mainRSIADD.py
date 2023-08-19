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
                # dataClose = GrabCurrentData(symbol)
                # f = open('documents/data.txt', 'w')
                # f.write(str(dataClose))
                # previousPrice = dataClose[obtainPastTimeFormatted(2)]['4. close']
                # currentPrice = dataClose[(obtainPastTimeFormatted(1))]['4. close']
                # print("previously" + str(previousPrice))
                # print("currently: " + str(currentPrice))
                # if previousBuy:
                #     print("Symbol: " + str(symbol))

                #     if previousPrice < currentPrice:
                #         print("CORRECT")
                #         pos+=1
                #         sumPos += difference
                #     elif previousPrice == currentPrice:
                #         print("NUETROL")
                #         nuet+=1
                #         sumNeut += difference
                #     else:
                #         print("INCORRECT")
                #         neg+=1
                #         sumNeg += difference
                # if previousSell:
                #     print("Symbol: " + str(symbol))
                #     if previousPrice > currentPrice:
                #         print("CORRECT")
                #         pos+=1
                #         sumPos += difference
                #     elif previousPrice == currentPrice:
                #         print("NUETROL")
                #         nuet+=1
                #         sumNeut += difference
                #     else:
                #         print("INCORRECT")
                #         neg+=1
                #         sumNeg += difference
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
            slope, currentADX = findADXslope(symbol, 5) # was getting EURJPY slope
            continuement = True
            if slope > 0.1:
                opp = False
            elif slope < -0.1:
                opp = True
            else:
                opp = None
            # if currentADX < 20:
            #     continuement = False
            # if RSIvalue < 55 and RSIvalue > 45:
            #     continuement = False
                
            if opp != None and continuement == True:
                if (signal == "BUY" and opp == False) or (opp == True and signal == "SELL"):
                    print("BUY")
                    print(symbol)
                    # automaticBuy()
                    previousBuy = True
                if (signal == "SELL" and opp == False) or (opp == True and signal == 'BUY'):
                    print("SELL")
                    print(symbol)
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
    symbol4 = "GBPJPY"
    # Create two processes, each running the `my_function` with different inputs
    process_1 = multiprocessing.Process(target=main, args=(symbol3, 1))
    process_2 = multiprocessing.Process(target=main, args=(symbol4, 1))

    # Start the two processes
    process_1.start()
    process_2.start()

    # Wait for the two processes to finish
    process_1.join()
    process_2.join()


#NOTES:

# AT green

# 2min+: correct

#AT RED
# 1min only correct




#IDEAS: 

#1. do opp when ADX < 20
# dont do anything when RSI < 55 and RSI > 45
#2. swap the buy and SELL


# 2 min: 7 0 5
# 1min: 7 0 4
# # 1 trade after: 3 0 3

# OTHER:


# 2min: 11 1 5
# 1 min: 8 3 6
# 1 trade after: 10 2 4

#EURJPY
#1min: 12 1 2
# 2min: 12 0 4
# 1aft: 7 0 8
# 2aft: 1 0 6
#EURUSD
# 1min: 5 1 3
# 2min: 5 0 4
# 1aft: 5 0 4

#8:25pm-Whatever

#EURJPY
# 1min: 1 0 3
# 2min: 2 0 2
# 1aft: 2 0 2
# 2aft: 3 0 1
#EURUSD
# 1min: 1 0 1
# 2min: 2 0 0
# 1aft: 2 0 0
# 2aft: 1 0 1


#9am-onward:
#EURJPY
# 1min: 0 0 2
# 2min: 0 1 1
# 1aft: 2 0 0
# 2aft: / 0 1


#GBPJPY
# 1min: 0 0 1
# 2min: 0 0 1
# 1aft: 0 0 1
# 2aft: 0 0 1

#4pm
#EURJPY
# 1min: 0 0 3
# 2min: 0 0 3
# 1aft: 1 0 2
# 2aft: 2 0 1


#GBPJPY
# 1min: 1 0 1
# 2min: 1 0 1
# 1aft: 1 0 1
# 2aft: 1 0 1

#11:00
#EURJPY
# 1min: 1 0 3
# 2min: 1 0 3
# 1aft: 3 0 1
# 2aft: 4 0 0


#GBPJPY
# 1min: 4 0 6
# 2min: 3 0 7
# 1aft: 4 2 4
# 2aft: 5 1 4

#12:00
#EURJPY
# 1min: 0 0 0
# 2min: 0 0 0
# 1aft: 0 0 0
# 2aft: 0 0 0

#GBPJPY
# 1min: 1 0 1
# 2min: 2 0 0
# 1aft: 2 0 0
# 2aft: 1 0 1


#1:00pm
#EURJPY
# 1min: 3 0 0
# 2min: 3 0 0
# 1aft: 1 0 2
# 2aft: 0 0 3

#GBPJPY
# 1min: 3 1 2
# 2min: 3 0 3
# 1aft: 2 0 4
# 2aft: 5 0 1


#2:00pm  
#EURJPY
# 1min: 5 0 2
# 2min: 4 0 3
# 1aft: 2 0 5
# 2aft: 5 0 2

#GBPJPY
# 1min: 5 0 3
# 2min: 6 0 2
# 1aft: 6 0 2
# 2aft: 4 0 4