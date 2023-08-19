from tests.functionTests.testMACD import findMACDslope, findMACDslopeSIM, get_macd
from tests.functionTests.testADX import grabADX
from tests.functionTests.testGrabData import grabHistoricalData
from tests.functionTests.testRSI import get_rsi
from tests.functionTests.testSTOCH import get_stoch, getSTOCHdata, getSTOCHdataSIM
from tests.functionTests.testSpecial import formatDataset

if '__main__' == __name__:
    symbol = "EURJPY"
    data = grabHistoricalData(symbol)
    data = formatDataset(data)
    data = get_stoch(data, 100, 3)
    macdData = get_macd(data, 1, 15, 1)
    data = data.dropna()
    macd_data = macdData.dropna()
    previousBuy = previousSell = False
    neg = nuet = pos = 0
    macd_signal = ""
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
        difference = 1
        STOCHsignal = getSTOCHdataSIM(data, 4, 0, i)
        if STOCHsignal == None:
            continue
        slope1, slope2 = findMACDslopeSIM(macd_data, 2, 2, i)
        if slope1 > 0 and slope2 > 0:
            macd_signal = "BUY"
        if slope1 < 0 and slope2 < 0:
            macd_signal = "SELL"
        if macd_signal == 'SELL' and STOCHsignal == 'SELL':
            # print("SELL")
            previousSell = True
        elif macd_signal == 'BUY' and STOCHsignal == 'BUY': 
            # print("BUY")
            previousBuy = True
    print(pos, nuet, neg)
    print("POS/NEG RATIO: " + str(pos/neg))
    print("Percentage Correct: " + str(pos/(neg+pos)))
    print("CANDLES: " + str(len(data)-2))
    print("PERCENT OF TRADES: " + str((pos+nuet+neg)/len(data)))
    print(str(length) + ", " + str(difference) + ":   STOCH")