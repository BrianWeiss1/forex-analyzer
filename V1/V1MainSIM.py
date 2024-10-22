import random
from src.testEMA import calculate_200ema, greaterThenCurrent
from src.testMACD import get_macd
from src.testADX import grabADX
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from SpecialFunctions import formatDataset
from src.testSupertrend import get_supertrend

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
    dataRSI = get_rsi(data["close"], 14)
    dataRSI2 = get_rsi(data['close'], 9)
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
    correctBuy = True
    correctSell = True
    prevSellRSI = False
    prevBuyRSI = False

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
    stbuy5 = None
    previousSignal = None

    lst = []
    current = {}

    n = 0
    length = difference = 0

    # Loop to go through datapoints
    for j in range(100):
        st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
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
                if st5[i] > data["close"][i]:
                    stbuy5 = True
                elif st5[i] < data["close"][i]:
                    stbuy5 = False                
                
                if (
                    stbuy2 == True
                    and stbuy3 == True
                    and stbuy4 == True
                    and stbuy5 == True
                    # and EMAresult == True
                ):
                    signalSuper = "BUY"
                if (
                    stbuy2 == False
                    and stbuy3 == False
                    and stbuy4 == False
                    and stbuy5 == True
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



            # if prevBuy:
            #     if dataRSI["rsi_14"][i] < j and data['STOCHk_5_3_3'][i] < 100: #45, 100
            #         previousBuy = False
            #         continue
            #     else:
            #         previousBuy = True
            # if prevSell:
            #     if dataRSI["rsi_14"][i] < 91 and data["STOCHk_5_3_3"][i] > 67: # 47
            #         previousSell = False
            #         continue
            #     else:
            #         previousSell = True

            #---------IMPORTANT----------
            # if prevSell:
            #     if dataRSI["rsi_14"][i] < 45 or dataRSI["rsi_14"][i] > 55: # 47
            #         previousSell = False
            #         continue
            #     else:
            #         previousSell = True
            #-----IMPORTANT 80% sucess with 1% of trades



            change = "12.38"
            changeNeg = "-12.38"
            change = float(change)
            changeNeg = float(changeNeg)

            if prevBuy:
                if dataRSI["rsi_14"][i] < 55+changeNeg or dataRSI['rsi_14'][i] > 45+change: #45, 100
                    # previousBuy = False
                    prevBuyRSI = False
                    # continue
                else:
                    # previousBuy = True
                    prevBuyRSI = True
            if prevSell:
                if dataRSI["rsi_14"][i] < 55+changeNeg or dataRSI["rsi_14"][i] > 45+change: # 47
                    # previousSell = False
                    prevSellRSI = False
                    # continue
                else:
                    # previousSell = True
                    prevSellRSI = True
            if prevBuyRSI:
                previousBuy = True
            else:
                previousBuy = False
            
            if prevSellRSI:
                previousSell = True
            else:
                previousSell = False


            # if previousBuyRSI and previousSellRSI:
            #     print("A")
            # else:
            #     if previousSellRSI:
            #         previousSell = True
            #     if previousBuyRSI:
            #         previousBuy = True




            # if prevBuy:
            #     if dataRSI["rsi_14"][i] < 73 and data['STOCHk_5_3_3'][i] < 100: #45, 100
            #         previousBuy = False
            #         continue
            #     else:
            #         previousBuy = True
            # if prevSell:
            #     if dataRSI["rsi_14"][i] < 91 and data["STOCHk_5_3_3"][i] > 67: # 47
            #         previousSell = False
            #         continue
            #     else:
            #         previousSell = True


            if previousSell == True and previousBuy == True:
                previousBuy = False
                previousSell = False





                
        


        # If previous_position is "none":
        #     If macd_line crosses above signal_line:
        #         Set current_position to "buy"
        #         Set previous_position to "none"
        #     ElseIf macd_line crosses below signal_line:
        #         Set current_position to "sell"
        #         Set previous_position to "none"
        # Else If current_position is "buy":
        #     If macd_line crosses below signal_line:
        #         Set current_position to "sell"
        #         Set previous_position to "buy"
        # Else If current_position is "sell":
        #     If macd_line crosses above signal_line:
        #         Set current_position to "buy"
        #         Set previous_position to "sell"











                    #BEFORE:

                    # Percentage Correct: 0.5688822874118084
                    # CANDLES: 7032
                    # PERCENT OF TRADES: 0.3915268694910435

                    

                    # Percentage Correct: 65.76%
                    # CANDLES: 7032
                    # PERCENT OF TRADES: 14.47
                    # prevSell = 100
                    
                    # Percentage Correct: 63.88%
                    # CANDLES: 7032
                    # PERCENT OF TRADES: 15.33

                    # if dataRSI["rsi"][i] < 70 and data['STOCHk_5_3_3'][i] < 58:
                    #         previousBuy = False
                    #         continue
                    #     else:
                    #         previousBuy = True
                    # if prevSell:
                    #     if dataRSI["rsi"][i] < 70 and data["STOCHk_5_3_3"][i] > 76:
                    #         previousSell = False
                    #         continue
                    #     else:
                    #         previousSell = True
                    
                    
                    #INTO:
                    # if dataRSI["rsi"][i] < 70 and data["STOCHk_5_3_3"][i] > 80:
                        # Percentage Correct: 0.6036745406824147
                        # CANDLES: 7032
                        # PERCENT OF TRADES: 0.1661927779357407

                    # if dataRSI["rsi"][i] > 70 and data["STOCHk_5_3_3"][i] > 80:
                        # Percentage Correct: 0.5871238628411477
                        # CANDLES: 7032
                        # PERCENT OF TRADES: 0.2078475973841342


            #     #-----Uncomment: when supertrend code done------#
            #     RSIvalue = dataRSI['rsi'][i]
            #     ADXvalue = data['adx'][i]
            #     signal = None
            #     signal_list = obtainResult(lst, RSIvalue, current) # check 1 data BUY
            #     checkPusdo(current, RSIvalue) # check 1 data
            #     checkNextCandle, lst = findCandleNumber(current, 2) # solves for candle
            #     if signal_list != None:
            #         if "SELL" in signal_list and "BUY" in signal_list:
            #             signal_list = []
            #             signal = None
            #         elif "SELL" in signal_list:
            #             signal = "SELL"
            #         elif "BUY" in signal_list:
            #             signal = "BUY"

            #     if signal == "SELL":
            #         if ADXvalue > 10 and ADXvalue < 40:
            #             previousSell = True
            #     elif signal == 'BUY':
            #         if ADXvalue > 10 and ADXvalue < 40:
            #             previousBuy = True
            # #-----Uncomment: when supertrend code done------#

            # ----- uncomment this section -----
            # if macd_signal == 'SELL' and STOCHsignal == 'SELL':
            #     # if reverse != True:
            #     if dataRSI['rsi'][i] < 20:
            #         previousSell = True

            # if STOCHsignal == 'SELL':
            #     if dataRSI['rsi'][i] < 37:
            #         previousSell = True
            # ------ uncomment this section -------
        # print(macd_data)


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