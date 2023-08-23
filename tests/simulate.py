
# Update data
import random
from tests.simulate2 import obtainResult
from tests.testADX import grabADX
from tests.testRSI import get_rsi
from tests.testSTOCH import get_stoch
from tests.testSupertrend import get_supertrend
import sys


def simulate(data, avgResult, avgInput):
    ultimateData = data
    data = grabADX(data)
    # ema = calculate_200ema(data, 200)
    rsiValue = 10
    dataRSI, dataRSI2 = get_rsi(data["close"], rsiValue)
    dataRSI3, dataRSI4 = get_rsi(data["close"], rsiValue)
    # dataRSI2 = get_rsi(data["close"], 9)
    # macdData = get_macd(data, 12, 26, 9)
    data = get_stoch(ultimateData, 5, 3)
    # print(dataRSI)
    print(dataRSI2)

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
    for j in range(1, 101):
        rsiValue2 = j
        # dataRSI3, dataRSI4 = get_rsi(data["close"], rsiValue)
        # print(dataRSI3)
        for i in range(40, len(data) - 40):
            j = 0
            
            
            pos, nuet, neg = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg)
            previousSell = previousBuy = False
            previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue, j)
            prevBuyRSI = None
            if 



            # -------RSI canvus 82%: 4%-------#
            # if dataRSI3[f'rsi_{rsiValue}'][i] > dataRSI4[f'rsi_{rsiValue}'][i]:
            #     prevBuyRSI = False
            # if dataRSI3[f'rsi_{rsiValue}'][i] > dataRSI4[f'rsi_{rsiValue}'][i]:
            #     prevBuyRSI = True
            # if prevBuyRSI:
            #     previousBuy = True
            # if not prevBuyRSI:
            #     previousSell = True
            #--------RSI Canvas--------#



            



        try:
            print(j)
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
        except ZeroDivisionError:
            print("ERROR GO BRRRR")

        # ------Profilio-----

        pos *=2
        neg*=2
        nuet*= 2
        profilioSum = 0
        for i in range(1):
            profilio = 10
            betPercent = 0.1
            winRate = 1.5
            for i in range(pos + neg + nuet):
                bet = betPercent * profilio
                profilio = profilio - (bet)
                randomNum = random.randint(0, pos + nuet + neg)
                if randomNum <= neg:  # negitive
                    profilio = profilio
                elif randomNum <= neg + nuet:  # nuetrol
                    profilio = profilio + (bet)
                else:
                    profilio = profilio + (bet * winRate)
            profilioSum += profilio
        profilio = profilioSum / 10
        # print((profilio))
        lst.append(profilio)
        if (profilio) > BestProfilio:
            BestProfilio = profilio
            # Bestk = k
            Bestj = j
        if profilio < WorseProfilio:
            WorseProfilio = profilio
            # worstk = k
            worstj = j
        pos = nuet = neg = 0
    return lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj

def findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg):
    if previousBuy == True:
        if data["close"][i + n] < data["open"][i + n]:
            pos += 1
        elif data["close"][i + n] == data["open"][i + n]:
            nuet += 1
        else:
            neg += 1
        previousBuy = False
    if previousSell == True:
        if data["close"][i + n] > data["open"][i + n]:
            pos += 1
        elif data["close"][i + n] == data["open"][i + n]:
            nuet += 1
        else:
            neg += 1
        previousSell = False
    return pos, nuet, neg