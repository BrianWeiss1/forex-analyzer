import random
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
    neg = nuet = pos = 0
    BestProfilio = 0
    Bestj = Bestk = -1
    macd_signal = ""
    macdData = get_macd(data, 1, 15, 1)
    macd_data = macdData.dropna()
    for j in range(1000):
        for k in range(15):
            neg = nuet = pos = 0
            data = get_stoch(ultimateData, j, k)
            data = data.dropna()
            length = difference = 0
            for i in range(len(data)-10):
                if previousBuy == True:
                    if data['close'][i] < data['open'][i] :
                        neg += 1
                    elif data['close'][i] == data['open'][i]:
                        nuet += 1
                    else:
                        pos += 1
                    previousBuy = False
                if previousSell == True:
                    if data['close'][i] > data['open'][i] :
                        neg += 1
                    elif data['close'][i] == data['open'][i]:
                        nuet += 1
                    else:
                        pos += 1
                    previousSell = False
                length = 4
                difference = 0
                STOCHsignal = getSTOCHdataSIM(data, length, difference, i, j)
                if STOCHsignal == None:
                    continue
                slope1, slope2 = findMACDslopeSIM(macd_data, 2, 5, i)
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
            winRate = 1.5
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
            if (profilio) > BestProfilio:
                BestProfilio = profilio
                Bestj = j
                Bestk = k
                # Bestk = k
            

    print(BestProfilio)
    print(Bestj)
    print(Bestk)



