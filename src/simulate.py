
# Update data
import random
from src.VWAP import get_VWAP
from src.specialFunctions import obtainResult
from src.testADX import grabADX
from src.testAroon import aroon
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch
from src.testSupertrend import get_supertrend, superTrend
import sys


def simulate(data, avgResult, avgInput):
    ultimateData = data
    data = grabADX(data, 14)
    # print(data)
    # ema = calculate_200ema(data, 200)
    aroonData = aroon(data, 14)
    rsiValue = 10
    dataRSI = get_rsi(data["close"], rsiValue)
    # dataRSI2 = get_rsi(data["close"], 9)
    # macdData = get_macd(data, 12, 26, 9)
    data = get_stoch(ultimateData, 5, 3)

    # print(dataRSI)

    # MACD setup
    # macd_data = macdData.dropna()
    # macd_signal = ""

    # STOCH setup
    data = data.dropna()

    # Supertrend setup
    st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
    st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
    st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 1) #change to 2
    st7, upt7, dt7 = get_supertrend(data["high"], data["low"], data["close"], 65, 1)


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
    stbuy = None
    stbuy1 = None
    stbuy2 = None
    stbuy3 = None
    stbuy4 = None
    stbuy5 = None
    stbuy6 = None
    stbuy7 = None
    previousSignal = None

    lst = []
    current = {}

    n = 0
    length = difference = 0

    # Loop to go through datapoints
    # for j in range(1, 101):
    # for j in range(1, 101):




    profilio = 10
    for k in range(1, 101):
        for i in range(10, len(data) - 10):
            
            pos, nuet, neg, profilio = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio)
            previousSell = previousBuy = False
            previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)
            
        


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
        except ZeroDivisionError:
            print("ERROR GO BRRRR")
        # ------Profilio-----

        pos = nuet = neg = 0
        lst.append(profilio)
        if profilio > BestProfilio:
            BestProfilio = profilio
            # Bestj = j
            Bestk = k
        elif profilio < WorseProfilio:
            WorseProfilio = profilio
            # worstj = j
            worstk = k
        profilio = 10
        #HERE
    return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj

def findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio):
    betPercent = 0.19066666666666666
    winRate = 1.6
    p = 0.7818
    q = 1-p
    b = winRate-1
    f = p - (q/b)
    betPercent = f
    # print(betPercent)
    bet = 0
    if previousBuy == True:
        bet = betPercent * profilio
        profilio = profilio - (bet)
        if data["close"][i + n] < data["open"][i + n]:
            pos += 1
            profilio = profilio + (bet * winRate)
        elif data["close"][i + n] == data["open"][i + n]:
            nuet += 1
            profilio = profilio + (bet)
        else:
            neg += 1
        previousBuy = False
    if previousSell == True:
        bet = betPercent * profilio
        profilio = profilio - (bet)
        if data["close"][i + n] > data["open"][i + n]:
            pos += 1
            profilio = profilio + (bet * winRate)
        elif data["close"][i + n] == data["open"][i + n]:
            nuet += 1
            profilio = profilio + (bet)
        else:
            neg += 1
        previousSell = False
    return pos, nuet, neg, profilio
def simulateCrypto(data, avgResult, avgInput):
    
    ultimateData = data
    data = grabADX(data, 14)
    # print(data)
    # ema = calculate_200ema(data, 200)
    VWAPdata = get_VWAP(data, 5)
    aroonData = aroon(data, 14)
    # dataRSI2 = get_rsi(data["close"], 9)
    # macdData = get_macd(data, 12, 26, 9)
    rsiValue = 8
    dataRSI = get_rsi(data["close"], rsiValue)
    data = get_stoch(ultimateData, 5, 3)

    # print(dataRSI)

    # MACD setup
    # macd_data = macdData.dropna()
    # macd_signal = ""

    # STOCH setup
    data = data.dropna()

    # Supertrend setup
    # def getSupertrend():

    st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
    st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
    st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 2) #change to 2
    st7, upt7, dt7 = get_supertrend(data["high"], data["low"], data["close"], 65, 1)

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

    # Loop to go through datapoints
    # for j in range(1, 101):
    # for j in range(1, 101):

    st10 = superTrend(data, 2, 87) # 2, 87
    # st11 = superTrend(data, 6, 1)
    change = -7

    profilio = 10
    try:
        for k in range(1, 501):
            print("K: " + str(k))
            for j in range(1, 100):
                st10 = superTrend(data, k, j)
                for i in range(10, len(data) - 10):
                    
                    pos, nuet, neg, profilio = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio)
                    previousSell = previousBuy = False
                    previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)

                    if VWAPdata[i] > data['close'][i]+change and previousSell:
                        #only sell
                        previousSell = True
                    else:
                        previousSell = False
                    if VWAPdata[i]+change < data['close'][i] and previousBuy:
                        #only buy
                        previousBuy = True
                    else:
                        previousBuy = False
                    if st10[i] > data['close'][i] and previousBuy:
                        previousBuy = True
                    else:
                        previousBuy = False
                    if st10[i] < data['close'][i] and previousSell:
                        previousSell = True
                    else:
                        previousSell = False
                        
                # try:
                #     print(pos, nuet, neg)
                #     print("POS/NEG RATIO: " + str(pos / neg))
                #     print(
                #         "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                #     )
                #     print("CANDLES: " + str(len(data) - 2))
                #     print(
                #         "PERCENT OF TRADES: "
                #         + str(round(((pos + nuet + neg) / len(data)) * 100, 2))
                #     )
                #     print("protfilio: " + str(profilio))
                # except ZeroDivisionError:
                #     print("ERROR GO BRRRR")
                # ------Profilio-----

                pos = nuet = neg = 0
                lst.append(profilio)
                if profilio > BestProfilio:
                    BestProfilio = profilio
                    Bestj = j
                    Bestk = k
                elif profilio < WorseProfilio:
                    WorseProfilio = profilio
                    worstj = j
                    worstk = k
                profilio = 10
        #SEPERATE WHEN TABBING
        return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj
    except KeyboardInterrupt:
        print("BEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
