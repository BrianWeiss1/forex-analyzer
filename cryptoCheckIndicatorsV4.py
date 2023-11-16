from src.longTermPos import checkLuquidation, checkLuquidationV1, findSelection
import sys
import requests
from SpecialFunctions import formatDataset, formatDataset1, formatDataset3, formatDataset2
from src.underliningProcesses import swap
from src.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex, get_supertrend
from temp.testGrabData import calltimes30FIXED
from datetime import datetime, timedelta
import numpy as np
import random
import time
def simulateCrypto(df, aVal, bVal, cVal):
    printing = False
    printingSpecific = True
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    df = df.dropna()
    bestSpecialValue = -sys.maxsize
    worstSpecialValue = sys.maxsize
    j = -1
    k = -1
    pos = 0
    AvgPercent = 0
    nuet = 0
    countrUp = 0
    neg = 0
    BestProfilio = -sys.maxsize
    WorseProfilio = sys.maxsize
    Bestj = -1
    Bestk = -1
    worstk = -1
    worstj = -1
    bestAvgj = -1
    bestAvgk = -1
    worstAvgj = -1
    worstAvgk = -1
    BestSpecialValues = (0, 0)
    WorstSpecialValues = (0, 0)

    oldj = -1
    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    countr = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    repeatA = repeatB = repeatC = False


    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False
    lstSpecialNumsDECLINE = []
    lstSpecialNumsINCLINE = []
    
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


