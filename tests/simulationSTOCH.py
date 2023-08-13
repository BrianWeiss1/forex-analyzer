import datetime
import time
from src.functions.GrabData import GrabCloseData

from src.functions.StochasticOscillator import compareGetStoch
from src.functions.StochasticOscillator import get_list_solastic

def calculate_supreme_average(lstKandDValues, lstValues, time, specialNum):
    arraylst = []
    previousBuy = False
    previousSell = False
    pos = 0
    neg = 0
    nuet = 0

    for i in range(len(list(lstKandDValues.keys()))-1, 0, -1):
        if previousBuy:
            if not lstValues[i] > lstValues[i+1]: # need to change to prices
                pos += 1
                previousBuy = False
            elif lstValues[i] == lstValues[i+1]:
                nuet += 1
                previousBuy = False
            else:
                neg += 1
                previousBuy = False
        elif previousSell:
            if not lstValues[i] < lstValues[i+1]: # need to change to prices
                pos += 1
                previousSell = False
            elif lstValues[i] == lstValues[i+1]:
                nuet += 1
                previousSell = False
            else:
                neg += 1
                previousSell = False
        result = compareGetStoch(float(lstKandDValues[time[i]]['SlowK']), float(lstKandDValues[time[i]]['SlowD']), 1, specialNum) # I can run this with each different %

        if result['buy']:
            arraylst.append(['buy', datetime.datetime.now])
            previousBuy = True
        elif result['sell']:
            arraylst.append(['sell', datetime.datetime.now])
            previousSell = True
    return pos, nuet, neg
symbol = 'AUDCHF'
sucess = 0.6739288307915758 # 1 3 3 (1) (0)
closeData, time2 = GrabCloseData(symbol)
temp = True
while(temp == True):
    try:
        pos, nuet, neg = calculate_supreme_average(get_list_solastic(symbol, 1, 3, 3), closeData, time2, 0)
        sucessRate = pos/(pos+neg)
        print("Candles: " + str(len(closeData)))
        print("Total Trades: " + str(pos+neg+nuet))
        print("Positive Trades: " + str(pos))
        print("Neutrol Trades: " + str(nuet))
        print("Negitive Trades: " + str(neg))
        if sucessRate > sucess:
            sucess = sucessRate
        temp = False
    except:
        print("error")
        time.sleep(20)
        temp = True
