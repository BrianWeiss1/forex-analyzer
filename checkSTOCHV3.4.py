from src.longTermPos import checkLuquidation, findSelection
import sys
import requests
from SpecialFunctions import formatDataset, formatDataset1, formatDataset3, formatDataset2
from src.underliningProcesses import swap
from src.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex, get_supertrend
from datetime import datetime, timedelta
import numpy as np
import random

api_key = "d6e8542914aa439e92fceaccca1c2708"
api_key2= "0d27bad2c7854a18bc4cafcb5d7f3583"
def grabForex(values):
    base_url = "https://api.twelvedata.com/time_series"
    '''
    GBPUSD=X/GBP/USD
    AUDUSD=X/AUD/USD
    NZDUSD=X/NZD/USD
    EURJPY=X/EUR/JPY
    GBPJPY=X/GBP/JPY
    EURGBP=X/EUR/GBP
    EURCAD=X/EUR/CAD
    EURSEK=X/EUR/SEK
    EURCHF=X/EUR/CHF
    EURHUF=X/EUR/HUF
    EURJPY=X/EUR/JPY
    CNY=X/USD/CNY
    HKD=X/USD/HKD
    SGD=X/USD/SGD
    INR=X/USD/INR
    MXN=X/USD/MXN
    PHP=X/USD/PHP
    IDR=X/USD/IDR
    THB=X/USD/THB
    MYR=X/USD/MYR
    ZAR=X/USD/ZAR
    RUB=X/USD/RUB
    '''
    params = {
        "symbol": "USD/NZD", #USD/NZD 0.003, NZD/USD 0.002
        "interval": "30min",
        "outputsize": values,
        "apikey": api_key2
        
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    ForexData = open('documents/forexData.txt', 'w')
    ForexData.write(str(data['values']))
    ForexData.close()
    return data['values']

def simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, incerment):
    printing = False
    printingSpecific = True
    # bestAvgPips = -sys.maxsize
    # worstAvgPips = sys.maxsize
    df = df.dropna()
    bestSpecialValue = -sys.maxsize
    worstSpecialValue = sys.maxsize
    j = -1
    k = -1
    pos = 0
    # AvgPercent = 0
    nuet = 0
    # countrUp = 0
    neg = 0
    # BestProfilio = -sys.maxsize
    # WorseProfilio = sys.maxsize
    # Bestj = -1
    # Bestk = -1
    # worstk = -1
    # worstj = -1
    # bestAvgj = -1
    # bestAvgk = -1
    # worstAvgj = -1
    # worstAvgk = -1
    BestSpecialValues = (0, 0)
    WorstSpecialValues = (0, 0)

    oldj = -1
    posPips = 0
    negPips = 0
    # avgPips = 0
    nowPrice = 0
    nowCount = 0
    # repeatA = repeatB = repeatC = False


    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False
    
