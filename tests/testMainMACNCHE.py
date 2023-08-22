from tests.functionTests.testMACD import findMACDslope, get_macd
from tests.functionTests.testADX import grabADX
from tests.functionTests.testGrabData import grabHistoricalData
from tests.functionTests.testRSI import get_rsi
from tests.functionTests.testSTOCH import get_stoch, getSTOCHdata
from tests.functionTests.testSpecial import formatDataset

if '__main__' == __name__:
    symbol = "EURJPY"
    while(True):
        data = grabHistoricalData(symbol)
        data = formatDataset(data)

        ADXdata = grabADX(data)
        STOCHdata = get_stoch(data, 100, 3)
        print(STOCHdata)
        STOCHsignal = getSTOCHdata(STOCHdata, 2, 4)
        if STOCHsignal == None:
            break
        data['rsi_14'] = get_rsi(data['close'], 14)
        data = data.dropna()
        # print(data)
        macd_data = get_macd(data, 1, 15, 1)
        # print(macd_data)
        slope1, slope2 = findMACDslope(macd_data, 3, 5)
        if slope1 > 0 and slope2 > 0:
            macd_signal = "BUY"
        if slope1 < 0 and slope2 < 0:
            macd_signal = "SELL"
        if macd_signal == 'SELL' and STOCHsignal == 'SELL':
            print("SELL")
        elif macd_signal == 'BUY' and STOCHsignal == 'BUY': 
            print("BUY")
        


    '''
    If MACD last 3 candles + (only buy)
    If MACD last 5 candles + (only buy)

    If MADC last 3 candles - (only sell)
    If MACD last 5 candles - (only sell)


    If STOCH for last 2 candles BUY: 
    BUY
    if STOCH for last 2 candles SELL:
    SELL
    If MADC and STOCH !=
    Dont do anything
    else
    Do corresponing signa

    '''

