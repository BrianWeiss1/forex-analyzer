
# Update data
from src.simulate import findPos, findPosLongTerm
from src.VWAP import get_VWAP
from src.specialFunctions import obtainResult
from src.testADX import grabADX
from src.testAroon import aroon
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch
from src.testSupertrend import get_supertrend, superTrend
import sys

from src.testSTOCHRSI import get_STOCHRSI
from src.testIchi import get_ichimoku
from src.testSpecial import formatDataset

def simuateLongterm(data):
    

    totalPips = 0
    countPips = 0


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
    k = -1
    j = -1
    bullish = None


    lst = []

    n = 0
    ichimoku = get_ichimoku(data)
    print(ichimoku)
    print(data)
    profilio = 10
    try:
        for k in range(0, 101):
            ich_change = 0
            ich_change = float(ich_change)
            print("K: " + str(k))
            ich_change = float(ich_change)

            for i in range(20, len(data) - 50):
                # if previousBuy:
                #     print(data['datetime'])
                pos, nuet, neg, profilio, totalPips, countPips = findPosLongTerm(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio, totalPips, countPips)
                previousBuy = False
                previousSell = False

                # if price greater then conversion and base line:
                    #BUY
                # if price less then conversion and base line
                    #SELL

                #compare this to with red and with green

                # previousSell = True
                # bullish = None
                # bearish = None

                # if ichimoku['a'][i] > ichimoku['b'][i]: # this one has 60% accuracy
                    # bullish = True

                # if data['close'][i] < ichimoku['b'][i] and ichimoku['b'][i] > ichimoku['a'][i]: # this one has 52%
                #     bearish = True

                # if bullish:
                #     previousBuy = True
                # else:
                #     previousBuy = False
                # if bearish and previousSell:
                #     previousSell = True
                # else:
                #     previousSell = False

                # if previousBuy and previousSell:
                #     previousSell = previousBuy = False
                # if price breaks ichimoku cloud:
                #     change in trend, 

                # if (data['close'][i-1] > ichimoku['b'][i-1]) and data['close'][i] < ichimoku['b'][i]:
                #     previousBuy = True

                # if (data['low'][i-1] > ichimoku['b'][i-1]) and data['close'][i] < ichimoku['b'][i]:
                #     previousBuy = True

                # if data['high'][i-1] < ichimoku['b'][i-1] and data['close'][i] > ichimoku['b'][i]:
                #     previousBuy = True

                if data['close'][i-1] > ichimoku['a'][i-1] and data['close'][i] < ichimoku['a'][i-1] :
                    previousBuy = True
          


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
                
            except ZeroDivisionError:
                print("ERROR GO BRRRR")
            # ------Profilio-----

            lst.append(profilio)
            # print(pos / (neg + pos))
            pos = nuet = neg = 0
            if profilio > BestProfilio:
                BestProfilio = profilio
                # Bestj = j
                Bestk = k
            elif profilio < WorseProfilio:
                WorseProfilio = profilio
                # worstj = j
                worstk = k
            profilio = 10
        #SEPERATE WHEN TABBING
        return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj
    except KeyboardInterrupt:
        print("BEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))






# if breaks through ichimoku cloud, then that signals a change in the trend
# price can bounch off of cloud (check high/low)
    #as long as it doesn't hit the end of the cloud, you guchii (check high/low)


#very usefuly
    # if it breaks then hits ittchu cloud, then u enter (check high/low)


#If one of these signals are confirmation, then buy
if __name__ == '__main__':
    f = open("documents/dataCryptoTest.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    lst, bestProfilio, Wostprofilio, BestK, Bestj, worstk, worstj = simuateLongterm(data)

    print("\n" + str(bestProfilio))
    print("BEST J: " + str(Bestj))
    print("BEST K: " + str(BestK))

    print("\n" + str(Wostprofilio))
    print("WORST J: " + str(worstj))
    print("WORST K: " + str(worstk))