#get_StochasticRelitiveStrengthIndex(df, 258, 19, 161) -0.0022 #1
#get_StochasticRelitiveStrengthIndex(df, 18, 217, 289) -0.00147#2
#get_StochasticRelitiveStrengthIndex(df, 276, 296, 18) -0.0027 #3
#get_StochasticRelitiveStrengthIndex(df, 53, 327, 132) -0.00212#4
#get_StochasticRelitiveStrengthIndex(df, 267, 291, 11) -0.00289#5
#get_StochasticRelitiveStrengthIndex(df, 125, 285, 151)-0.0022 #6
#get_StochasticRelitiveStrengthIndex(df, 149, j, 235)  -0.0014 #7
#get_StochasticRelitiveStrengthIndex(df, 306, 297, 13) -0.00294#8
#get_StochasticRelitiveStrengthIndex(df, 304, 18, 145) -0.00224#9
#get_StochasticRelitiveStrengthIndex(df, 451, 17, 212) -0.00353
#get_StochasticRelitiveStrengthIndex(df, 91, 304, 699) -0.0027
#get_StochasticRelitiveStrengthIndex(df, 106, 261, 417)-0.0021
#get_StochasticRelitiveStrengthIndex(df, 255, 298, 15) -0.00302
#get_StochasticRelitiveStrengthIndex(df, 236, 4, 219)  -0.0018
#get_StochasticRelitiveStrengthIndex(df, 321, 5, 584)  -0.00426
#get_StochasticRelitiveStrengthInde(df, 69, 1273, 1120)-0.00306
#get_StochasticRelitiveStrengthIndex(df, 1223, 4, 487) -0.00527
#get_StochasticRelitiveStrengthIndex(df, 1217, 138, 52)-0.00263
#get_StochasticRelitiveStrengthIndex(df, 495, 4, 496)  -0.0051
#get_StochasticRelitiveStrengthIndex(df, 419, j, 416)  -0.00344
#get_StochasticRelitiveStrengthIndex(df, 230, 20, 860) -0.003
#get_StochasticRelitiveStrengthIndex(df, 11, 318, 126))
#get_StochasticRelitiveStrengthIndex(df, 161, 3, 316)
#get_StochasticRelitiveStrengthIndex(df, 1056, 41, 6)
#get_StochasticRelitiveStrengthIndex(df, 521, 321, 73)
#get_StochasticRelitiveStrengthIndex(df, 10, 130, 148)
#get_StochasticRelitiveStrengthIndex(df, 12, 298, 78)
#get_StochasticRelitiveStrengthIndex(df, 640, 14, 374)
#get_StochasticRelitiveStrengthIndex(df, 255, 317, 85)
#get_StochasticRelitiveStrengthIndex(df, 315, 325, 90)
#get_StochasticRelitiveStrengthIndex(df, 345, 311, 45)
#get_StochasticRelitiveStrengthIndex(df, 686, 4, 984)
#get_StochasticRelitiveStrengthIndex(df, 16, 298, 252)
#get_StochasticRelitiveStrengthIndex(df, 366, 3, 1017)
#get_StochasticRelitiveStrengthIndex(df, 422, 120, 120)
#get_StochasticRelitiveStrengthIndex(df, 433, 120, 123)
#get_StochasticRelitiveStrengthIndex(df, 18, 1325, 157)
#get_StochasticRelitiveStrengthIndex(df, 874, 7, 805)
#get_StochasticRelitiveStrengthIndex(df, 7, 122, 140)
#get_StochasticRelitiveStrengthIndex(df, 9, 145, 361)
#get_StochasticRelitiveStrengthIndex(df, 321, 7, 150)
#get_StochasticRelitiveStrengthIndex(df, 335, 9, 173)
#get_StochasticRelitiveStrengthIndex(df, 315, 5, 151)
#get_StochasticRelitiveStrengthIndex(df, 304, 10, 356)
#get_StochasticRelitiveStrengthIndex(df, 643, 176, 18)
#get_StochasticRelitiveStrengthIndex(df, 32, 1302, 876)
#get_StochasticRelitiveStrengthIndex(df, 209, 24, 360)
#get_StochasticRelitiveStrengthIndex(df, 409, 3, 240)
#get_StochasticRelitiveStrengthIndex(df, 515, 9, 236)
#get_StochasticRelitiveStrengthIndex(df, 633, 29, 690)
#get_StochasticRelitiveStrengthIndex(df, 347, 310, 34)
#get_StochasticRelitiveStrengthIndex(df, 303, 295, 54)




