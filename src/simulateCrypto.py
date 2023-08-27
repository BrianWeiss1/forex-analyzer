
# Update data
from src.simulate import findPos
from src.VWAP import get_VWAP
from src.specialFunctions import obtainResult
from src.testADX import grabADX
from src.testAroon import aroon
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch
from src.testSupertrend import get_supertrend, superTrend
import sys

from src.testSTOCHRSI import get_STOCHRSI

def simulateCrypto(data, avgResult, avgInput):
    
    ultimateData = data
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

    st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
    st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
    st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 1) #change to 2
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
    st10 = superTrend(data, 1, 1) # 2, 87
    VWAP5 = get_VWAP(data, 5)
    # Loop to go through datapoints
    # for j in range(1, 101):
    # for j in range(1, 101):

    # st11 = superTrend(data, 6, 1)
    VWAPdata = get_VWAP(data, 1)
    profilio = 10
    try:
        for k in range(-101, 101):
            print("K: " + str(k))
            change = k
            # for j in range(1, 100):
            for i in range(10, len(data) - 10):
                
                pos, nuet, neg, profilio, totalPips, countPips = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio, totalPips, countPips)
                previousSell = previousBuy = False
                previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)

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
                # # if  
                def funct(num, i, VWAP5):
                    if VWAP5[i] > data['close'][i]+num:
                        prevSell = True
                    else:
                        prevSell = False
                    if VWAPdata[i] + change < data['close'][i] and previousBuy:
                        #only buy
                        prevBuy = True
                    else:
                        prevBuy = False
                    return prevBuy, prevSell
                def callAllFunct(lst, i, VWAP5):
                    for idsjnewukku in range(len(lst)):
                        data = funct(lst[idsjnewukku], i, VWAP5)
                        if data[0] == True:
                            return {"BUY": True, "SELL": False}
                        if data[1] == True:
                            return {"BUY": False, "SELL": True}
                    return {"BUY": False, "SELL": False}
                # lstcount = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
                # value = callAllFunct(lstcount, i, VWAP5)
                # if value['BUY']:
                #     previousBuy = True
                # elif value['SELL']:
                #     previousSell = True

                ''' AT VWAP 5
                K: 7
138 0 41
POS/NEG RATIO: 3.3658536585365852
Percentage Correct: 77.09%
CANDLES: 14987
PERCENT OF TRADES: 1.19
AVERAGE PIPS: 490.66515436985947
Ratio: 23.185912357048878
K: 8
104 0 26
POS/NEG RATIO: 4.0
Percentage Correct: 80.0%
CANDLES: 14987
PERCENT OF TRADES: 0.87
AVERAGE PIPS: 490.74487276476214
Ratio: 20.175527085645115
K: 9
82 0 20
POS/NEG RATIO: 4.1
Percentage Correct: 80.39%
CANDLES: 14987
PERCENT OF TRADES: 0.68
AVERAGE PIPS: 490.8047714445626
Ratio: 19.744260974627466
K: 10
61 0 14
POS/NEG RATIO: 4.357142857142857
Percentage Correct: 81.33%
CANDLES: 14987
PERCENT OF TRADES: 0.5
AVERAGE PIPS: 490.8770960698243
Ratio: 18.763819095477388
K: 11
45 0 10
POS/NEG RATIO: 4.5
Percentage Correct: 81.82%
CANDLES: 14987
PERCENT OF TRADES: 0.37
AVERAGE PIPS: 490.938906359631
Ratio: 18.24751580849143
K: 12
39 0 6
POS/NEG RATIO: 6.5
Percentage Correct: 86.67%
CANDLES: 14987
PERCENT OF TRADES: 0.3
AVERAGE PIPS: 490.9998392310501
Ratio: 13.370110330992976
K: 13
29 0 4
POS/NEG RATIO: 7.25
Percentage Correct: 87.88%
CANDLES: 14987
PERCENT OF TRADES: 0.22
AVERAGE PIPS: 491.0607775257159
Ratio: 12.146722790138309
K: 14
19 0 1
POS/NEG RATIO: 19.0
Percentage Correct: 95.0%
CANDLES: 14987
PERCENT OF TRADES: 0.13
AVERAGE PIPS: 491.1228671947612
Ratio: 5.006508460999299
K: 15
15 0 1
POS/NEG RATIO: 15.0
Percentage Correct: 93.75%
CANDLES: 14987
PERCENT OF TRADES: 0.11
AVERAGE PIPS: 491.17132027923384
Ratio: 6.256882570827911
K: 16
11 0 1
POS/NEG RATIO: 11.0
Percentage Correct: 91.67%
CANDLES: 14987
PERCENT OF TRADES: 0.08
AVERAGE PIPS: 491.19481400125346
Ratio: 8.336669335468374
K: 17
7 0 1
POS/NEG RATIO: 7.0
Percentage Correct: 87.5%
CANDLES: 14987
PERCENT OF TRADES: 0.05
AVERAGE PIPS: 491.2145910732522
Ratio: 12.506253126563283
K: 18
7 0 1
POS/NEG RATIO: 7.0
Percentage Correct: 87.5%
CANDLES: 14987
PERCENT OF TRADES: 0.05
AVERAGE PIPS: 491.2343667108891
Ratio: 12.506253126563283
K: 19
6 0 1
POS/NEG RATIO: 6.0
Percentage Correct: 85.71%
CANDLES: 14987
PERCENT OF TRADES: 0.05
AVERAGE PIPS: 491.24552797913174
Ratio: 14.29714857428715
K: 20
5 0 1
POS/NEG RATIO: 5.0
Percentage Correct: 83.33%
CANDLES: 14987
PERCENT OF TRADES: 0.04
AVERAGE PIPS: 491.24647623774024
Ratio: 16.67667066826731
K: 21
4 0 1
POS/NEG RATIO: 4.0
Percentage Correct: 80.0%
CANDLES: 14987
PERCENT OF TRADES: 0.03
AVERAGE PIPS: 491.2465526359083
Ratio: 20.00600180054016
K: 22

                '''

                
                    
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
                # print("protfilio: " + str(profilio))
                print("AVERAGE PIPS: " + str(totalPips/countPips))
            except ZeroDivisionError:
                print("ERROR GO BRRRR")
            # ------Profilio-----

            lst.append(profilio)
            # print(pos / (neg + pos))
            try:
                ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            except ZeroDivisionError:
                ratio = 0
            pos = nuet = neg = 0
            print("Ratio: " + str(ratio))
            if ratio > BestProfilio:
                BestProfilio = ratio
                # Bestj = j
                Bestk = k
            elif ratio < WorseProfilio:
                WorseProfilio = ratio
                # worstj = j
                worstk = k
            profilio = 10
        #SEPERATE WHEN TABBING
        return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj
    except KeyboardInterrupt:
        print("BEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))


