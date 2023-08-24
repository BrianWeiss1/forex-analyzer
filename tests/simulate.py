
# Update data
import random
from tests.simulate2 import obtainResult
from tests.testADX import grabADX
from tests.testAroon import aroon
from tests.testRSI import get_rsi
from tests.testSTOCH import get_stoch
from tests.testSupertrend import get_supertrend
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

            if data['adx'][i] < 15:
                previousBuy = False
                previousSell = False
            # if previousBuy == True:
            #     if data['adx'][i] < 59 or data['adx'][i] > 7:
            #         previousBuy = True
            #     else:
            #         previousBuy = False
            # if previousSell == True:
            #     if data['adx'][i] < 76 or data['adx'][i] > 6:
            #         previousSell = True
            #     else:
            #         previousSell = False            
            # if aroonData['aroon_indicator'][i] <= 8:
            #     previousBuy = True
            # if aroonData['aroon_indicator'][i] >= 98:
            #     previousSell = True

            # if both are below 50%: colosiating
            # 30% and 70%
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
    return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj

def findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio):
    betPercent = 0.19066666666666666
    winRate = 1.6
        #Kelly Criterium:
        # p = 0.6965
        # q = 1-p
        # b = winRate-1
        # f = p - (q/b)
        # betPercent = f
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