#lstOfSTOCH = [[-0.0028316428799999996, (11, 318, 126)], [-0.00579613696, (161, 3, 316)], [-0.0026401339999999997, (1056, 41, 6)], [-0.0035683620000000007, (521, 321, 73)], [-0.0027887670199999996, (10, 130, 148)], [-0.0032564743199999997, (12, 298, 78)], [-0.005307652959999999, (640, 14, 374)], [-0.002934756, (255, 317, 85)], [-0.0034242753999999998, (315, 325, 90)], [-0.005224770479999999, (345, 311, 45)], [-0.00553080816, (686, 4, 984)], [-0.0034872774999999997, (16, 298, 252)], [-0.0046564574, (366, 3, 1017)], [-0.004528188, (326, 12, 717)], [-0.0023384592, (422, 120, 120)], [-0.00223377, (433, 120, 123)], [-0.0028171470600000005, (18, 1325, 157)], [-0.00454345632, (874, 7, 805)], [-0.0020107008000000005, (7, 122, 140)], [-0.0023027963999999995, (9, 145, 361)], [-0.006052687740000001, (321, 7, 150)], [-0.005577784740000002, (323, 8, 163)]]



    SpecialValue = 0
    # print(df)
    # countAAA = 0
    try:
        for j in range(2, amountTo, incerment):
            if printingSpecific: 
                if j != oldj:
                    oldj = j
            # print(a, b, c)
            if a:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, bVal, cVal) 
            elif b:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, j, cVal) 
            elif c:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, bVal, j) 
            else:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, 100, 680)
            stochRSIK1 = np.array(stochRSIK1)                
            stochRSID1 = np.array(stochRSID1)
            closeData = np.array(df['close'])
            for i in range(len(df)):
                
                nowPrice += closeData[i]
                nowCount += 1
                
                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, posPips, negPips = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, closeData, i, pos, nuet, neg, posPips, negPips)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] > stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] < stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True
                    
                # previousBuyStochasticRSI1, previousSellStochasticRSI1 = swap(previousBuyStochasticRSI1, previousSellStochasticRSI1)
                
                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                
            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice / nowCount

                negPip = np.where(neg != 0, negPips / neg, 0)

                posPercent = round((posPips / pos / AvgPrice), 5)
                negPercent = round((negPip / AvgPrice), 5)

                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness - 0.5
                tradeDecimal = percentOfTrades / 100
                
                
                # if printing:
                #     print("NEGITIVE PIPS: " + str(negPip))
                #     print("AVERAGE %: " + str(AvgPercent))
                #     print("POS %: " + str(posPercent))
                #     print("NEG %: " + str(negPercent))
                # leverage = 50
                # if printing:
                #     print(f"{leverage}X LEVERAGE")
                #     print("AVERAGE %: " + str(AvgPercent*leverage))
                #     print("POS %: " + str(posPercent*leverage))
                #     print("NEG %: " + str(negPercent*leverage))
                # if printing:
                #     print(SpecialValue)
                # p = (pos / (neg + pos))
                # q = 1-p
                # t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                # s = ((negPip/AvgPrice)*leverage/100)+1
                # KellyCriterum = p/s - q/t
                # if printing:
                #     print("Best Bet %: " + str(KellyCriterum))
                # if printing:
                #     try:
                #         print("POS/NEG RATIO: " + str(pos / neg))
                #         print(
                #             "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                #         )
                #     except: 
                #         print("ERROR 404")
                #     print("CANDLES: " + str(len(df) - 2))
                #     print(
                #         "PERCENT OF TRADES: "
                #         + str(percentOfTrades)
                #     )
                #     print("protfilio: " + str(portfolio))
                # if printing:
                #     print("AVERAGE PIPS: " + str(totalPips/countPips))
                #     print("POSITIVE PIPS: " + str(posPips/(countPos)))
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            pos = nuet = neg = 0
            try: 
                SpecialValue = difference * accuracy * tradeDecimal
                # print(SpecialValue)
                # if SpecialValue < 0:
                #     lstSpecialNumsDECLINE.append([(31, 290, 36),SpecialValue])
                #     lstSpecialNumsDECLINE = sorted(lstSpecialNumsDECLINE, key=lambda x: x[1])
                #     # print(lstSpecialNumsDECLINE)
                #     countr += 1
                #     if countr > 100:
                #         lstSpecialNumsDECLINE.pop()
                #         # print(len(lstSpecialNumsDECLINE))
                # if SpecialValue > 0:
                #     lstSpecialNumsINCLINE.append([(31, 290, 36),SpecialValue])
                #     lstSpecialNumsINCLINE = sorted(lstSpecialNumsINCLINE, key=lambda x: x[1], reverse=True)
                #     # print(lstSpecialNumsINCLINE)
                #     countrUp += 1
                #     if countrUp > 100:
                #         lstSpecialNumsINCLINE.pop()
                #         # print(len(lstSpecialNumsINCLINE))
                        
                if SpecialValue > bestSpecialValue:
                    bestSpecialValue = SpecialValue
                    BestSpecialValues = (j, k)
                if SpecialValue < worstSpecialValue:
                    worstSpecialValue = SpecialValue
                    WorstSpecialValues = (j, k)
            except:
                if printing:
                    print("ERROR")
                
            # if avgPips*percentOfTrades > bestAvgPips and avgPips > 52000:
            #     bestAvgPips = avgPips*percentOfTrades
            #     bestAvgj = j
            #     bestAvgk = k
            # if avgPips*percentOfTrades < worstAvgPips:
            #     worstAvgPips = avgPips*percentOfTrades
            #     worstAvgj = j
            #     worstAvgk = k
            # if portfolio > BestProfilio:
            #     BestProfilio = portfolio
            #     Bestj = j
            #     Bestk = k
            # elif portfolio < WorseProfilio:
            #     WorseProfilio = portfolio
            #     worstj = j
            #     worstk = k
            negPips = 0
            posPips = 0
        #SEPERATE WHEN TABBING
        
