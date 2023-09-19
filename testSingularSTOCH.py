# Update data

# from src.WMA import get_WMA
from srcLONGTERM.longTermPos import checkLuquidation, findSelection
# from src.VWAP import get_VWAP
# from src.specialFunctions import optimize2
# from src.testADX import grabADX
# from src.testRSI import get_rsi
# from src.testSupertrend import superTrend
import sys
# from datetime import timedelta
# from src.testIchi import get_ichimoku
from src.testSpecial import formatDataset
# from src.testEMA import calculate_200ema
# from src.testMACD import get_macd
from srcLONGTERM.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex

def simulateCrypto(data):

    # data = grabADX(data, 14)
    # rsiValue = 147 #8, 147
    # dataRSI = get_rsi(data["close"], rsiValue)
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
    # st10 = superTrend(data, 2, 1) # 2, 87
    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    longI = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortI = {'shortSignal': False, 'luquidate': False, 'entry': []}
    hehehhahahaaPIPS2 = 0
    hehehahhaPer2 = 0
    hehehhahahaaPIPS = 0
    hehehahhaPer = 0


    # ema2 = calculate_200ema(data2, 200)
    rsiValue2 = 10
    # dataRSI2 = get_rsi(data2["close"], rsiValue2)
    
    # WMA = get_WMA(data, 11)
    # ichimoku = get_ichimoku(data, 7, 15) # 7, 15
    
    # get_StochasticOscilator(data, 14, 10, 3) # ---> returns dataframe
    # stochK = data['%K']
    # stochD = data['%D']
    nowPrice = 0
    nowCount = 0
    STOCHamount2 = 2
    STOCHamount1 = 3

    stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 18, 883, 22) # 13%
    get_StochasticOscilator(data, 34, 34, 34) # -21%
    get_StochasticOscilator(data, 460, 351, 4) # 23%
    get_StochasticOscilator(data, 30, 387, 35) # -19%
    get_StochasticOscilator(data, 79, 34, 17) # -26%
    get_StochasticOscilator(data, 46, 344, 25) # 26%
    get_StochasticOscilator(data, 158, 439, 8) # 23%
    get_StochasticOscilator(data, 232, 446, 5) # 22%
    get_StochasticOscilator(data, 42, 345, 25) # 23%
    get_StochasticOscilator(data, 271, 441, 4) # 24%
    get_StochasticOscilator(data, 327, 441, 3) # 24%
    get_StochasticOscilator(data, 66, 396, 10) # -21%
    get_StochasticOscilator(data, 136, 441, 10) # 23%
    get_StochasticOscilator(data, 6, 73, 1251) # 22%
    get_StochasticOscilator(data, 327, 327, 4) # 21%
    
    try:
        for j in range(1, 3000):
            print("J: " + str(j-1))
            # for k in range(1, 100):
            countPips = 0
            avgPips = 0
            
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 165, 48, 181) # 45k --> 0.77
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 151, 122, 76) # 43k --> 0.77
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 112, 122, 79) # 39k --> 0.87
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 82, 136, 82) # 37k --> 0.97
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 170, 108, 72) # 38k --> 0.77
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 66, 141, 76) # 40k --> 1.18
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 66, 110, 121) # 40k --> 1.07
            # stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 46, 58, 211) # 36k --> 1.18



            # -----NEW-----#
            # (69, 148, 59) -->  1.07 --> 40,000
            # (180, 33, 132) --> 0.87 --> 44,000
            # (96, 64, 110) --> 0.97 --> 33,000
            # (23, 375, 325) --> 1.37 --> -30,000

            # g = 339 #J:239, J: 339
            # a = 00000
            g = j
            print2 = True
            get_StochasticOscilator(data, j, j, 2) # 21%, 25, 345, 25, (772, 511, 345) 1248
            stochRSIK2 = data['%K']
            stochRSID2 = data['%D']
            # get_StochasticOscilator(da ta, 196, 731, 314) # 6, 303, 9
            # stochRSIK2 = data['%K']
            # stochRSID2 = data['%D']
            # print(stochRSIK, stochRSID)          
            # stochRSIK = data['%K']
            # 561, 418 --> bad
            # stochRSID = data['%D']           
            # print("K: " + str(k))
            v = 1
            
            for i in range(1, len(data)):
                nowPrice += data['close'].iloc[i]
                nowCount += 1
                longI, shortI = findSelection(previousBuy, previousSell, longI, shortI, i) 
                shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
                previousSell = previousBuy = False
                # dif = stochRSIK2[i-v]/stochRSID2[i-v]

                if stochRSIK2.iloc[i-v] >= stochRSID2.iloc[i-v] and stochRSIK2.iloc[i] < stochRSID2.iloc[i]:
                    previousSell = True
                if stochRSIK2.iloc[i-v] <= stochRSID2.iloc[i-v] and stochRSIK2.iloc[i] > stochRSID2.iloc[i]:
                    previousBuy = True


                if previousBuy and previousSell:
                    previousBuy = False
                    previousSell = False




            percentOfTrades = round(((pos + nuet + neg) / len(data)) * 100, 2)
            
            try:
                AvgPrice = nowPrice/nowCount
                if print2 == True:
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
                if print2:
                    print("AVERAGE PIPS: " + str(totalPips/countPips))
                    print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                if print2:
                    print("NEGITIVE PIPS: " + str(negPip))
                    print("AVERAGE %: " + str(round((avgPips/AvgPrice), 5)))
                    print("POS %: " + str(round(posPips/(pos)/AvgPrice, 5)))
                    print("NEG %: " + str(round(negPip/AvgPrice, 5)))
                    leverage = 50
                    print(str(leverage) + "X LEVERAGE")
                    print("AVERAGE %: " + str(round((avgPips/AvgPrice)*leverage, 5)))
                    print("POS %: " + str(round((posPips/(pos)/AvgPrice)*leverage, 5)))
                    print("NEG %: " + str(round((negPip/AvgPrice)*leverage, 5)))
                if avgPips > bestAvgPips and percentOfTrades > 2.5:
                    # if j == 411:
                    #     print("a")
                    bestAvgPips = avgPips
                    bestAvgj = j
                    bestAvgk = k
                    hehehhahahaaPIPS2 = avgPips
                    hehehahhaPer2 = percentOfTrades
                if avgPips < worstAvgPips and percentOfTrades > 2.5:
                    worstAvgPips = avgPips
                    worstAvgj = j
                    worstAvgk = k
                    hehehhahahaaPIPS = avgPips
                    hehehahhaPer = percentOfTrades
                if portfolio > BestProfilio:
                    BestProfilio = portfolio
                    Bestj = j
                    Bestk = k
                elif portfolio < WorseProfilio:
                    WorseProfilio = portfolio
                    worstj = j
                    worstk = k
                
            except ZeroDivisionError:
                if print2 == True:
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
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, hehehhahahaaPIPS, hehehahhaPer, hehehhahahaaPIPS2, hehehahhaPer2
    except KeyboardInterrupt:
        # print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        # print("BEST K: " + str(k-1))
        # print("BEST J: " + str(j-1))
        # print("\n")
        print("\nPosPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("PIPS: "  + str(hehehhahahaaPIPS2))
        print("PERCENT: " + str(hehehahhaPer2))
        # print("\n\nWorst Portfolio: " + str(WorseProfilio))
        # print("J: " + str(worstj-1))
        # print("K: " + str(worstk-1))
        print("\nNegPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))
        print("PIPS: "  + str(hehehhahahaaPIPS))
        print("PERCENT: " + str(hehehahhaPer))





if "__main__" == __name__:
    f = open("documents/binance30.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    print(len(data))
    # data = data[0:5000]
    
    data = formatDataset(data)
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']

    for column in columns_to_convert:
        data[column] = data[column].astype(float)

    # import pandas as pd
    # df = pd.read_csv('output.csv')
    # df.rename(columns={'High': 'high', 'Low': 'low', "Open": 'open', 'Close':'close'}, inplace=True)
    # df = df.set_index('Datetime')
    # df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    # print(df)    

    # print(data)
    # pool = multiprocessing.Pool()
    # BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, hehehhahahaaPIPS, hehehahhaPer, hehehhahahaaPIPS2, hehehahhaPer2 = pool.map(simulateCrypto, data)

    
    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, hehehhahahaaPIPS, hehehahhaPer, hehehhahahaaPIPS2, hehehahhaPer2 = simulateCrypto(data)
    
    

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
    print("PosPips: " + str(bestAvgPips))
    print("K: " +str(bestAvgk))
    print("J: " + str(bestAvgj))
    print("PIPS: "  + str(hehehhahahaaPIPS2))
    print("PERCENT: " + str(hehehahhaPer2))
    print("\nNegPips: " + str(worstAvgPips))
    print("K: " +str(worstAvgk))
    print("J: " + str(worstAvgj))
    print("PIPS: "  + str(hehehhahahaaPIPS))
    print("PERCENT: " + str(hehehahhaPer))



    # # BestAVGPips*percentOfTrades
    # print("\n\n\n\n")
    # print("Best Portfolio: \n" + str(BestProfilio))
    # print("J:" + str(Bestj-1))
    # print("K: " + str(Bestk-1))
    # print('\n\n')
    # print("Worst Portfolio: \n" + str(WorseProfilio))
    # print("J: " + str(worstj-1))
    # print("K: " + str(worstk-1))
