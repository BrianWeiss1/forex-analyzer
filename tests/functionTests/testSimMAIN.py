import random
from src.functions.RSI import checkPusdo, findCandleNumber, obtainResult
from tests.functionTests.testEMA import calculate_200ema, greaterThenCurrent
from tests.functionTests.testMACD import get_macd
from tests.functionTests.testADX import grabADX
from tests.functionTests.testRSI import get_rsi
from tests.functionTests.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from tests.functionTests.testSpecial import formatDataset
from tests.functionTests.testSupertrend import get_supertrend

if "__main__" == __name__:
    # __INNIT__
    f = open("documents/dataSIM.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    data = formatDataset(data)
    ultimateData = data

    # Update data
    data = grabADX(data)
    ema = calculate_200ema(data, 200)
    rsiValue = 9
    dataRSI = get_rsi(data["close"], rsiValue)
    # dataRSI2 = get_rsi(data['close'], 9)
    macdData = get_macd(data, 12, 26, 9)
    data = get_stoch(ultimateData, 5, 3)
    data.drop(columns=['n_low', '%K', "%D"])
    # print(data)

    # print(dataRSI)

    # MACD setup
    macd_data = macdData.dropna()
    macd_signal = ""

    # STOCH setup
    data = data.dropna()

    # Supertrend setup
    st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 12, 3)
    st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 11, 2)
    st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 10, 1)

    previousBuy = False
    previousSell = False
    prevSellRSI = False
    prevBuyRSI = False
    prevBuySTOCH = False
    prevSellSTOCH = False
    correctBuy = True
    correctSell = True

    contempent = False
    
    pos = 0
    nuet = 0
    neg = 0

    number = 0
    BestProfilio = -1
    WorseProfilio = 10
    checkNextCandle = 0

    Bestj = -1
    Bestk = -1
    worstk = -1
    worstj = -1

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
    for j in range(100):
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
                    correctBuy == False
                previousBuy = False
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

            # if slope1 > 100 and slope2 > 0.07: # slope2 >, slope1  >
            #     macd_signal = "BUY"
            #     # print("BUY")
            # if slope2 < 0: # slope1 >, slope 2 >
            #     # print(slope1)
            #     macd_signal = "SELL"
            # if slope1 < 0:
            #     macd_signal = "SELL"
            #     # print("SELL")
            # reverse = False
            # if slope1 < -0.07:
            #     reverse == True

            # if dataRSI['rsi_14'][i-1] < 37 and dataRSI['rsi_14'][i] > 37:
            #     previousSell = True
            # if dataRSI['rsi'][i-1] < 67 and dataRSI['rsi'][i] > 67:
            #     previousBuy = True

            prevBuyRSI = False
            prevSellRSI = False
            contempent = False
            prevBuySTOCH = False
            prevSellSTOCH = False

            def SuperTrendEMA():
                prevBuy = prevSell = False
                signalSuper = ""

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
                        stbuy2 == True
                        and stbuy3 == True
                        and stbuy4 == True
                        and EMAresult == True
                    ):
                        signalSuper = "BUY"
                    if (
                        stbuy2 == False
                        and stbuy3 == False
                        and stbuy4 == False
                        and EMAresult == False
                    ):
                        signalSuper = "SELL"

                if signalSuper == "BUY":
                    prevBuy = True

                if signalSuper == "SELL":
                    prevSell = True

                return prevBuy, prevSell

            prevBuy, prevSell = SuperTrendEMA()

            if prevBuy:
                if dataRSI[f"rsi_{rsiValue}"][i] < 39 and data['STOCHk_5_3_3'][i] < 100: #45, 100
                    prevBuySTOCH = False
                else:
                    prevBuySTOCH = True
            if prevSell:
                if dataRSI[f"rsi_{rsiValue}"][i] < 95 and data["STOCHk_5_3_3"][i] > 47: # <95, 47
                    prevSellSTOCH = False
                else:
                    prevSellSTOCH = True

            #PREVIOUS: 80% at 7

            #-----Working Code-----#
            change = f"16.5"
            changeNeg = f"-16.5"
            change = float(change)
            changeNeg = float(changeNeg)

            if prevBuy:
                if dataRSI[f"rsi_{rsiValue}"][i] < 55+changeNeg or dataRSI[f'rsi_{rsiValue}'][i] > 45+change: #45, 100
                    # previousBuy = False
                    prevBuyRSI = False
                    # continue
                else:
                    # previousBuy = True
                    prevBuyRSI = True
            if prevSell:
                if dataRSI[f"rsi_{rsiValue}"][i] < 55+changeNeg or dataRSI[f"rsi_{rsiValue}"][i] > 45+change: # 47
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

    


        try:
            print(j)
            print(pos, nuet, neg)
            print("POS/NEG RATIO: " + str(pos / neg))
            print("Percentage Correct: " + str(round((pos / (neg + pos))*100, 2)) + "%")
            print("CANDLES: " + str(len(data) - 2))
            print("PERCENT OF TRADES: " + str(round(((pos + nuet + neg) / len(data))*100, 2)))
        except ZeroDivisionError:
            print("ERROR GO BRRRR")

        #------Profilio-----
        profilioSum = 0
        for i in range(200):
            profilio = 10
            betPercent = 0.1
            winRate = 1.7
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
            profilioSum+=profilio
        profilio = profilioSum/10
        print((profilio))
        if (profilio) > BestProfilio:
            BestProfilio = profilio
            # Bestk = k
            Bestj = j
        if profilio < WorseProfilio:
            WorseProfilio = profilio
            # worstk = k
            worstj = j
        pos = nuet = neg = 0


    print("BEST")
    print(BestProfilio)
    print(Bestj)
    print(Bestk)
    print("WORSE")
    print(WorseProfilio)
    print(worstj)
    print(worstk)