#        return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues
    except KeyboardInterrupt:
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues
def main():
    df = formatDataset2(formatDataset3(grabForex(5000)))
    # a = 0
    # b = 1
    # c = 1
    a = b = c = False
    aVal = bVal = cVal = 50
    # a = True
    i = 50
    stochValues = []
    lastBestVal = -1
    amountTo = 1400
    countRep = 0
    while(True):
        a = b = c = False
        abOrC = random.randint(0, 2)
        if abOrC == 0:
            a = True  
        if abOrC == 1:
            b = True
        if abOrC == 2:
            c = True 
        aVal = random.randint(1, 1000) 
        bVal = random.randint(1, 1000) 
        cVal = random.randint(1, 1000) 
        
        amountTo = 1400
        repeatA = False
        repeatB = False
        repeatC = False
        # 1.5x max
        onceA = onceB = onceC = False
        while True:
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 5)
            randomNum = random.randint(0, 1)
            # print("\n\nSIMULATION RESULTS: ")
            # print("\nBest Special Value: " + str(bestSpecialValue) + "  " + str(BestSpecialValues))
            # print("\nWorst Specl Value: " + str(worstSpecialValue) + "  " + str(WorstSpecialValues))
            if abs(bestSpecialValue) > abs(worstSpecialValue):
                # print("Best: " + str(BestSpecialValues))
                bestVal = BestSpecialValues[0]
                bestPer = bestSpecialValue
            else:
                # print("Worst: " + str(WorstSpecialValues))
                bestVal = WorstSpecialValues[0]
                bestPer = worstSpecialValue
            if a:
                onceA = True
                a = False
                if round(aVal, 5) == round(bestVal, 5):
                    repeatA = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                aVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatB):
                    b = True
                elif (randomNum == 0 or repeatB) and (not repeatC):
                    c = True
            elif b:
                onceB = True
                if round(bVal, 5) == round(bestVal, 5):
                    repeatB = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                b = False
                bVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatC):
                    c = True
            elif c:
                onceC = True
                if round(cVal, 5) == round(bestVal, 5):
                    repeatC = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                c = False
                cVal = bestVal
                if (randomNum == 1 or repeatB) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatB):
                    b = True
            else:
                print("ERROR: No value for a b c")
            
            if repeatA and repeatB and repeatC:
                break
                print(f"get_StochasticRelitiveStrengthIndex(df, {aVal}, {bVal}, {cVal})")
                stochValues.append([bestPer, (aVal, bVal, cVal)])
                break
            if onceC and onceB and onceA:
                amountTo = int(max(aVal, bVal, cVal)*2)
            lastBestVal = bestVal
        repeatA = repeatB = repeatC = False
        a = b = c = False
        abOrC = random.randint(0, 2)
        if abOrC == 0:
            a = True  
        if abOrC == 1:
            b = True
        if abOrC == 2:
            c = True 
        while True:
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 1)
            randomNum = random.randint(0, 1)
            # print("\n\nSIMULATION RESULTS: ")
            # print("\nBest Special Value: " + str(bestSpecialValue) + "  " + str(BestSpecialValues))
            # print("\nWorst Specl Value: " + str(worstSpecialValue) + "  " + str(WorstSpecialValues))
            if abs(bestSpecialValue) > abs(worstSpecialValue):
                # print("Best: " + str(BestSpecialValues))
                bestVal = BestSpecialValues[0]
                bestPer = bestSpecialValue
            else:
                # print("Worst: " + str(WorstSpecialValues))
                bestVal = WorstSpecialValues[0]
                bestPer = worstSpecialValue
            if a:
                onceA = True
                a = False
                if round(aVal, 5) == round(bestVal, 5):
                    repeatA = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                aVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatB):
                    b = True
                elif (randomNum == 0 or repeatB) and (not repeatC):
                    c = True
            elif b:
                onceB = True
                if round(bVal, 5) == round(bestVal, 5):
                    repeatB = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                b = False
                bVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatC):
                    c = True
            elif c:
                onceC = True
                if round(cVal, 5) == round(bestVal, 5):
                    repeatC = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                c = False
                cVal = bestVal
                if (randomNum == 1 or repeatB) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatB):
                    b = True
            else:
                print("ERROR: No value for a b c")
            
            if repeatA and repeatB and repeatC:
                print(f"get_StochasticRelitiveStrengthIndex(df, {aVal}, {bVal}, {cVal})")
                stochValues.append([bestPer, (aVal, bVal, cVal)])
                break
            if onceC and onceB and onceA:
                amountTo = int(max(aVal, bVal, cVal)*2)
            lastBestVal = bestVal\
                
        print(stochValues)




if "__main__" == __name__:
    main()
    