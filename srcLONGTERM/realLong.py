from datetime import datetime

from testGrabData import calltimes
previousMinute = -1

while True:
    if datetime.now().minute != previousMinute:
        if datetime.now().second > 0 and datetime.now().second < 2:
            print("\n" + datetime.now().strftime("%H:%M"))
            previousMinute = datetime.now().minute  
            data = calltimes("BTCUSD", 1, "2023-08-6 0:45", 'd3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9')
            


            nowPrice += data['close'][i]
            nowCount += 1
            longI, shortI = findSelection(previousBuy, previousSell, longI, shortI, i) 
            shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
            previousSell = previousBuy = False


            if stochK[i-1] >= stochD[i-1] and stochK[i] < stochD[i]:
                # print("SELL")
                # print(data.index[i])
                # print("K: " + str(stochK[i]))
                # print("D: " + str(stochD[i]))
                previousSell = True
            else:
                previousSell = False
            if stochK[i-1] <= stochD[i-1] and stochK[i] > stochD[i]:
                previousBuy = True
            else:
                previousBuy = False                




            if previousBuy and previousSell:
                previousBuy = False
                previousSell = False





