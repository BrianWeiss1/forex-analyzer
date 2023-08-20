import random
from tests.functionTests.testMACD import findMACDslope, findMACDslopeSIM, get_macd
from tests.functionTests.testADX import grabADX
from tests.functionTests.testGrabData import grabHistoricalData
from tests.functionTests.testRSI import get_rsi
from tests.functionTests.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from tests.functionTests.testSpecial import formatDataset

if '__main__' == __name__:
    f = open('documents/dataSIM.txt', 'r')
    data = f.readlines()
    data = eval(data[0])
    data = formatDataset(data)
    
    ultimateData = data
    previousBuy = previousSell = False
    neg = nuet = pos = 0
    BestProfilio = -1
    Bestj = Bestk = -1
    WorseProfilio = 10
    worstk = worstj = -1

    macd_signal = ""
    neg = nuet = pos = 0
    length = difference = 0

    # macdData = get_macd(data, 376, 200, 225)
    # macd_data = macdData.dropna()

    data = get_stoch(ultimateData, 52, 444)
    data = data.dropna()
    

    for i in range(41, len(data)-41):
        if previousBuy == True:
            if data['close'][i] < data['open'][i] : # check with i-1 too
                pos += 1
            elif data['close'][i] == data['open'][i]: # check with i-1 too
                nuet += 1
            else:
                neg += 1
            previousBuy = False
        if previousSell == True:
            if data['close'][i] > data['open'][i] :
                pos += 1
            elif data['close'][i] == data['open'][i]:
                nuet += 1
            else:
                neg += 1
            previousSell = False
        length = 0
        difference = 9
        STOCHsignal = getSTOCHdataSIM(data, length, difference, i, 52, 444)
        if STOCHsignal != None:
            continue
        slope1, slope2 = findMACDslopeSIM(macd_data, 31, 30, i)
        if slope1 > 0 and slope2 > 0:
            macd_signal = "BUY"
        if slope1 < 0 and slope2 < 0:
            macd_signal = "SELL"
        if macd_signal == 'SELL' and STOCHsignal == 'SELL':
            previousSell = True
        elif macd_signal == 'BUY' and STOCHsignal == 'BUY': 
            previousBuy = True
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
        Bestk = k
        Bestj = j
    if profilio < WorseProfilio:
        WorseProfilio = profilio
        worstk = k
        worstj = j
            
    print("BEST")
    print(BestProfilio)
    print(Bestj)
    print(Bestk)
    print("WORSE")
    print(WorseProfilio)
    print(worstj)
    print(worstk)



