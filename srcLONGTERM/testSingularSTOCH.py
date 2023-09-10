
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
            print("J: " + str(j-1))
            # for k in range(1, 100):
            countPips = 0
            avgPips = 0
            # get_StochasticOscilator(data, 301, 100, 101) 
            # stochK3 = data['%K']
            # stochD3 = data['%D']
            # (1334, 16, 15) -> 0.17 --> 200,000 
            # (data, 1293, 50, 15) --> 0.24 --> -146,000
            # (817, 50, 15) --> 0.59 --> -83,000
            # (817, 220, 15) --> 0.28 --> -110,000
            # (293, 83, 316) --> 0.21 --> -169,000
            # (24, 1956, 25) --> 1.05 --> 41,739
            # (787, 1, 328) --> 0.77 --> -40,000
            # (560, 5, 200) --> 0.24 --> -125,281
            # (417, 71, 200) --> 0.21 --> -161,000
            # (677, 70, 872) --> 0.07 --> 500,000
            # (535, 127, 137) --> 0.17 --> 127,000
            # (401, 127, 137) --> 0.21 --> -168,000
            # (401, 127, 80) --> 0.56 --> -47,272
            # (401, 127, 153) --> 0.21 --> -169,000
            # (123, 123, 153) --> 0.59 --> -58,589
            # (660, 660, 153) --> 0.14 --> 133,000
            # (154, 263, 586) --> 0.21 --> -136,000
            # (154, 120, 586) --> 0.49 --> -57,000
            # (154, 120, 613) --> 0.52 --> -64,000
            # (133, 120, 133) --> 0.59 --> -62,000
            # (281, 120, 281) --> 0.21 --> -162,650
            # (202, 52, 152) --> 0.52 --> -74,000
            # (468, 9, 152) --> 0.66 --> -55,000
            # (468, 52, 152) --> 0.24 --> -150,000
            # (468, 9, 324) --> 0.24 --> -125,458
            g = 339 #J:239, J: 339
            get_StochasticOscilator(data, 196, 731, 314) # 6, 303, 920
            stochK1 = data['%K']
            stochD1 = data['%D']
            # print(stochRSIK, stochRSID)          
            # stochRSIK = data['%K']
            # 561, 418 --> bad
            # stochRSID = data['%D']           
            # print("K: " + str(k))
            for i in range(1, len(data) - 1):
                nowPrice += data['close'][i]
                nowCount += 1
                longI, shortI = findSelection(previousBuy, previousSell, longI, shortI, i) 
                shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
                previousSell = previousBuy = False

                if stochK1[i-1] >= stochD1[i-1] and stochK1[i] < stochD1[i]:
                    previousSell = True
                if stochK1[i-1] <= stochD1[i-1] and stochK1[i] > stochD1[i]:
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
                leverage = 50
                print(f"{leverage}X LEVERAGE")
                print("AVERAGE %: " + str(round((avgPips/AvgPrice)*leverage, 5)))
                print("POS %: " + str(round((posPips/(pos)/AvgPrice)*leverage, 5)))
                print("NEG %: " + str(round((negPip/AvgPrice)*leverage, 5)))
                if j == 411:
                    print('a')
                if avgPips*percentOfTrades > bestAvgPips and pos > 0 and percentOfTrades > 1:
                    # if j == 411:
                    #     print("a")
                    bestAvgPips = avgPips*percentOfTrades
                    bestAvgj = j-1
                    bestAvgk = k-1
                if avgPips*percentOfTrades < worstAvgPips and avgPips < -40000 and percentOfTrades > 0.5:
                    worstAvgPips = avgPips*percentOfTrades
                    worstAvgj = j-1
                    worstAvgk = k-1
                if portfolio > BestProfilio:
                    BestProfilio = portfolio
                    Bestj = j-1
                    Bestk = k-1
                elif portfolio < WorseProfilio:
                    WorseProfilio = portfolio
                    worstj = j-1
                    worstk = k-1
                
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
        print("BEST K: " + str(k-1))
        print("BEST J: " + str(j-1))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk-1))
        print("J: " + str(bestAvgj-1))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj-1))
        print("K: " + str(worstk-1))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk-1))
        print("J: " + str(worstAvgj-1))





if "__main__" == __name__:
    f = open("documents/dataCryptoTest15min.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    import pandas as pd
    df = pd.read_csv('output.csv')
    df.rename(columns={'High': 'high', 'Low': 'low', "Open": 'open', 'Close':'close'}, inplace=True)
    df = df.set_index('Datetime')
    df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    print(df)    

    # print(data)
    
    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj = simulateCrypto(df)
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
    print("J:" + str(Bestj-1))
    print("K: " + str(Bestk-1))
    print('\n\n')
    print("Worst Portfolio: \n" + str(WorseProfilio))
    print("J: " + str(worstj-1))
    print("K: " + str(worstk-1))
