
# Update data
from src.simulate import findPos
from src.VWAP import get_VWAP
from src.specialFunctions import obtainResult, optimizeResult
from src.testADX import grabADX
from src.testAroon import aroon
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch
from src.testSupertrend import get_supertrend, superTrend
import sys

from src.testSTOCHRSI import get_STOCHRSI
from src.testIchi import get_ichimoku
from src.testSpecial import formatDataset
from src.testEMA import calculate_200ema
from src.testMACD import get_macd

def simulateCrypto(data, avgResult, avgInput):
    
    ultimateData = data
    data2 = data
    data = grabADX(data, 14)
    # print(data)
    # ema = calculate_200ema(data, 200)
    VWAPdata = get_VWAP(data, 5)
    # aroonData = aroon(data, 14)f
    # dataRSI2 = get_rsi(data["close"], 9)
    # macdData = get_macd(data, 12, 26, 9)
    # STOCHRSI = get_STOCHRSI(data, 14, 3, 3)
    rsiValue = 147 #8, 147
    dataRSI = get_rsi(data["close"], rsiValue)

    totalPips = 0
    countPips = 0
    bestAvgPips = 0
    # print(dataRSI)
    data = get_stoch(ultimateData, 5, 3)
    # MACD setup
    # macd_data = macdData.dropna()
    # macd_signal = ""

    # STOCH setup
    data = data.dropna()

    # Supertrend setup
    # def getSupertrend():
    j = -1
    st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
    st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
    st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 1) #change to 2
    st7, upt7, dt7 = get_supertrend(data["high"], data["low"], data["close"], 65, 1)


    st23, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 40, 2)
    st22, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 30, 2)
    st20, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 3, 3)

    # stdata = [164, 1]
    # st = superTrend(data, stdata[0], stdata[1])
    # df_filtered = st[[f'SUPERT_{stdata[0]}_{stdata[1]}.0']]
    # st = df_filtered[f'SUPERT_{stdata[0]}_{stdata[1]}.0']
    # print(st)


    # Average Result: 1568010824.655752
    # Median Result: 28360590.612781316
    # Best Profilio: 162631407085.49048

    # Average Result: 3952144693.0374
    # Median Result: 5280123.050841998
    # Best Profilio: 432493562718.766



    #       POS/NEG RATIO: 3.4464285714285716
    #       Percentage Correct: 77.51%
    #       CANDLES: 6968
    #       PERCENT OF TRADES: 7.33
    #       1099400833.0625887
    # 2: 20 3
    # 3: 5 2
    # 4: 1 1
    k = -1
    previousBuy = False
    previousSell = False
    correctBuy = True
    correctSell = True
    prevSellRSI = False
    prevBuyRSI = False
    contempent = False
    prevSellSTOCH = None
    prevBuySTOCH = None

    pos = 0
    nuet = 0
    neg = 0

    number = 0
    BestProfilio = -sys.maxsize
    WorseProfilio = sys.maxsize
    checkNextCandle = 0

    Bestj = -1
    Bestk = -1
    worstk = -1
    worstj = -1
    # stbuy = None
    # stbuy1 = None
    # stbuy2 = None
    # stbuy3 = None
    # stbuy4 = None
    # stbuy5 = None
    # stbuy6 = None
    # stbuy7 = None
    previousSignal = None
    bestAvgj = -1
    bestAvgk = -1

    lst = []
    current = {}

    n = 0
    length = difference = 0
    VWAP5 = get_VWAP(data, 5)
    # Loop to go through datapoints
    # for j in range(1, 101):
    # for j in range(1, 101):

    # st11 = superTrend(data, 6, 1)
    VWAPdata = get_VWAP(data, 1)
    st10 = superTrend(data, 2, 1) # 2, 87
    profilio = 10
    change = 0
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    bullish = bearish = None


    data2 = grabADX(data2, 14)
    ema2 = calculate_200ema(data2, 200)
    macdData2 = get_macd(data2, 12, 26, 9)
    data2 = get_stoch(ultimateData, 5, 3)
    data2.drop(columns=["n_low", "%K", "%D"])

    macd_data = macdData2.dropna()
    macd_signal = ""

    # STOCH setup
    data = data.dropna()



    try:
        for k in range(1, 101):
            print("K: " + str(k))
            n = 0
            for i in range(102, len(data) - 102):
                
                pos, nuet, neg, profilio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio, totalPips, countPips, posPips, countPos, negPips, countNeg)
                previousSell = previousBuy = False
                previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)
                    
            try:
                percentOfTrades = round(((pos + nuet + neg) / len(data)) * 100, 2)
                print(pos, nuet, neg)
                print("POS/NEG RATIO: " + str(pos / neg))
                print(
                    "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                )
                print("CANDLES: " + str(len(data) - 2))
                print(
                    "PERCENT OF TRADES: "
                    + str(percentOfTrades)
                )
                print("protfilio: " + str(profilio))
                avgPips = totalPips/countPips
                print("AVERAGE PIPS: " + str(totalPips/countPips))
                print("POSITIVE PIPS: " + str(posPips/(pos)))
                print("NEGITIVE PIPS: " + str(negPips/(neg)))

                
            except ZeroDivisionError:
                print("ERROR GO BRRRR")
            # ------Profilio-----

            lst.append(profilio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            pos = nuet = neg = 0
            if avgPips > 1200:
                avgPips -= 1200
                avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
                if avgPips > bestAvgPips:
                    bestAvgPips = avgPips
                    bestAvgj = j
                    bestAvgk = k
            if profilio > BestProfilio:
                BestProfilio = profilio
                Bestj = j
                Bestk = k
            elif profilio < WorseProfilio:
                WorseProfilio = profilio
                worstj = j
                worstk = k
            profilio = 10
            negPips = 0
            posPips = 0
            totalPips = 0
            countPips = 0
            countPos = 0
            countNeg = 0
        #SEPERATE WHEN TABBING
        return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk
    except KeyboardInterrupt:
        print("BEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("BestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))



if "__main__" == __name__:
    f = open("documents/dataCryptoTest.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    
    lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk = simulateCrypto(data, 1.5, 0.1)

    if not lst:
        exit()
    
    total = sum(lst)
    average = total / len(lst)


    sorted_arr = sorted(lst)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        median = sorted_arr[n // 2]
    else:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2
    print("BestAVGPips: " + str(bestAvgPips))
    print("K: " +str(bestAvgk))
    print("J: " + str(bestAvgj))



    print("\n")
    print("Average Result: " + str(average))
    print("Median Result: " + str(median))
    print("\n")
    print("Best Portfolio: " + str(BestProfilio))
    print("J:" + str(Bestj))
    print("K: " + str(Bestk))
    print("Worst Portfolio: " + str(WorseProfilio))
    print("J: " + str(worstj))
    print("K: " + str(worstk))
