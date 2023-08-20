import random
from src.functions.RSI import checkPusdo, findCandleNumber, obtainResult
from tests.functionTests.testMACD import findMACDslope, findMACDslopeSIM, get_macd
from tests.functionTests.testADX import grabADX
from tests.functionTests.testGrabData import grabHistoricalData
from tests.functionTests.testRSI import get_rsi
from tests.functionTests.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from tests.functionTests.testSpecial import formatDataset

if '__main__' == __name__:
    # symbol = "EURJPY"
    # data = grabHistoricalData(symbol)
    f = open('documents/dataSIM.txt', 'r')
    data = f.readlines()
    data = eval(data[0])
    data = formatDataset(data)
    ultimateData = data
    previousBuy = previousSell = False
    neg = nuet = pos = number = 0
    BestProfilio = -1
    checkNextCandle = 0
    Bestj = Bestk = -1
    macd_signal = ""
    macdData = get_macd(data, 1, 15, 1) # 376, 200, 225
    macd_data = macdData.dropna()
    data = get_stoch(ultimateData, 5, 3)
    data = data.dropna()
    WorseProfilio = 10
    worstk = worstj = -1
    lst = []
    dataRSI = get_rsi(data, data['close'], 14)

    # print(data)
    # dataRSI.loc['rsi_14'] = get_rsi(data, data['close'], 14)
    current = {}

    n = 0
    macd_signal = ""
    neg = nuet = pos = 0
    length = difference = 0
    for i in range(41, len(data)-41):
        if previousBuy == True:
            if data['close'][i+n] < data['open'][i+n] : # check with i-1 too
                pos += 1
                # print("correct")
            elif data['close'][i+n] == data['open'][i+n]: # check with i-1 too
                nuet += 1
            else:
                neg += 1
                # print("innocrect")
            previousBuy = False
        if previousSell == True:
            if data['close'][i+n] > data['open'][i+n] :
                pos += 1
                # print('correct')
            elif data['close'][i+n] == data['open'][i+n]:
                nuet += 1
            else:
                neg += 1
                # print('incorrect')
            previousSell = False
        length = 0
        difference = 8
        STOCHsignal = getSTOCHdataSIM(data, length, difference, i, 5, 3) # 52 444
        # print(STOCHsignal)
        slope1, slope2 = findMACDslopeSIM(macd_data, 4, 20, i) # 31, 30, 
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
        #     print("AAAAAAAA\n\\n\n\\nAAAAA")



        # if dataRSI['rsi_14'][i-1] < 37 and dataRSI['rsi_14'][i] > 37:
        #     previousSell = True
        # if dataRSI['rsi'][i-1] < 67 and dataRSI['rsi'][i] > 67:
        #     previousBuy = True
        RSIvalue = dataRSI['rsi'][i]
        signal = None
        signal_list = obtainResult(lst, RSIvalue, current) # check 1 data BUY
        checkPusdo(current, RSIvalue) # check 1 data
        checkNextCandle, lst = findCandleNumber(current, 2) # solves for candle
        if signal_list != None:
            if "SELL" in signal_list and "BUY" in signal_list:
                signal_list = []
                signal = None
            elif "SELL" in signal_list:
                signal = "SELL"
            elif "BUY" in signal_list:
                signal = "BUY"

        if signal == "SELL":
            if RSIvalue > 60 or RSIvalue < 40:
            # if RSIvalue > 60 or RSIvalue < 40:
                previousSell = True
        elif signal == 'BUY':
            if RSIvalue > 60 or RSIvalue < 40:
                previousBuy = True
        

        #----- uncomment this section -----
        # if macd_signal == 'SELL' and STOCHsignal == 'SELL':
        #     # if reverse != True:
        #     if dataRSI['rsi'][i] < 20:
        #         previousSell = True

        # if STOCHsignal == 'SELL':
        #     if dataRSI['rsi'][i] < 37:
        #         previousSell = True
        # ------ uncomment this section -------


        '''
        POS/NEG RATIO: 1.2079207920792079
        Percentage Correct: 0.547085201793722
        CANDLES: 6943
        PERCENT OF TRADES: 0.16371490280777537
        
        '''
    try:
        print(pos, nuet, neg)
        print("POS/NEG RATIO: " + str(pos/neg))
        print("Percentage Correct: " + str(pos/(neg+pos)))
        print("CANDLES: " + str(len(data)-2))
        print("PERCENT OF TRADES: " + str((pos+nuet+neg)/len(data)))
        print(str(length) + ", " + str(difference) + ":   STOCH")
    except ZeroDivisionError:
        print("ERROR GO BRRRR")

    profilio = 10
    betPercent = 0.1
    winRate = 2
    for i in range(pos+neg+nuet):
        bet = betPercent*profilio
        profilio = profilio-(bet)
        randomNum = random.randint(0, pos+nuet+neg)
        if randomNum <= neg: #negitive
            profilio = profilio
        elif randomNum <= neg+nuet: #nuetrol
            profilio = profilio+(bet)
        else:
            profilio = profilio+(bet*winRate)
    print((profilio))
    if (profilio) > BestProfilio:
        BestProfilio = profilio
        # Bestk = k
        # Bestj = j
    if profilio < WorseProfilio:
        WorseProfilio = profilio
        # worstk = k
        # worstj = j
            
    # print("BEST")
    # print(BestProfilio)
    # print(Bestj)
    # print(Bestk)
    # print("WORSE")
    # print(WorseProfilio)
    # print(worstj)
    # print(worstk)



