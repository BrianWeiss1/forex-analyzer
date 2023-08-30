
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
    # aroonData = aroon(data, 14)
    # dataRSI2 = get_rsi(data["close"], 9)
    # macdData = get_macd(data, 12, 26, 9)
    # STOCHRSI = get_STOCHRSI(data, 14, 3, 3)
    rsiValue = 8
    dataRSI = get_rsi(data["close"], rsiValue)
    data = get_stoch(ultimateData, 5, 3)
    totalPips = 0
    countPips = 0
    # print(dataRSI)

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

    lst = []
    current = {}

    n = 0
    length = difference = 0
    VWAP5 = get_VWAP(data, 5)
    # Loop to go through datapoints
    # for j in range(1, 101):
    # for j in range(1, 101):
    ichimoku = get_ichimoku(data)

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



    ema2 = calculate_200ema(data2, 200)
    rsiValue2 = 5
    dataRSI2 = get_rsi(data2["close"], rsiValue2)
    macdData2 = get_macd(data2, 12, 26, 9)
    data2 = get_stoch(ultimateData, 5, 3)
    data2.drop(columns=["n_low", "%K", "%D"])
    macd_data = macdData2.dropna()

    # STOCH setup
    data = data.dropna()

    try:
        for k in range(1, 101):
            print("K: " + str(k))
            # for j in range(1, 100):
            n = 0
            for i in range(10, len(data) - 10):
                
                pos, nuet, neg, profilio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio, totalPips, countPips, posPips, countPos, negPips, countNeg)
                previousSell = previousBuy = False
                previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)

                # if ichimoku['a'][i] > ichimoku['b'][i]:
                #     bullish = True
                # else:
                #     bullish = False
                # if ichimoku['a'][i] < ichimoku['b'][i]:
                #     bearish = True
                # else:
                #     bearish = False


                #----82% sucess----#
                bullish = True
                bearish = True
                #by itself: 50%, with 80%
                if data['close'][i] > ichimoku['cover'][i] and data['close'][i] > ichimoku['base'][i] and bullish and previousBuy:
                    previousBuy = True
                else:
                    previousBuy = False
                if data['close'][i] < ichimoku['cover'][i] and data['close'][i] < ichimoku['base'][i] and bearish and previousSell:
                    previousSell = True
                else:
                    previousSell = False
                
                if previousBuy and previousSell:
                    previousSell = False
                    previousBuy = False
                #------82% sucess: 5% of tradess----#



                # if not previousBuy or not previousSell:
                #     previousBuy, previousSell = optimizeResult(i, data2, ema2, dataRSI2, rsiValue2, macd_data, st23, st22, st20, st3)
























                # if cloud is under price:
                #     Bullish
                # if cloud is overprice:
                #     sellish
                # the bigger the better

                # dont buy if inside the cloud






                
                # if VWAPdata[i] > data['close'][i]+change and previousSell:
                #     #only sell
                #     previousSell = True
                # else:
                #     previousSell = False
                # if VWAPdata[i] + change < data['close'][i] and previousBuy:
                #     #only buy
                #     previousBuy = True
                # else:
                #     previousBuy = False





                # # Supertrend
                # if st10[i] > data['close'][i] and previousBuy:
                #     previousBuy = True
                # else:
                #     previousBuy = False
                # if st10[i] < data['close'][i] and previousSell:
                #     previousSell = True
                # else:
                #     previousSell = False




                    
                # # # if  
                # def funct(num, i, VWAP5):
                #     if VWAP5[i] > data['close'][i]+num:
                #         prevSell = True
                #     else:
                #         prevSell = False
                #     if VWAPdata[i] + change < data['close'][i] and previousBuy:
                #         #only buy
                #         prevBuy = True
                #     else:
                #         prevBuy = False
                #     return prevBuy, prevSell
                # def callAllFunct(lst, i, VWAP5):
                #     for idsjnewukku in range(len(lst)):
                #         data = funct(lst[idsjnewukku], i, VWAP5)
                #         if data[0] == True:
                #             return {"BUY": True, "SELL": False}
                #         if data[1] == True:
                #             return {"BUY": False, "SELL": True}
                #     return {"BUY": False, "SELL": False}
                # lstcount = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
                # value = callAllFunct(lstcount, i, VWAP5)
                # if value['BUY']:
                #     previousBuy = True
                # elif value['SELL']:
                #     previousSell = True

                
                    
            try:
                print(pos, nuet, neg)
                print("POS/NEG RATIO: " + str(pos / neg))
                print(
                    "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                )
                print("CANDLES: " + str(len(data) - 2))
                print(
                    "PERCENT OF TRADES: "
                    + str(round(((pos + nuet + neg) / len(data)) * 100, 2))
                )
                print("protfilio: " + str(profilio))
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
            # print("Ratio: " + str(ratio))
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
        return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj
    except KeyboardInterrupt:
        print("BEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))


if "__main__" == __name__:
    f = open("documents/dataCryptoTest5min.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    # print(data)
    
    lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj = simulateCrypto(data, 1.5, 0.1)
    #720mi
    # 77mil
    # 200bil


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
