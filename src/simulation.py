import datetime
import time
from functions.GrabData import GrabCloseData

from functions.StochasticOscillator import compareGetStoch
from functions.StochasticOscillator import get_list_solastic

def calculate_supreme_average(lstKandDValues, lstValues, time):
    arraylst = []
    previousBuy = False
    previousSell = False
    pos = 0
    neg = 0
    # print(lstValues[1])
    # print(time[1])
    # print(data)
    # print(lstKandDValues)
    # print(len(time))
    print(len(lstValues))
    # print(len(lstKandDValues))
    print(len(time))
    # KDvalue = list(lstKandDValues.values())
    for i in range(len(list(lstKandDValues.keys()))-1, 0, -1):
        if previousBuy:
            if not lstValues[i] > lstValues[i+1]: # need to change to prices
                pos += 1
                previousBuy = False
            else:
                neg += 1
                previousBuy = False
        elif previousSell:
            if not lstValues[i] < lstValues[i+1]: # need to change to prices
                pos += 1
                previousSell = False
            else:
                neg += 1
                previousSell = False
        result = compareGetStoch(float(lstKandDValues[time[i]]['SlowK']), float(lstKandDValues[time[i]]['SlowD']), 10) # I can run this with each different %

        if result['buy']:
            arraylst.append(['buy', datetime.datetime.now])
            previousBuy = True
        elif result['sell']:
            arraylst.append(['sell', datetime.datetime.now])
            previousSell = True
    return pos, neg
symbol = 'AUDCHF'
sucess = 0.6612529002320185 # 1 3 3
for i in range(22, 50):
    # time.sleep(20)
    closeData, time2 = GrabCloseData(symbol)
    temp = True
    while(temp == True):
        try:
            pos, neg = calculate_supreme_average(get_list_solastic(symbol, 1, 3, 3), closeData, time2)
            sucessRate = pos/(pos+neg)
            print("Trades = " + str(pos+neg))
            print("Sucess = " + str(sucessRate))
            if sucessRate > sucess:
                sucess = sucessRate
            temp = False
        except:
            print("error")
            time.sleep(60)
            # closeData, time2, data = GrabCloseData(symbol)
            temp = True

# print("Amount of candles: " + str(1383))
# print("Trades = " + str(pos+neg))
# print("Sucessful Trades: " + str(pos))
# print("Negitive Traades: " + str(neg))
# print("Sucess = " + str(pos/(pos+neg)))

# CURRENT TIME: 2023-08-10 17:07'
# This is in the list: 2023-08-10 17:07:00
# Times printed out

#17:21
#17:48
# 27
# 0.5706 = 2023-08-10 17:25



# 0.5724 = 