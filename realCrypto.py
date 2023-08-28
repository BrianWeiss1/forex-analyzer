from datetime import datetime
import sys
import time
from src.specialFunctions import automaticBuy, automaticSell, obtainResult

from src.testGrabData import grabCurrentDataBTC, grabHistoricalDataBTC
from src.testRSI import get_rsi
from src.testSTOCH import get_stoch
from src.testSpecial import formatDataset
from src.testSupertrend import get_supertrend
from test import limit, market


def __innit__(symbol):    
    
    rsiValue = 8

    totalPips = 0
    countPips = 0

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
    previousSignal = None

    lst = []
    current = {}

    n = 0
    length = difference = 0

    previousMinute = -1

    profilio = 10
    change = 0
    while True:
        if datetime.now().minute != previousMinute:
            if datetime.now().second > 0 and datetime.now().second < 2:
                


                print("\n" + datetime.now().strftime("%H:%M"))
                data = grabCurrentDataBTC(symbol)
                # print(data)
                data = data[len(data)-170:len(data)]
                data = formatDataset(data)
                ultimateData = data
                dataRSI = get_rsi(data["close"], rsiValue)
                data = get_stoch(ultimateData, 5, 3)
                data = data.dropna()
                st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
                st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
                st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
                st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
                st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
                st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 1) #change to 2
                st7, upt7, dt7 = get_supertrend(data["high"], data["low"], data["close"], 65, 1)

                previousMinute = datetime.now().minute
                i = -1
                # pos, nuet, neg, profilio, totalPips, countPips = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio, totalPips, countPips)
         
                previousSell = previousBuy = False
                previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)

                if previousBuy:
                    print(str(datetime.now()) + "BUY")
                    limit()
                    automaticBuy((1414, 946))
                    market()
                if previousSell:
                    print(str(datetime.now()) + "SELL")
                    limit()
                    automaticSell((1268, 938))
                    market()
                time.sleep(55)

if "__main__" == __name__:
    symbol = "BTCUSD"
    __innit__(symbol)