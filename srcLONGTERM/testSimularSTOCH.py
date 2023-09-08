
# Update data
from src.WMA import get_WMA
from srcLONGTERM.longTermPos import checkLuquidation, findPos, findSelection
from src.VWAP import get_VWAP
from src.specialFunctions import optimize2
from src.testADX import grabADX
from src.testRSI import get_rsi
from src.testSupertrend import superTrend
import sys
from datetime import timedelta
from src.testIchi import get_ichimoku
from src.testSpecial import formatDataset
from src.testEMA import calculate_200ema
from src.testMACD import get_macd
from srcLONGTERM.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex

def simulateCrypto(data):

    data = grabADX(data, 14)
    rsiValue = 147 #8, 147
    dataRSI = get_rsi(data["close"], rsiValue)
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    data = data.dropna()

    j = -1
    k = -1
    previousBuy = False
    previousSell = False
    pos = 0
    nuet = 0
    neg = 0
    BestProfilio = -sys.maxsize
    WorseProfilio = sys.maxsize
    Bestj = -1
    Bestk = -1
    worstk = -1
    worstj = -1
    bestAvgj = -1
    bestAvgk = -1
    worstAvgj = -1
    worstAvgk = -1

    lst = []

    n = 60
    st10 = superTrend(data, 2, 1) # 2, 87
    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    longI = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortI = {'shortSignal': False, 'luquidate': False, 'entry': []}


    # ema2 = calculate_200ema(data2, 200)
    rsiValue2 = 10
    # dataRSI2 = get_rsi(data2["close"], rsiValue2)
    WMA = get_WMA(data, 11)
    ichimoku = get_ichimoku(data, 7, 15) # 7, 15
    # get_StochasticOscilator(data, 14, 10, 3) # ---> returns dataframe
    # stochK = data['%K']
    # stochD = data['%D']
    nowPrice = 0
    nowCount = 0
    STOCHamount2 = 2
    STOCHamount1 = 3


    try:
        for j in range(1, 1000):
            print("J: " + str(j))
            # get_StochasticOscilator(data, 301, 100, 101) 
            # stochK3 = data['%K']
            # stochD3 = data['%D']
            stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(data, 25, 751, 23)
            # print(stochRSIK, stochRSID)           
            # stochRSIK = data['%K']
            # stochRSID = data['%D']           
            # print("K: " + str(k))
            for i in range(1, len(data) - 1):
                nowPrice += data['close'][i]
                nowCount += 1
                longI, shortI = findSelection(previousBuy, previousSell, longI, shortI, i) 
                shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
                previousSell = previousBuy = False

                # ------ Uncomment ------- #
                # if stochK[i-1] >= stochD[i-1] and stochK[i] < stochD[i]:
                #     # print("\nSELL")
                #     # print(data.index[i] - timedelta(hours=4))
                #     # print("K: " + str(stochK[i]))
                #     # print("D: " + str(stochD[i]))
                #     previousSell = True
                # else:
                #     previousSell = False
                # if stochK[i-1] <= stochD[i-1] and stochK[i] > stochD[i]:
                #     # print("\nBUY")
                #     # print(data.index[i] - timedelta(hours=4))
                #     previousBuy = True
                # else:
                #     previousBuy = False                


                # # if previousBuy:
                # #     previousBuy = False
                # #     previousSell = True
                # # elif previousSell:
                # #     previousSell = False
                # #     previousBuy = True
                
                # if previousBuy and previousSell:
                #     previousBuy = False
                #     previousSell = False

                # if stochK2[i-1] >= stochD2[i-1] and stochK2[i] < stochD2[i]:
                #     previousSell = True
                # if stochK2[i-1] <= stochD2[i-1] and stochK2[i] > stochD2[i]:
                #     previousBuy = True



                # if previousBuy and previousSell:
                #     previousBuy = False
                #     previousSell = False


                # if stochK3[i-1] >= stochD3[i-1] and stochK3[i] < stochD3[i]:
                #     previousSell = True
                # if stochK3[i-1] <= stochD3[i-1] and stochK3[i] > stochD3[i]:
                #     previousBuy = True
            
                # if previousBuy and previousSell:
                #     previousBuy = False
                #     previousSell = False

                # UNCOMMENT #

                if stochRSIK[i-1] >= stochRSID[i-1] and stochRSIK[i] < stochRSID[i]:
                    previousSell = True
                if stochRSIK[i-1] <= stochRSID[i-1] and stochRSIK[i] > stochRSID[i]:
                    previousBuy = True


                if previousBuy and previousSell:
                    previousBuy = False
                    previousSell = False




            percentOfTrades = round(((pos + nuet + neg) / len(data)) * 100, 2)
                    
            try:
                AvgPrice = nowPrice/nowCount
                print(pos, nuet, neg)
                try:
                    print("POS/NEG RATIO: " + str(pos / neg))
                    print(
                        "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                    )
                except: 
                    print("ERROR 404")
                print("CANDLES: " + str(len(data) - 2))
                print(
                    "PERCENT OF TRADES: "
                    + str(percentOfTrades)
                )
                print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                print("AVERAGE PIPS: " + str(totalPips/countPips))
                print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                print("NEGITIVE PIPS: " + str(negPip))
                print("AVERAGE %: " + str(round((avgPips/AvgPrice), 5)))
                print("POS %: " + str(round(posPips/(pos)/AvgPrice, 5)))
                print("NEG %: " + str(round(negPip/AvgPrice, 5)))

                
            except ZeroDivisionError:
                print("ERROR GO BRRRR")
            # # ------Profilio-----

            lst.append(portfolio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            # if avgPips > 1000:
            #     avgPips -= 1000
            #     avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
            if avgPips*percentOfTrades > bestAvgPips and avgPips > 60000:
                bestAvgPips = avgPips*percentOfTrades
                bestAvgj = j
                bestAvgk = k
            if avgPips*percentOfTrades < worstAvgPips:
                worstAvgPips = avgPips*percentOfTrades
                worstAvgj = j
                worstAvgk = k
            if portfolio > BestProfilio:
                BestProfilio = portfolio
                Bestj = j
                Bestk = k
            elif portfolio < WorseProfilio:
                WorseProfilio = portfolio
                worstj = j
                worstk = k
            pos = nuet = neg = 0

            portfolio = 10
            negPips = 0
            posPips = 0
            totalPips = 0
            countPips = 0
            countPos = 0
            countNeg = 0
        #SEPERATE WHEN TABBING
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj
    except KeyboardInterrupt:
        print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj))
        print("K: " + str(worstk))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))