#STOCH RSI CHECK ALL INDICATORS: how? run this through each one, loop through them all

    SpecialValue = 0
    # print(df)
    # countAAA = 0
    try:
        for j in range(1, 2):
            if printingSpecific: 
                if j != oldj:
                    oldj = j
            stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, bVal, cVal)
                
                
        
            stochRSIK1 = stochRSIK1.values
            stochRSID1 = stochRSID1.values

            for i in range(len(df)):
                
                nowPrice += df['close'][i]
                nowCount += 1
                
                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidationV1(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
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

                avgPips = totalPips / countPips
                negPip = np.where(neg != 0, negPips / neg, 0)

                posPercent = round((posPips / pos / AvgPrice), 5)
                negPercent = round((negPip / AvgPrice), 5)
                AvgPercent = round((avgPips / AvgPrice), 5)

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
                
            if avgPips*percentOfTrades > bestAvgPips and avgPips > 52000:
                bestAvgPips = avgPips*percentOfTrades
                bestAvgj = j
                bestAvgk = k
            if avgPips*percentOfTrades < worstAvgPips:
                worstAvgPips = avgPips*percentOfTrades
                worstAvgj = j
                worstAvgk = k
            if portfolio > BestProfilio:
                BestProfilio = portfolio
                Bestj = j
                Bestk = k
            elif portfolio < WorseProfilio:
                WorseProfilio = portfolio
                worstj = j
                worstk = k
            portfolio = 10
            negPips = 0
            posPips = 0
            totalPips = 0
            countPips = 0
            countPos = 0
            countNeg = 0
        #SEPERATE WHEN TABBING
        
#        return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues
    except KeyboardInterrupt:
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues




if "__main__" == __name__:
    # import re

    # original_list = [
    #     "GBPUSD=X/GBP/USD",
    #     "AUDUSD=X/AUD/USD",
    #     "NZDUSD=X/NZD/USD",
    #     "EURJPY=X/EUR/JPY",
    #     "GBPJPY=X/GBP/JPY",
    #     "EURGBP=X/EUR/GBP",
    #     "EURCAD=X/EUR/CAD",
    #     "EURSEK=X/EUR/SEK",
    #     "EURCHF=X/EUR/CHF",
    #     "EURHUF=X/EUR/HUF",
    #     "EURJPY=X/EUR/JPY",
    #     "CNY=X/USD/CNY",
    #     "HKD=X/USD/HKD",
    #     "SGD=X/USD/SGD",
    #     "INR=X/USD/INR",
    #     "MXN=X/USD/MXN",
    #     "PHP=X/USD/PHP",
    #     "IDR=X/USD/IDR",
    #     "THB=X/USD/THB",
    #     "MYR=X/USD/MYR",
    #     "ZAR=X/USD/ZAR",
    #     "RUB=X/USD/RUB"
    # ]

    # pattern = r'(\w{3}/\w{3})'  # Define a regular expression pattern for XXX/YYY format
    dic = {}
    f = open('documents/binanceSymbols.txt', 'r')
    dataSymbol = f.readlines()
    dataSymbol = eval(dataSymbol[0])
    f.close()
#  [[-0.0036410471999999998, (552, 28, 872)], [-0.0037366807399999997, (781, 971, 10)], [-0.0022908795, (22, 316, 162)], [-0.007873680360000001, (664, 4, 265)], [-0.0068785982999999985, (189, 522, 947)], [-0.0019358036000000003, (824, 1124, 3)], [-0.0029315714400000004, (110, 322, 22)], [-0.00439623976, (160, 631, 613)], [-0.005215583999999999, (249, 4, 346)], [-0.00603495936, (549, 7, 327)], [-0.0024781679999999998, (10, 82, 107)], [-0.003242826399999999, (138, 587, 6)], [-0.00472372992, (114, 3, 413)], [-0.009469126400000001, (628, 960, 10)], [-0.0047135648, (217, 5, 774)], [-0.0050740614, (680, 959, 13)], [-0.0034603264, (365, 17, 652)], [-0.004908023759999999, (219, 19, 361)], [-0.004967219399999999, (459, 2, 251)], [-0.003455264340000001, (318, 1243, 449)], [-0.004013453839999999, (100, 1555, 790)], [-0.005844654, (264, 3, 159)], [-0.0023328914399999997, (6, 48, 288)], [-0.00520546932, (539, 10, 341)], [-0.005572400459999999, (370, 3, 218)], [-0.0059221833999999985, (301, 7, 325)], [-0.0052228288, (12, 942, 1080)], [-0.003340869839999999, (200, 823, 486)], [-0.0021226077600000003, (92, 1500, 1117)], [-0.0041306606200000005, (632, 28, 704)], [-0.006237546479999997, (318, 7, 153)], [-0.005519434680000002, (287, 6, 158)], [-0.003508073160000001, (275, 1169, 109)], [-0.005885165239999999, (552, 7, 332)], [-0.004507456000000001, (780, 7, 850)], [-0.005233001199999999, (397, 4, 1031)], [-0.00387193914, (615, 29, 710)], [-0.006027344399999999, (313, 6, 160)], [-0.005166881600000001, (348, 7, 186)], [-0.005667141999999999, (527, 7, 482)], [-0.004050597599999999, (197, 267, 279)], [-0.0024576116399999998, (11, 137, 773)], [-0.004434063659999999, (887, 3, 741)], [-0.00583247952, (649, 10, 425)], [-0.005388838359999999, (625, 11, 400)], [-0.0047763198399999995, (162, 255, 387)], [-0.005267606400000001, (527, 10, 466)], [-0.00541825768, (214, 520, 803)], [-0.0028828072000000003, (11, 1383, 543)], [-0.005273950499999998, (611, 177, 477)]]
    for i in range(len(dataSymbol)):
        # symbol = "USD/MYR"
        try:
            df = formatDataset1(formatDataset(calltimes30FIXED(dataSymbol[i], (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d'))))
        except:
            time.sleep(3)
            continue
            

        lstOfSTOCH = [(78, 3, 46), (195, 89, 18), (290, 8, 209), (114, 3, 58), (105, 3, 46), (99, 3, 45), (290, 3, 214), (115, 3, 43), (92, 3, 45), (103, 2, 53), (258, 7, 212), (41, 3, 114), (52, 4, 262), (96, 3, 58), (53, 3, 257), (84, 4, 43), (139, 3, 51), (87, 2, 54), (53, 3, 269), (60, 2, 66), (41, 3, 105), (182, 11, 296), (66, 4, 69), (72, 4, 50), (223, 8, 266), (274, 5, 225), (245, 9, 194), (66, 3, 61), (226, 8, 249), (135, 2, 297), (58, 3, 97), (98, 3, 51), (55, 3, 102), (180, 11, 268), (204, 13, 231), (292, 14, 198), (245, 12, 188), (169, 2, 39), (101, 3, 36), (197, 3, 290), (133, 3, 29), (242, 11, 199), (70, 5, 43), (74, 3, 59), (197, 12, 234), (115, 3, 35), (194, 14, 246), (52, 3, 205), (43, 3, 90), (195, 12, 239), (274, 1, 274), (42, 3, 96), (180, 11, 277), (34, 4, 183), (66, 3, 28), (84, 3, 28), (148, 3, 36), (34, 4, 178), (274, 1, 266), (238, 3, 292), (179, 2, 29), (66, 3, 23), (168, 3, 26), (205, 3, 287), (141, 2, 29), (18, 6, 105), (114, 2, 48), (98, 3, 57), (50, 3, 266), (194, 4, 272), (50, 3, 253), (114, 5, 42), (151, 10, 181), (115, 3, 61), (194, 3, 299), (136, 2, 295), (50, 3, 259), (153, 3, 40), (146, 2, 41), (130, 3, 34), (131, 4, 42), (99, 2, 48), (98, 3, 70), (163, 2, 30), (140, 4, 49), (98, 3, 65), (114, 3, 53), (84, 3, 43), (98, 3, 42), (146, 3, 35), (194, 14, 240), (130, 4, 47), (146, 10, 191), (114, 3, 35), (148, 2, 178), (132, 3, 29), (163, 13, 8), (167, 2, 40), (148, 3, 28), (179, 11, 275), (114, 3, 66), (138, 2, 31), (168, 3, 28), (99, 4, 35), (130, 2, 24), (146, 3, 21), (66, 3, 24), (114, 3, 26), (154, 3, 28)]
        sumN = 0
        for j in range(len(lstOfSTOCH)):
            print(lstOfSTOCH[j])
            aVal = bVal = cVal = lstOfSTOCH[j][0], lstOfSTOCH[j][1], lstOfSTOCH[j][2] 
            aVal = aVal[0]
            bVal = bVal[1]
            cVal = cVal[2]
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, aVal, bVal, cVal)
            print(worstSpecialValue)
            if worstSpecialValue == 9223372036854775807:
                continue
            if dic.get(j) is not None:
                dic[j].append([dataSymbol[i], worstSpecialValue])
            else:
                dic[j] = [[dataSymbol[i], worstSpecialValue]]
            sumN+=worstSpecialValue
        print("\n\n\nBEST: " + str(round((sumN/len(lstOfSTOCH)), 5)))
        # print(symbol)
        print("\n\n\n")
        print(dic)
    print(i)
f = open("test2.txt", 'w')
f.write(str(dic))
f.close