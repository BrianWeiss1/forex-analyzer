import random
from src.testEMA import calculate_200ema, greaterThenCurrent
from src.testMACD import get_macd
from src.testADX import grabADX
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from src.testSpecial import formatDataset
from src.testSupertrend import get_supertrend
from src.testIchi import get_ichimoku

if "__main__" == __name__:
    # __INNIT__
    f = open("documents/dataCrypto.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    data = formatDataset(data)
    ultimateData = data

    # Update data
    data = grabADX(data, 14)
    ema = calculate_200ema(data, 200)
    rsiValue = 10
    dataRSI = get_rsi(data["close"], rsiValue)
    rsiValue2 = 5
    dataRSI2 = get_rsi(data["close"], rsiValue2)
    macdData = get_macd(data, 12, 26, 9)
    data = get_stoch(ultimateData, 5, 3)
    data.drop(columns=["n_low", "%K", "%D"])
    ichimoku = get_ichimoku(data)
    # print(data)

    # print(dataRSI)

    # MACD setup
    macd_data = macdData.dropna()
    macd_signal = ""

    # STOCH setup
    data = data.dropna()

    # Supertrend setup
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 40, 2)
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 30, 2)
    st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 3, 3)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
    # st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
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
    BestProfilio = -1
    WorseProfilio = 10000000000000000000000000000000000000000000000000000
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
    previousSignal = None

    lst = []
    current = {}

    n = 0
    length = difference = 0

    # Loop to go through datapoints
    for j in range(1, 101):
        for i in range(41, len(data) - 41):
            # Check for previous decision: then check if correct or incorrect
            if previousBuy == True:
                if data["close"][i + n] < data["open"][i + n]:
                    pos += 1
                    correctBuy == True
                    # print("correct BUY: " + str(ADXvalue))
                elif data["close"][i + n] == data["open"][i + n]:
                    nuet += 1
                else:
                    neg += 1
                    # print("INNCORECT BUY: " + str(ADXvalue))
                    previousBuy = False
                    correctBuy == False
            if previousSell == True:
                if data["close"][i + n] > data["open"][i + n]:
                    pos += 1
                    # print("CORRECT SELL: " + str(ADXvalue))
                    correctSell == True
                elif data["close"][i + n] == data["open"][i + n]:
                    nuet += 1
                else:
                    neg += 1
                    correctSell == False
                    # print("INNCORECT SELL: " + str(ADXvalue))
                previousSell = False

            ADXvalue = data["adx"][i]
            stochastic_signal = getSTOCHdataSIM(data, 0, 8, i, 5, 3)  # 52 444
            currentEMA = ema[i]
            currentPrice = data["close"][i]
            EMAresult = greaterThenCurrent(currentEMA, currentPrice)

            prevBuyRSI = False
            prevSellRSI = False
            prevSellSTOCH = None
            prevBuySTOCH = None

            def SuperTrendEMA():
                prevBuy = prevSell = False
                signalSuper = ""
                if st[i] > data["close"][i]:
                    stbuy = True
                elif st[i] < data["close"][i]:
                    stbuy = False

                if st2[i] > data["close"][i]:
                    stbuy2 = True
                elif st2[i] < data["close"][i]:
                    stbuy2 = False
                if st3[i] > data["close"][i]:
                    stbuy3 = True
                elif st3[i] < data["close"][i]:
                    stbuy3 = False
                if st4[i] > data["close"][i]:
                    stbuy4 = True
                elif st4[i] < data["close"][i]:
                    stbuy4 = False

                if EMAresult != None:
                    if (
                        stbuy == True
                        and stbuy2 == True
                        and stbuy3 == True
                        and stbuy4 == True
                        # and EMAresult == True
                    ):
                        signalSuper = "BUY"
                    if (
                        stbuy == False
                        and stbuy2 == False
                        and stbuy3 == False
                        and stbuy4 == False
                        # and EMAresult == False
                    ):
                        signalSuper = "SELL"

                if signalSuper == "BUY":
                    prevBuy = True

                if signalSuper == "SELL":
                    prevSell = True

                return prevBuy, prevSell

            prevBuy, prevSell = SuperTrendEMA()
            Dataset = [prevBuy, prevSell]

            if prevSell:
                if dataRSI[f"rsi_{rsiValue}"][i] > 36 and data["STOCHk_5_3_3"][i] > 36: # <95, 47
                    prevSellSTOCH = False
                else:
                    prevSellSTOCH = True
             
            # if prevBuy:
            #     if dataRSI2[f"rsi_{rsiValue2}"][i] > j and ADXvalue > j: # <95, 47
            #         prevBuySTOCH = False
            #     else:
            #         prevBuySTOCH = True

            # -----RSI--------#
            change = f"9.41"
            changeNeg = f"-9.41"
            change = float(change)
            changeNeg = float(changeNeg)

            if prevBuy:
                if (
                    dataRSI[f"rsi_{rsiValue}"][i] < 56 + changeNeg
                    or dataRSI[f"rsi_{rsiValue}"][i] > 43 + change
                ):  # 45, 100
                    # previousBuy = False
                    prevBuyRSI = False
                    # continue
                else:
                    # previousBuy = True
                    prevBuyRSI = True
            if prevSell:
                if (
                    dataRSI[f"rsi_{rsiValue}"][i] < 56 + changeNeg
                    or dataRSI[f"rsi_{rsiValue}"][i] > 43 + change
                ):  # 47
                    # previousSell = False
                    prevSellRSI = False
                    # continue
                else:
                    # previousSell = True
                    prevSellRSI = True

            #compareitivness
            if prevBuyRSI and prevSellRSI:
                prevSell = False
                prevBuy = False
            if prevBuyRSI:
                previousBuy = True
            else:
                previousBuy = False
            
            if prevSellRSI:
                previousSell = True
            else:
                previousSell = False
            
            if previousSell == True and previousBuy == True:
                previousBuy = False
                previousSell = False
                contempent = True

            #------Working code-------#

            if not contempent:
                if prevBuySTOCH and prevSellSTOCH:
                    prevBuySTOCH = False
                    prevSellSTOCH = False
                if prevBuySTOCH:
                    previousBuy = True
                if prevSellSTOCH:
                    previousSell = True

            #contentment
            if previousSell == True and previousBuy == True:
                previousBuy = False
                previousSell = False
                contempent = True


            # if data['close'][i] < ichimoku['base'][i] and previousBuy:
            #     previousBuy = True
            # else:
            #     previousBuy = False
            # if data['close'][i] > ichimoku['base'][i] and previousSell:
            #     previousSell = True
            # else:
            #     previousSell = False

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
        print((profilio))
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

    print("Average Result: " + str(average))
    print("Median Result: " + str(median))

    print("Best Profilio: " + str(BestProfilio))
    print("J:" + str(Bestj))
    print("K: " + str(Bestk))
    print("Best Profilio: " + str(WorseProfilio))
    print("J: " + str(worstj))
    print("K: " + str(worstk))