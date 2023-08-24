from tests.simulate import findPos
from tests.simulate2 import obtainResult
from tests.testADX import grabADX
from tests.testGrabData import grabHistoricalData
from tests.testRSI import get_rsi
from tests.testSTOCH import get_stoch
from tests.testSpecial import formatDataset
from tests.testSupertrend import get_supertrend
from datetime import datetime, timedelta
from sys import maxsize


def __innit__(symbol):    

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
    BestProfilio = -maxsize
    WorseProfilio = maxsize
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
    previousMinute = -1
    n = 0
    length = difference = 0
    profilio = 10
    while True:
        if datetime.now().minute != previousMinute:
            if datetime.now().second > 0 and datetime.now().second < 2:
                print("\n" + datetime.now().strftime("%H:%M"))
                data = grabHistoricalData(symbol)
                data = data[len(data)-200:len(data)]
                data = formatDataset(data)

                previousMinute = datetime.now().minute
                i = -1
                ultimateData = data
                rsiValue = 10
                dataRSI = get_rsi(data["close"], rsiValue)
                data = get_stoch(ultimateData, 5, 3)

                data = data.dropna()

                # Supertrend setup
                st, upt, dt = get_supertrend(data["high"], data["low"], data["close"], 164, 1)
                st2, upt2, dt2 = get_supertrend(data["high"], data["low"], data["close"], 93, 1)
                st3, upt3, dt3 = get_supertrend(data["high"], data["low"], data["close"], 1, 1)
                st4, upt4, dt4 = get_supertrend(data["high"], data["low"], data["close"], 77, 1)
                st5, upt5, dt5 = get_supertrend(data["high"], data["low"], data["close"], 39, 1)
                st6, upt6, dt6 = get_supertrend(data["high"], data["low"], data["close"], 42, 1) 
                st7, upt7, dt7 = get_supertrend(data["high"], data["low"], data["close"], 65, 1)




                pos, nuet, neg, profilio = findPos(data, i, n, previousBuy, previousSell, pos, nuet, neg, profilio)
                previousSell = previousBuy = False

                previousBuy, previousSell = obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue)
                # print("HALLLO")
                if previousBuy == True:
                    print("BUYYYY")
                elif previousSell == True:
                    print("SELL")


if "__main__" == __name__:
    # f = open("documents/dataSIM.txt", "r")
    # data = f.readlines()
    # data = eval(data[0])

    symbol = "EURJPY"
    __innit__(symbol)