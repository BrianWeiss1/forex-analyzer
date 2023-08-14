from functions.specialFunctions import automaticBuy, automaticSell, obtainCurrentTime
from src.functions.STOCHredo import STOCH, checkPusdo, findCandleNumber, obtainResult
from datetime import datetime
import time
# 1 is at 80.06674757281553%
#EURUSD
def main(symbol):

    current = {}
    current[">percentD"] = 0
    current["<percentD"] = 0
    checkNextCandle = 0
    timer = -1
    bol = False
    while(True):
        if (datetime.now().second >= 1 and datetime.now().second <= 2 and not datetime.now().minute == timer):
            bol = True
        if bol == True:
            listOfKD = STOCH(symbol, 2, 1, 2)
            percentK = float(listOfKD[obtainCurrentTime()]['SlowK'])
            percentD = float(listOfKD[obtainCurrentTime()]['SlowD'])
            checkNextCandle = findCandleNumber(current) # check next candle 
            signal = obtainResult(checkNextCandle, current, percentK, percentD) # gives output of BUY or SELL
            checkPusdo(current, percentK, percentD) # change current
            if signal == "BUY":
                print("BUY")
                automaticBuy((1004, 481))
            elif signal == 'SELL':
                print("SELL")
                automaticSell((1009, 563))
            else:
                print("NONE")
            if (datetime.now().second >= 1 and datetime.now().second <= 2):
                timer = datetime.now().minute
            bol = False
            print(datetime.now())
            time.sleep(50)

if __name__ == "__main__":
    main("GBPAUD")