if "__main__" == __name__:
    f = open("documents/dataCryptoTest15min.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    # print(data)
    
    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj = simulateCrypto(data)
    #720mi
    # 77mil
    # 200bil


    # if not lst:
    #     exit()
    
    # total = sum(lst)
    # average = total / len(lst)


    # sorted_arr = sorted(lst)
    # n = len(sorted_arr)
    
    # if n % 2 == 1:
    #     median = sorted_arr[n // 2]
    # else:
    #     middle_right = n // 2
    #     middle_left = middle_right - 1
    #     median = (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2
    print("\n\nSIMULATION RESULTS: ")
    print("BestAVGPips: " + str(bestAvgPips))
    print("K: " +str(bestAvgk))
    print("J: " + str(bestAvgj))
    print("\nWORSTAVGPips: " + str(worstAvgPips))
    print("K: " +str(worstAvgk))
    print("J: " + str(worstAvgj))



    # BestAVGPips*percentOfTrades
    print("\n\n\n\n")
    print("Best Portfolio: \n" + str(BestProfilio))
    print("J:" + str(Bestj))
    print("K: " + str(Bestk))
    print('\n\n')
    print("Worst Portfolio: \n" + str(WorseProfilio))
    print("J: " + str(worstj))
    print("K: " + str(worstk))
