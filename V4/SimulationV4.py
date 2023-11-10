# Update data
from temp.longTermPos import checkLuquidation, findPos, findSelection
import sys
from datetime import timedelta, datetime
from temp.SpecialFunctions import formatDataset, formatDataset1
from temp.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex
from temp.underliningProcesses import swap
import pandas as pd
from temp.testGrabData import getYahoo, calltimes15m, calltimes30FIXED
import numpy as np


def simulateCrypto(df, days=None, printing=True, endday = 0):
    
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

    lst = []

    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCH = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortRunSTOCH = {'shortSignal': False, 'luquidate': False, 'entry': []}



    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

    longRunSTOCHRSI2 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI2 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI2, previousSellStochasticRSI2 = False, False

    longRunSTOCHRSI3 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI3 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI3, previousSellStochasticRSI3 = False, False

    longRunSTOCHRSI4 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI4 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI4, previousSellStochasticRSI4 = False, False


    longRunSTOCHRSI5 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI5 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI5, previousSellStochasticRSI5 = False, False

    longRunSTOCHRSI6 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI6 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI6, previousSellStochasticRSI6 = False, False

    longRunSTOCHRSI7 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI7 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI7, previousSellStochasticRSI7 = False, False

    longRunSTOCHRSI8 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI8 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI8, previousSellStochasticRSI8 = False, False

    longRunSTOCHRSI9 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI9 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI9, previousSellStochasticRSI9 = False, False

    longRunSTOCHRSI10 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI10 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI10, previousSellStochasticRSI10 = False, False

    longRunSTOCHRSI11 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI11 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI11, previousSellStochasticRSI11 = False, False

    longRunSTOCHRSI12 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI12 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI12, previousSellStochasticRSI12 = False, False

    longRunSTOCHRSI13 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI13 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI13, previousSellStochasticRSI13 = False, False
    
    longRunSTOCHRSI14 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI14 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI14, previousSellStochasticRSI14 = False, False

    longRunSTOCHRSI15 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI15 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI15, previousSellStochasticRSI15 = False, False

    longRunSTOCHRSI16 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI16 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI16, previousSellStochasticRSI16 = False, False

    longRunSTOCHRSI17 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI17 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI17, previousSellStochasticRSI17 = False, False

    longRunSTOCHRSI18 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI18 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI18, previousSellStochasticRSI18 = False, False

    longRunSTOCHRSI19 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI19 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI19, previousSellStochasticRSI19 = False, False

    longRunSTOCHRSI20 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI20 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI20, previousSellStochasticRSI20 = False, False

    longRunSTOCHRSI21 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI21 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI21, previousSellStochasticRSI21 = False, False

    longRunSTOCHRSI22 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI22 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI22, previousSellStochasticRSI22 = False, False

    longRunSTOCHRSI23 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI23 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI23, previousSellStochasticRSI23 = False, False

    longRunSTOCHRSI24 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI24 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI24, previousSellStochasticRSI24 = False, False

    longRunSTOCHRSI25 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI25 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI25, previousSellStochasticRSI25 = False, False

    longRunSTOCHRSI26 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI26 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI26, previousSellStochasticRSI26 = False, False

    # get_StochasticOscilator(df, 34, 34, 34) # -21% 
    # stochRSIK1 = df['%K']
    # stochRSID1 = df['%D']
    get_StochasticOscilator(df, 460, 351, 4) # 23%
    stochRSIK2 = df['%K']
    stochRSID2 = df['%D']
    # get_StochasticOscilator(df, 30, 387, 35) # -21%
    # stochRSIK3 = df['%K']
    # stochRSID3 = df['%D']
    # get_StochasticOscilator(df, 79, 34, 17) # -26%
    # stochRSIK4 = df['%K']
    # stochRSID4 = df['%D']
    get_StochasticOscilator(df, 46, 344, 25) # 26%
    stochRSIK5 = df['%K']
    stochRSID5 = df['%D']
    get_StochasticOscilator(df, 158, 439, 8) # 23%
    stochRSIK6 = df['%K']
    stochRSID6 = df['%D']
    get_StochasticOscilator(df, 232, 446, 5) # 22%
    stochRSIK7 = df['%K']
    stochRSID7 = df['%D']
    get_StochasticOscilator(df, 42, 345, 25) # 23%
    stochRSIK8 = df['%K']
    stochRSID8 = df['%D']
    get_StochasticOscilator(df, 271, 441, 4) # 24%
    stochRSIK9 = df['%K']
    stochRSID9 = df['%D']
    get_StochasticOscilator(df, 327, 441, 3) # 24%
    stochRSIK10 = df['%K']
    stochRSID10 = df['%D']
    # get_StochasticOscilator(df, 66, 396, 10) # -21%
    # stochRSIK11 = df['%K']
    # stochRSID11 = df['%D']
    get_StochasticOscilator(df, 136, 441, 10) # 23%
    stochRSIK12 = df['%K']
    stochRSID12 = df['%D']
    get_StochasticOscilator(df, 6, 73, 1251) # 22%
    stochRSIK13 = df['%K']
    stochRSID13 = df['%D']
    get_StochasticOscilator(df, 327, 327, 4) # 21%
    stochRSIK14 = df['%K']
    stochRSID14 = df['%D']
    get_StochasticOscilator(df, 442, 442, 3) # 24%
    stochRSIK15 = df['%K']
    stochRSID15 = df['%D']
    get_StochasticOscilator(df, 209, 437, 5) # 24%
    stochRSIK16 = df['%K']
    stochRSID16 = df['%D']
    get_StochasticOscilator(df, 207, 439, 5) # 27%
    stochRSIK17 = df['%K']
    stochRSID17 = df['%D']
    get_StochasticOscilator(df, 207, 439, 6) # 28%
    stochRSIK18 = df['%K']
    stochRSID18 = df['%D']
    get_StochasticOscilator(df, 430, 442, 3) # 24.5%
    stochRSIK19 = df['%K']
    stochRSID19 = df['%D']
    # get_StochasticOscilator(df, 36, 388, 24) # 21%
    # stochRSIK20 = df['%K']
    # stochRSID20 = df['%D']
    get_StochasticOscilator(df, 39, 346, 31) # 25%
    stochRSIK21 = df['%K']
    stochRSID21 = df['%D']
    get_StochasticOscilator(df, 439, 205, 4) # 23%
    stochRSIK22 = df['%K']
    stochRSID22 = df['%D']
    # get_StochasticOscilator(df, 31, 387, 36) # 20%
    # stochRSIK23 = df['%K']
    # stochRSID23 = df['%D']
    get_StochasticOscilator(df, 31, 290, 37) # 19%
    stochRSIK24 = df['%K']
    stochRSID24 = df['%D']
    get_StochasticOscilator(df, 328, 441, 3) # 23%
    stochRSIK25 = df['%K']
    stochRSID25 = df['%D'] 
    # df = df[len(df)-(days*48):len(df)]

    SpecialValue = 0
    if days == None:
        days = len(df)/48
        
    days = days + endday
    # print(df)
    # countAAA = 0
    try:
        for j in range(1, 2):
            if printing:
                print("K: " + str(j))

            for i in range(len(df)-(days*48), (len(df) - 1)-(endday*48)):
                # countAAA += 1
                # print(countAAA)

                nowPrice += df['close'][i]
                nowCount += 1


                #--------STOCH1RSI----------#
                # longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                # shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                # if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                #     previousSellStochasticRSI1 = True
                # if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                #     previousBuyStochasticRSI1 = True
                    
                # previousBuyStochasticRSI1, previousSellStochasticRSI1 = swap(previousBuyStochasticRSI1, previousSellStochasticRSI1)
                
                # if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                #     previousBuyStochasticRSI1 = False
                #     previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                   
                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True
                    
                previousBuyStochasticRSI2, previousSellStochasticRSI2 = swap(previousBuyStochasticRSI2, previousSellStochasticRSI2)

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                # #--------STOCH2RSI----------#

                # #--------STOCH3RSI----------#
                # longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                # shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                # if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                #     previousSellStochasticRSI3 = True
                # if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                #     previousBuyStochasticRSI3 = True

                # # previousBuyStochasticRSI3, previousSellStochasticRSI3 = swap(previousBuyStochasticRSI3, previousSellStochasticRSI3)

                # if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                #     previousBuyStochasticRSI3 = False
                #     previousSellStochasticRSI3 = False      
                # #--------STOCH3RSI----------#

                # #--------STOCH4RSI----------#
                # longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                # shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                # if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                #     previousSellStochasticRSI4 = True
                # if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                #     previousBuyStochasticRSI4 = True
                # previousBuyStochasticRSI4, previousSellStochasticRSI4 = swap(previousBuyStochasticRSI4, previousSellStochasticRSI4)

                # if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                #     previousBuyStochasticRSI4 = False
                #     previousSellStochasticRSI4 = False   

                # #--------STOCH4RSI----------#


                # # #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True
                previousSellStochasticRSI5, previousBuyStochasticRSI5 = swap(previousBuyStochasticRSI5, previousSellStochasticRSI5)

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                # # #--------STOCH5RSI----------#

                # # #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True

                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                # # #--------STOCH6RSI----------#

                # #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True

                previousBuyStochasticRSI7, previousSellStochasticRSI7 = swap(previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                # #--------STOCH7RSI----------#

                # # #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True

                previousBuyStochasticRSI8, previousSellStochasticRSI8 = swap(previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                # # #--------STOCH8RSI----------#

                # # --------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI9 = previousBuyStochasticRSI9 = False

                if stochRSIK9[i-1] >= stochRSID9[i-1] and stochRSIK9[i] < stochRSID9[i]:
                    previousSellStochasticRSI9 = True
                if stochRSIK9[i-1] <= stochRSID9[i-1] and stochRSIK9[i] > stochRSID9[i]:
                    previousBuyStochasticRSI9 = True

                previousBuyStochasticRSI9, previousSellStochasticRSI9 = swap(previousBuyStochasticRSI9, previousSellStochasticRSI9)

                if previousSellStochasticRSI9 and previousBuyStochasticRSI9:
                    previousBuyStochasticRSI9 = False
                    previousSellStochasticRSI9 = False   
                # #--------STOCH9RSI----------#
                
                # #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI10 = previousBuyStochasticRSI10 = False

                if stochRSIK10[i-1] >= stochRSID10[i-1] and stochRSIK10[i] < stochRSID10[i]:
                    previousSellStochasticRSI10 = True
                if stochRSIK10[i-1] <= stochRSID10[i-1] and stochRSIK10[i] > stochRSID10[i]:
                    previousBuyStochasticRSI10 = True
                previousBuyStochasticRSI10, previousSellStochasticRSI10 = swap(previousBuyStochasticRSI10, previousSellStochasticRSI10)

                if previousSellStochasticRSI10 and previousBuyStochasticRSI10:
                    previousBuyStochasticRSI10 = False
                    previousSellStochasticRSI10 = False   
                #--------STOCH10RSI----------#

                #--------STOCH11RSI----------#
                # longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                # shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                # if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                #     previousSellStochasticRSI11 = True
                # if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                #     previousBuyStochasticRSI11 = True
                # previousSellStochasticRSI11, previousBuyStochasticRSI11 = swap(previousBuyStochasticRSI11, previousSellStochasticRSI11)

                # if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                #     previousBuyStochasticRSI11 = False
                #     previousSellStochasticRSI11 = False   
                #--------STOCH11RSI----------#

                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI12 = previousBuyStochasticRSI12 = False

                if stochRSIK12[i-1] >= stochRSID12[i-1] and stochRSIK12[i] < stochRSID12[i]:
                    previousSellStochasticRSI12 = True
                if stochRSIK12[i-1] <= stochRSID12[i-1] and stochRSIK12[i] > stochRSID12[i]:
                    previousBuyStochasticRSI12 = True
                previousBuyStochasticRSI12, previousSellStochasticRSI12 = swap(previousBuyStochasticRSI12, previousSellStochasticRSI12)

                if previousSellStochasticRSI12 and previousBuyStochasticRSI12:
                    previousBuyStochasticRSI12 = False
                    previousSellStochasticRSI12 = False   
                #--------STOCH12RSI----------#

                # #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                # previousSellStochasticRSI13, previousBuyStochasticRSI13 = swap(previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                # #--------STOCH13RSI----------#

                # #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                previousBuyStochasticRSI14, previousSellStochasticRSI14 = swap(previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                # #--------STOCH14RSI----------#

                # #--------STOCH15RSI-------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                # previousSellStochasticRSI15, previousBuyStochasticRSI15 = swap(previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                # #--------STOCH15RSI----------#

                # #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                previousBuyStochasticRSI16, previousSellStochasticRSI16 = swap(previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                # #--------STOCH16RSI----------#

                # #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                # previousSellStochasticRSI17, previousBuyStochasticRSI17 = swap(previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                # #--------STOCH17RSI----------#

                # #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                # previousSellStochasticRSI18, previousBuyStochasticRSI18 = swap(previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                # #--------STOCH18RSI----------#

                # #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                # previousSellStochasticRSI19, previousBuyStochasticRSI19 = swap(previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                # #--------STOCH19RSI----------#

                #--------STOCH20RSI----------#
                # longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                # shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                # if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                #     previousSellStochasticRSI20 = True
                # if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                #     previousBuyStochasticRSI20 = True
                # # previousSellStochasticRSI20, previousBuyStochasticRSI20 = swap(previousBuyStochasticRSI20, previousSellStochasticRSI20)

                # if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                #     previousBuyStochasticRSI20 = False
                #     previousSellStochasticRSI20 = False   
                #--------STOCH20RSI----------#

                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                # previousSellStochasticRSI21, previousBuyStochasticRSI21 = swap(previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                #--------STOCH21RSI----------#

                # #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                # previousSellStochasticRSI22, previousBuyStochasticRSI22 = swap(previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                # #--------STOCH22RSI----------#

                #--------STOCH23RSI----------#
                # longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                # shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                # previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                # if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                #     previousSellStochasticRSI23 = True
                # if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                #     previousBuyStochasticRSI23 = True
                # # previousSellStochasticRSI23, previousBuyStochasticRSI23 = swap(previousBuyStochasticRSI23, previousSellStochasticRSI23)

                # if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                #     previousBuyStochasticRSI23 = False
                #     previousSellStochasticRSI23 = False   
                # --------STOCH23RSI----------#

                # --------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                # previousSellStochasticRSI24, previousBuyStochasticRSI24 = swap(previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                # --------STOCH24RSI----------#

                # --------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                # previousSellStochasticRSI25, previousBuyStochasticRSI25 = swap(previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                # #--------STOCH25RSI----------#



            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice/nowCount
                if printing:
                    try:
                        print("POS/NEG RATIO: " + str(pos / neg))
                        print(
                            "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                        )
                    except: 
                        print("ERROR 404")
                    print("CANDLES: " + str(len(df) - 2))
                    print(
                        "PERCENT OF TRADES: "
                        + str(percentOfTrades)
                    )
                    print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                if printing:
                    print("AVERAGE PIPS: " + str(totalPips/countPips))
                    print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                posPercent = round((posPips/(pos)/AvgPrice), 5)
                negPercent = round((negPip/AvgPrice), 5)
                AvgPercent = round((avgPips/AvgPrice), 5)
                if printing:
                    print("NEGITIVE PIPS: " + str(negPip))
                    print("AVERAGE %: " + str(AvgPercent))
                    print("POS %: " + str(posPercent))
                    print("NEG %: " + str(negPercent))
                leverage = 50
                if printing:
                    print(f"{leverage}X LEVERAGE")
                    print("AVERAGE %: " + str(AvgPercent*leverage))
                    print("POS %: " + str(posPercent*leverage))
                    print("NEG %: " + str(negPercent*leverage))
                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness-0.5
                tradeDecimal = percentOfTrades/100
                if printing:
                    print(SpecialValue)
                p = (pos / (neg + pos))
                q = 1-p
                t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                s = ((negPip/AvgPrice)*leverage/100)+1
                # print(s)
                KellyCriterum = p/s - q/t
                if printing:
                    print("Best Bet %: " + str(KellyCriterum))
                # amountOfBets = pos + nuet + neg

                # amount = 10 * pow((1 + 0.76*1.768), amountOfBets)
                # print(amount)
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            # # ------Profilio-----

            lst.append(portfolio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            pos = nuet = neg = 0
            # if avgPips > 1000:
            #     avgPips -= 1000
            #     avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
            try: 
                SpecialValue = difference * accuracy * tradeDecimal   
                if SpecialValue > bestSpecialValue:
                    bestSpecialValue = SpecialValue
                    BestSpecialValues = (j, k)
                if SpecialValue < worstSpecialValue:
                    worstSpecialValue = SpecialValue
                    WorstSpecialValues = (j, k)
            except:
                a = j
                
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
        
        
        return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue
    except KeyboardInterrupt:
        print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj))
        print("K: " + str(worstk))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))














































def simulateSRSIOptimized(df, days=None, printing=True, endday = 0):
    
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    df = df.dropna()

    j = -1
    k = -1
    pos = 0
    AvgPercent = 0
    nuet = 0
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

    lst = []

    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCH = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortRunSTOCH = {'shortSignal': False, 'luquidate': False, 'entry': []}



    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

    longRunSTOCHRSI2 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI2 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI2, previousSellStochasticRSI2 = False, False

    longRunSTOCHRSI3 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI3 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI3, previousSellStochasticRSI3 = False, False

    longRunSTOCHRSI4 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI4 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI4, previousSellStochasticRSI4 = False, False


    longRunSTOCHRSI5 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI5 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI5, previousSellStochasticRSI5 = False, False

    longRunSTOCHRSI6 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI6 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI6, previousSellStochasticRSI6 = False, False

    longRunSTOCHRSI7 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI7 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI7, previousSellStochasticRSI7 = False, False

    longRunSTOCHRSI8 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI8 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI8, previousSellStochasticRSI8 = False, False

    longRunSTOCHRSI9 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI9 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI9, previousSellStochasticRSI9 = False, False

    longRunSTOCHRSI10 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI10 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI10, previousSellStochasticRSI10 = False, False

    longRunSTOCHRSI11 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI11 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI11, previousSellStochasticRSI11 = False, False

    longRunSTOCHRSI12 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI12 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI12, previousSellStochasticRSI12 = False, False

    longRunSTOCHRSI13 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI13 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI13, previousSellStochasticRSI13 = False, False
    
    longRunSTOCHRSI14 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI14 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI14, previousSellStochasticRSI14 = False, False

    longRunSTOCHRSI15 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI15 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI15, previousSellStochasticRSI15 = False, False

    longRunSTOCHRSI16 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI16 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI16, previousSellStochasticRSI16 = False, False

    longRunSTOCHRSI17 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI17 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI17, previousSellStochasticRSI17 = False, False

    longRunSTOCHRSI18 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI18 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI18, previousSellStochasticRSI18 = False, False

    longRunSTOCHRSI19 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI19 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI19, previousSellStochasticRSI19 = False, False

    longRunSTOCHRSI20 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI20 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI20, previousSellStochasticRSI20 = False, False

    longRunSTOCHRSI21 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI21 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI21, previousSellStochasticRSI21 = False, False

    longRunSTOCHRSI22 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI22 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI22, previousSellStochasticRSI22 = False, False

    longRunSTOCHRSI23 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI23 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI23, previousSellStochasticRSI23 = False, False

    longRunSTOCHRSI24 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI24 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI24, previousSellStochasticRSI24 = False, False

    longRunSTOCHRSI25 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI25 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI25, previousSellStochasticRSI25 = False, False

    longRunSTOCHRSI26 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI26 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI26, previousSellStochasticRSI26 = False, False

    stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, 2, 33, 25)
    stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 105)
    stochRSIK3, stochRSID3 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 114)
    stochRSIK4, stochRSID4 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 113)
    stochRSIK5, stochRSID5 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 112)
    stochRSIK6, stochRSID6 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 111)
    stochRSIK7, stochRSID7 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 110)
    stochRSIK8, stochRSID8 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 104)
    stochRSIK9, stochRSID9 = get_StochasticRelitiveStrengthIndex(df, 43, 3, 112)
    stochRSIK10, stochRSID10 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 115)
    stochRSIK11, stochRSID11 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 108)
    stochRSIK12, stochRSID12 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 106)
    stochRSIK13, stochRSID13 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 110)
    stochRSIK14, stochRSID14 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 113)
    stochRSIK15, stochRSID15 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 107)
    stochRSIK16, stochRSID16 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 114)
    stochRSIK17, stochRSID17 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 109)
    stochRSIK18, stochRSID18 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 112)
    stochRSIK19, stochRSID19 = get_StochasticRelitiveStrengthIndex(df, 42, 3, 109)
    stochRSIK20, stochRSID20 = get_StochasticRelitiveStrengthIndex(df, 40, 3, 115)
    stochRSIK21, stochRSID21 = get_StochasticRelitiveStrengthIndex(df, 40, 3, 113)
    stochRSIK22, stochRSID22 = get_StochasticRelitiveStrengthIndex(df, 39, 3, 106)
    stochRSIK23, stochRSID23 = get_StochasticRelitiveStrengthIndex(df, 40, 3, 109)
    stochRSIK24, stochRSID24 = get_StochasticRelitiveStrengthIndex(df, 42, 4, 92)
    stochRSIK25, stochRSID25 = get_StochasticRelitiveStrengthIndex(df, 41, 3, 101)
    stochRSIK26, stochRSID26 = get_StochasticRelitiveStrengthIndex(df, 40, 3, 112)
    SpecialValue = 0
    if days == None:
        days = len(df)/48
        
    days = days + endday
    # print(df)
    # countAAA = 0
    try:
        for j in range(1, 2):
            if printing:
                print("K: " + str(j))

            for i in range(len(df)-(days*48), (len(df) - 1)-(endday*48)):
                # countAAA += 1
                # print(countAAA)

                nowPrice += df['close'][i]
                nowCount += 1


                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True
                    
                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)
                
                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                   
                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True
                    
                previousBuyStochasticRSI2, previousSellStochasticRSI2 = swap(previousBuyStochasticRSI2, previousSellStochasticRSI2)

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                # #--------STOCH2RSI----------#

                # #--------STOCH3RSI----------#
                longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                    previousSellStochasticRSI3 = True
                if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                    previousBuyStochasticRSI3 = True

                # previousBuyStochasticRSI3, previousSellStochasticRSI3 = swap(previousBuyStochasticRSI3, previousSellStochasticRSI3)

                if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                    previousBuyStochasticRSI3 = False
                    previousSellStochasticRSI3 = False      
                # #--------STOCH3RSI----------#

                #--------STOCH4RSI----------#
                longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                    previousSellStochasticRSI4 = True
                if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                    previousBuyStochasticRSI4 = True
                previousBuyStochasticRSI4, previousSellStochasticRSI4 = swap(previousBuyStochasticRSI4, previousSellStochasticRSI4)

                if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                    previousBuyStochasticRSI4 = False
                    previousSellStochasticRSI4 = False   

                #--------STOCH4RSI----------#


                # # #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True
                previousSellStochasticRSI5, previousBuyStochasticRSI5 = swap(previousBuyStochasticRSI5, previousSellStochasticRSI5)

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                # # #--------STOCH5RSI----------#

                # # #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True

                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                # # #--------STOCH6RSI----------#

                # #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True

                previousBuyStochasticRSI7, previousSellStochasticRSI7 = swap(previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                # #--------STOCH7RSI----------#

                # # #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True

                previousBuyStochasticRSI8, previousSellStochasticRSI8 = swap(previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                # # #--------STOCH8RSI----------#

                # # --------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI9 = previousBuyStochasticRSI9 = False

                if stochRSIK9[i-1] >= stochRSID9[i-1] and stochRSIK9[i] < stochRSID9[i]:
                    previousSellStochasticRSI9 = True
                if stochRSIK9[i-1] <= stochRSID9[i-1] and stochRSIK9[i] > stochRSID9[i]:
                    previousBuyStochasticRSI9 = True

                previousBuyStochasticRSI9, previousSellStochasticRSI9 = swap(previousBuyStochasticRSI9, previousSellStochasticRSI9)

                if previousSellStochasticRSI9 and previousBuyStochasticRSI9:
                    previousBuyStochasticRSI9 = False
                    previousSellStochasticRSI9 = False   
                # #--------STOCH9RSI----------#
                
                # #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI10 = previousBuyStochasticRSI10 = False

                if stochRSIK10[i-1] >= stochRSID10[i-1] and stochRSIK10[i] < stochRSID10[i]:
                    previousSellStochasticRSI10 = True
                if stochRSIK10[i-1] <= stochRSID10[i-1] and stochRSIK10[i] > stochRSID10[i]:
                    previousBuyStochasticRSI10 = True
                previousBuyStochasticRSI10, previousSellStochasticRSI10 = swap(previousBuyStochasticRSI10, previousSellStochasticRSI10)

                if previousSellStochasticRSI10 and previousBuyStochasticRSI10:
                    previousBuyStochasticRSI10 = False
                    previousSellStochasticRSI10 = False   
                #--------STOCH10RSI----------#

                #--------STOCH11RSI----------#
                longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                    previousSellStochasticRSI11 = True
                if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                    previousBuyStochasticRSI11 = True
                previousSellStochasticRSI11, previousBuyStochasticRSI11 = swap(previousBuyStochasticRSI11, previousSellStochasticRSI11)

                if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                    previousBuyStochasticRSI11 = False
                    previousSellStochasticRSI11 = False   
                #--------STOCH11RSI----------#

                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI12 = previousBuyStochasticRSI12 = False

                if stochRSIK12[i-1] >= stochRSID12[i-1] and stochRSIK12[i] < stochRSID12[i]:
                    previousSellStochasticRSI12 = True
                if stochRSIK12[i-1] <= stochRSID12[i-1] and stochRSIK12[i] > stochRSID12[i]:
                    previousBuyStochasticRSI12 = True
                previousBuyStochasticRSI12, previousSellStochasticRSI12 = swap(previousBuyStochasticRSI12, previousSellStochasticRSI12)

                if previousSellStochasticRSI12 and previousBuyStochasticRSI12:
                    previousBuyStochasticRSI12 = False
                    previousSellStochasticRSI12 = False   
                #--------STOCH12RSI----------#

                # #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                # previousSellStochasticRSI13, previousBuyStochasticRSI13 = swap(previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                # #--------STOCH13RSI----------#

                # #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                previousBuyStochasticRSI14, previousSellStochasticRSI14 = swap(previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                # #--------STOCH14RSI----------#

                # #--------STOCH15RSI-------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                # previousSellStochasticRSI15, previousBuyStochasticRSI15 = swap(previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                # #--------STOCH15RSI----------#

                # #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                previousBuyStochasticRSI16, previousSellStochasticRSI16 = swap(previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                # #--------STOCH16RSI----------#

                # #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                # previousSellStochasticRSI17, previousBuyStochasticRSI17 = swap(previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                # #--------STOCH17RSI----------#

                # #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                # previousSellStochasticRSI18, previousBuyStochasticRSI18 = swap(previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                # #--------STOCH18RSI----------#

                # #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                # previousSellStochasticRSI19, previousBuyStochasticRSI19 = swap(previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                # #--------STOCH19RSI----------#

                #--------STOCH20RSI----------#
                longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                    previousSellStochasticRSI20 = True
                if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                    previousBuyStochasticRSI20 = True
                # previousSellStochasticRSI20, previousBuyStochasticRSI20 = swap(previousBuyStochasticRSI20, previousSellStochasticRSI20)

                if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                    previousBuyStochasticRSI20 = False
                    previousSellStochasticRSI20 = False   
                #--------STOCH20RSI----------#

                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                # previousSellStochasticRSI21, previousBuyStochasticRSI21 = swap(previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                #--------STOCH21RSI----------#

                # #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                # previousSellStochasticRSI22, previousBuyStochasticRSI22 = swap(previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                # #--------STOCH22RSI----------#

                #--------STOCH23RSI----------#
                longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                    previousSellStochasticRSI23 = True
                if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                    previousBuyStochasticRSI23 = True
                # previousSellStochasticRSI23, previousBuyStochasticRSI23 = swap(previousBuyStochasticRSI23, previousSellStochasticRSI23)

                if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                    previousBuyStochasticRSI23 = False
                    previousSellStochasticRSI23 = False   
                # --------STOCH23RSI----------#

                # --------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                # previousSellStochasticRSI24, previousBuyStochasticRSI24 = swap(previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                # --------STOCH24RSI----------#

                # --------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                # previousSellStochasticRSI25, previousBuyStochasticRSI25 = swap(previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                #--------STOCH25RSI----------#
                
                # --------STOCH26RSI----------#
                longRunSTOCHRSI26, shortRunSTOCHRSI26 = findSelection(previousBuyStochasticRSI26, previousSellStochasticRSI26, longRunSTOCHRSI26, shortRunSTOCHRSI26, i) 
                shortRunSTOCHRSI26, longRunSTOCHRSI26, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI26, longRunSTOCHRSI26, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI26 = previousBuyStochasticRSI26 = False

                if stochRSIK26[i-1] >= stochRSID26[i-1] and stochRSIK26[i] < stochRSID26[i]:
                    previousSellStochasticRSI26 = True
                if stochRSIK26[i-1] <= stochRSID26[i-1] and stochRSIK26[i] > stochRSID26[i]:
                    previousBuyStochasticRSI26 = True
                # previousSellStochasticRSI26, previousBuyStochasticRSI26 = swap(previousBuyStochasticRSI26, previousSellStochasticRSI26)

                if previousSellStochasticRSI26 and previousBuyStochasticRSI26:
                    previousBuyStochasticRSI26 = False
                    previousSellStochasticRSI26 = False   
                # #--------STOCH26RSI----------#



            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice/nowCount
                if printing:
                    try:
                        print("POS/NEG RATIO: " + str(pos / neg))
                        print(
                            "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                        )
                    except: 
                        print("ERROR 404")
                    print("CANDLES: " + str(len(df) - 2))
                    print(
                        "PERCENT OF TRADES: "
                        + str(percentOfTrades)
                    )
                    print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                if printing:
                    print("AVERAGE PIPS: " + str(totalPips/countPips))
                    print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                posPercent = round((posPips/(pos)/AvgPrice), 5)
                negPercent = round((negPip/AvgPrice), 5)
                AvgPercent = round((avgPips/AvgPrice), 5)
                if printing:
                    print("NEGITIVE PIPS: " + str(negPip))
                    print("AVERAGE %: " + str(AvgPercent))
                    print("POS %: " + str(posPercent))
                    print("NEG %: " + str(negPercent))
                leverage = 50
                if printing:
                    print(f"{leverage}X LEVERAGE")
                    print("AVERAGE %: " + str(AvgPercent*leverage))
                    print("POS %: " + str(posPercent*leverage))
                    print("NEG %: " + str(negPercent*leverage))
                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness-0.5
                tradeDecimal = percentOfTrades/100
                SpecialValue = difference * accuracy * tradeDecimal         
                if printing:
                    print(SpecialValue)
                p = (pos / (neg + pos))
                q = 1-p
                t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                s = ((negPip/AvgPrice)*leverage/100)+1
                # print(s)
                KellyCriterum = p/s - q/t
                if printing:
                    print("Best Bet %: " + str(KellyCriterum))
                # amountOfBets = pos + nuet + neg

                # amount = 10 * pow((1 + 0.76*1.768), amountOfBets)
                # print(amount)
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            # # ------Profilio-----

            lst.append(portfolio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            pos = nuet = neg = 0
            # if avgPips > 1000:
            #     avgPips -= 1000
            #     avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
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
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue
    except KeyboardInterrupt:
        print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj))
        print("K: " + str(worstk))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))






if "__main__" == __name__:
    simulation = 1
    if simulation == 1:
        betTest = True
        if betTest:
            symbolVolume = "CREAMUSDT"
            dic = {}
            printing = False
            count = 0
            totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d'))))
            for x in range(45):
                expFormula = 5*(pow(1.1, -x))
                dic[x] = expFormula
            # print(dic)
            for key, value in dic.items():
                # print(key)
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, key, False, 5)
                totalAmount += AvgPercent * value
                print(AvgPercent)
                count += value
            print("AVG PERCENT: " + str(totalAmount/count))
            for i in range(1, 6):
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, i, False, 0)
                print(AvgPercent)
        else:
            symbolVolume = "CREAMUSDT"
            # dic = {}
            printing = True
            # count = 0
            # totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=90)).strftime('%Y-%m-%d'))))
            print(df)
            # for x in range(45):
            #     expFormula = 5*(pow(1.1, -x))
            #     dic[x] = expFormula
            # # print(dic)
            # for key, value in dic.items():
            #     # print(key)
            #     BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, key, False, 1)
            #     totalAmount += AvgPercent * value
            #     print(AvgPercent)
            #     count += value
            # print("AVG PERCENT: " + str(totalAmount/count))
            # BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, False, 0)
            # print(AvgPercent)
                
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 2, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 3, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 5, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 10, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 14, True, 0)
            
            if printing:
                print("\n\nSIMULATION RESULTS: ")
                print("BestAVGPips: " + str(bestAvgPips))
                print("K: " +str(bestAvgk))
                print("J: " + str(bestAvgj))
                print("\nWORSTAVGPips: " + str(worstAvgPips))
                print("K: " +str(worstAvgk))
                print("J: " + str(worstAvgj))
                print("\n\n\n\n")

def simulateSRSI(df, days=None, printing=True, endday = 0):
    
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    df = df.dropna()

    j = -1
    k = -1
    pos = 0
    AvgPercent = 0
    nuet = 0
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

    lst = []

    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCH = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortRunSTOCH = {'shortSignal': False, 'luquidate': False, 'entry': []}



    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

    longRunSTOCHRSI2 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI2 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI2, previousSellStochasticRSI2 = False, False

    longRunSTOCHRSI3 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI3 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI3, previousSellStochasticRSI3 = False, False

    longRunSTOCHRSI4 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI4 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI4, previousSellStochasticRSI4 = False, False


    longRunSTOCHRSI5 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI5 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI5, previousSellStochasticRSI5 = False, False

    longRunSTOCHRSI6 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI6 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI6, previousSellStochasticRSI6 = False, False

    longRunSTOCHRSI7 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI7 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI7, previousSellStochasticRSI7 = False, False

    longRunSTOCHRSI8 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI8 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI8, previousSellStochasticRSI8 = False, False

    longRunSTOCHRSI9 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI9 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI9, previousSellStochasticRSI9 = False, False

    longRunSTOCHRSI10 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI10 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI10, previousSellStochasticRSI10 = False, False

    longRunSTOCHRSI11 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI11 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI11, previousSellStochasticRSI11 = False, False

    longRunSTOCHRSI12 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI12 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI12, previousSellStochasticRSI12 = False, False

    longRunSTOCHRSI13 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI13 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI13, previousSellStochasticRSI13 = False, False
    
    longRunSTOCHRSI14 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI14 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI14, previousSellStochasticRSI14 = False, False

    longRunSTOCHRSI15 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI15 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI15, previousSellStochasticRSI15 = False, False

    longRunSTOCHRSI16 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI16 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI16, previousSellStochasticRSI16 = False, False

    longRunSTOCHRSI17 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI17 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI17, previousSellStochasticRSI17 = False, False

    longRunSTOCHRSI18 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI18 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI18, previousSellStochasticRSI18 = False, False

    longRunSTOCHRSI19 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI19 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI19, previousSellStochasticRSI19 = False, False

    longRunSTOCHRSI20 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI20 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI20, previousSellStochasticRSI20 = False, False

    longRunSTOCHRSI21 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI21 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI21, previousSellStochasticRSI21 = False, False

    longRunSTOCHRSI22 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI22 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI22, previousSellStochasticRSI22 = False, False

    longRunSTOCHRSI23 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI23 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI23, previousSellStochasticRSI23 = False, False

    longRunSTOCHRSI24 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI24 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI24, previousSellStochasticRSI24 = False, False

    longRunSTOCHRSI25 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI25 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI25, previousSellStochasticRSI25 = False, False

    longRunSTOCHRSI26 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI26 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI26, previousSellStochasticRSI26 = False, False

    stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, 223, 418, 132)
    stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(df, 250, 418, 132)
    stochRSIK3, stochRSID3 = get_StochasticRelitiveStrengthIndex(df, 66, 70, 131)
    stochRSIK4, stochRSID4 = get_StochasticRelitiveStrengthIndex(df, 535, 127, 137) # --> 30000
    stochRSIK5, stochRSID5 = get_StochasticRelitiveStrengthIndex(df, 214, 47, 39)
    stochRSIK6, stochRSID6 = get_StochasticRelitiveStrengthIndex(df, 180, 33, 132)
    stochRSIK7, stochRSID7 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 80)
    stochRSIK8, stochRSID8 = get_StochasticRelitiveStrengthIndex(df, 69, 148, 59)
    stochRSIK9, stochRSID9 = get_StochasticRelitiveStrengthIndex(df, 154, 120, 586)
    stochRSIK10, stochRSID10 = get_StochasticRelitiveStrengthIndex(df, 96, 64, 110)
    stochRSIK11, stochRSID11 = get_StochasticRelitiveStrengthIndex(df, 145, 145, 39)
    stochRSIK12, stochRSID12 = get_StochasticRelitiveStrengthIndex(df, 153, 53, 56)
    stochRSIK13, stochRSID13 = get_StochasticRelitiveStrengthIndex(df, 77, 60, 136)
    stochRSIK14, stochRSID14 = get_StochasticRelitiveStrengthIndex(df, 51, 59, 156) 
    stochRSIK15, stochRSID15 = get_StochasticRelitiveStrengthIndex(df, 184, 62, 62) # 0%
    stochRSIK16, stochRSID16 = get_StochasticRelitiveStrengthIndex(df, 143, 143, 62)
    stochRSIK17, stochRSID17 = get_StochasticRelitiveStrengthIndex(df, 143, 424, 424) # 1%
    stochRSIK18, stochRSID18 = get_StochasticRelitiveStrengthIndex(df, 143, 49, 210) 
    stochRSIK19, stochRSID19 = get_StochasticRelitiveStrengthIndex(df, 53, 52, 194)
    stochRSIK20, stochRSID20 = get_StochasticRelitiveStrengthIndex(df, 53, 53, 199) # 0.8
    stochRSIK21, stochRSID21 = get_StochasticRelitiveStrengthIndex(df, 171, 57, 150) # 0.7
    stochRSIK22, stochRSID22 = get_StochasticRelitiveStrengthIndex(df, 65, 150, 65)
    stochRSIK23, stochRSID23 = get_StochasticRelitiveStrengthIndex(df, 134, 47, 238) # 1.09
    stochRSIK24, stochRSID24 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 137)
    stochRSIK25, stochRSID25 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 153)
    stochRSIK26, stochRSID26 = get_StochasticRelitiveStrengthIndex(df, 293, 83, 316)
                
    SpecialValue = 0
    if days == None:
        days = len(df)/48
        
    days = days + endday
    # print(df)
    # countAAA = 0
    try:
        for j in range(1, 2):
            if printing:
                print("K: " + str(j))

            for i in range(len(df)-(days*48), (len(df) - 1)-(endday*48)):
                # countAAA += 1
                # print(countAAA)

                nowPrice += df['close'][i]
                nowCount += 1


                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True
                    
                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)
                
                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                   
                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True
                    
                previousBuyStochasticRSI2, previousSellStochasticRSI2 = swap(previousBuyStochasticRSI2, previousSellStochasticRSI2)

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                # #--------STOCH2RSI----------#

                # #--------STOCH3RSI----------#
                longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                    previousSellStochasticRSI3 = True
                if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                    previousBuyStochasticRSI3 = True

                # previousBuyStochasticRSI3, previousSellStochasticRSI3 = swap(previousBuyStochasticRSI3, previousSellStochasticRSI3)

                if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                    previousBuyStochasticRSI3 = False
                    previousSellStochasticRSI3 = False      
                # #--------STOCH3RSI----------#

                #--------STOCH4RSI----------#
                longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                    previousSellStochasticRSI4 = True
                if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                    previousBuyStochasticRSI4 = True
                previousBuyStochasticRSI4, previousSellStochasticRSI4 = swap(previousBuyStochasticRSI4, previousSellStochasticRSI4)

                if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                    previousBuyStochasticRSI4 = False
                    previousSellStochasticRSI4 = False   

                #--------STOCH4RSI----------#


                # # #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True
                previousSellStochasticRSI5, previousBuyStochasticRSI5 = swap(previousBuyStochasticRSI5, previousSellStochasticRSI5)

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                # # #--------STOCH5RSI----------#

                # # #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True

                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                # # #--------STOCH6RSI----------#

                # #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True

                previousBuyStochasticRSI7, previousSellStochasticRSI7 = swap(previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                # #--------STOCH7RSI----------#

                # # #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True

                previousBuyStochasticRSI8, previousSellStochasticRSI8 = swap(previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                # # #--------STOCH8RSI----------#

                # # --------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI9 = previousBuyStochasticRSI9 = False

                if stochRSIK9[i-1] >= stochRSID9[i-1] and stochRSIK9[i] < stochRSID9[i]:
                    previousSellStochasticRSI9 = True
                if stochRSIK9[i-1] <= stochRSID9[i-1] and stochRSIK9[i] > stochRSID9[i]:
                    previousBuyStochasticRSI9 = True

                previousBuyStochasticRSI9, previousSellStochasticRSI9 = swap(previousBuyStochasticRSI9, previousSellStochasticRSI9)

                if previousSellStochasticRSI9 and previousBuyStochasticRSI9:
                    previousBuyStochasticRSI9 = False
                    previousSellStochasticRSI9 = False   
                # #--------STOCH9RSI----------#
                
                # #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI10 = previousBuyStochasticRSI10 = False

                if stochRSIK10[i-1] >= stochRSID10[i-1] and stochRSIK10[i] < stochRSID10[i]:
                    previousSellStochasticRSI10 = True
                if stochRSIK10[i-1] <= stochRSID10[i-1] and stochRSIK10[i] > stochRSID10[i]:
                    previousBuyStochasticRSI10 = True
                previousBuyStochasticRSI10, previousSellStochasticRSI10 = swap(previousBuyStochasticRSI10, previousSellStochasticRSI10)

                if previousSellStochasticRSI10 and previousBuyStochasticRSI10:
                    previousBuyStochasticRSI10 = False
                    previousSellStochasticRSI10 = False   
                #--------STOCH10RSI----------#

                #--------STOCH11RSI----------#
                longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                    previousSellStochasticRSI11 = True
                if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                    previousBuyStochasticRSI11 = True
                previousSellStochasticRSI11, previousBuyStochasticRSI11 = swap(previousBuyStochasticRSI11, previousSellStochasticRSI11)

                if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                    previousBuyStochasticRSI11 = False
                    previousSellStochasticRSI11 = False   
                #--------STOCH11RSI----------#

                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI12 = previousBuyStochasticRSI12 = False

                if stochRSIK12[i-1] >= stochRSID12[i-1] and stochRSIK12[i] < stochRSID12[i]:
                    previousSellStochasticRSI12 = True
                if stochRSIK12[i-1] <= stochRSID12[i-1] and stochRSIK12[i] > stochRSID12[i]:
                    previousBuyStochasticRSI12 = True
                previousBuyStochasticRSI12, previousSellStochasticRSI12 = swap(previousBuyStochasticRSI12, previousSellStochasticRSI12)

                if previousSellStochasticRSI12 and previousBuyStochasticRSI12:
                    previousBuyStochasticRSI12 = False
                    previousSellStochasticRSI12 = False   
                #--------STOCH12RSI----------#

                # #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                # previousSellStochasticRSI13, previousBuyStochasticRSI13 = swap(previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                # #--------STOCH13RSI----------#

                # #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                previousBuyStochasticRSI14, previousSellStochasticRSI14 = swap(previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                # #--------STOCH14RSI----------#

                # #--------STOCH15RSI-------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                # previousSellStochasticRSI15, previousBuyStochasticRSI15 = swap(previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                # #--------STOCH15RSI----------#

                # #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                previousBuyStochasticRSI16, previousSellStochasticRSI16 = swap(previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                # #--------STOCH16RSI----------#

                # #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                # previousSellStochasticRSI17, previousBuyStochasticRSI17 = swap(previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                # #--------STOCH17RSI----------#

                # #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                # previousSellStochasticRSI18, previousBuyStochasticRSI18 = swap(previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                # #--------STOCH18RSI----------#

                # #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                # previousSellStochasticRSI19, previousBuyStochasticRSI19 = swap(previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                # #--------STOCH19RSI----------#

                #--------STOCH20RSI----------#
                longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                    previousSellStochasticRSI20 = True
                if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                    previousBuyStochasticRSI20 = True
                # previousSellStochasticRSI20, previousBuyStochasticRSI20 = swap(previousBuyStochasticRSI20, previousSellStochasticRSI20)

                if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                    previousBuyStochasticRSI20 = False
                    previousSellStochasticRSI20 = False   
                #--------STOCH20RSI----------#

                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                # previousSellStochasticRSI21, previousBuyStochasticRSI21 = swap(previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                #--------STOCH21RSI----------#

                # #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                # previousSellStochasticRSI22, previousBuyStochasticRSI22 = swap(previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                # #--------STOCH22RSI----------#

                #--------STOCH23RSI----------#
                longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                    previousSellStochasticRSI23 = True
                if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                    previousBuyStochasticRSI23 = True
                # previousSellStochasticRSI23, previousBuyStochasticRSI23 = swap(previousBuyStochasticRSI23, previousSellStochasticRSI23)

                if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                    previousBuyStochasticRSI23 = False
                    previousSellStochasticRSI23 = False   
                # --------STOCH23RSI----------#

                # --------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                # previousSellStochasticRSI24, previousBuyStochasticRSI24 = swap(previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                # --------STOCH24RSI----------#

                # --------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                # previousSellStochasticRSI25, previousBuyStochasticRSI25 = swap(previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                #--------STOCH25RSI----------#
                
                # --------STOCH26RSI----------#
                longRunSTOCHRSI26, shortRunSTOCHRSI26 = findSelection(previousBuyStochasticRSI26, previousSellStochasticRSI26, longRunSTOCHRSI26, shortRunSTOCHRSI26, i) 
                shortRunSTOCHRSI26, longRunSTOCHRSI26, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI26, longRunSTOCHRSI26, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI26 = previousBuyStochasticRSI26 = False

                if stochRSIK26[i-1] >= stochRSID26[i-1] and stochRSIK26[i] < stochRSID26[i]:
                    previousSellStochasticRSI26 = True
                if stochRSIK26[i-1] <= stochRSID26[i-1] and stochRSIK26[i] > stochRSID26[i]:
                    previousBuyStochasticRSI26 = True
                # previousSellStochasticRSI26, previousBuyStochasticRSI26 = swap(previousBuyStochasticRSI26, previousSellStochasticRSI26)

                if previousSellStochasticRSI26 and previousBuyStochasticRSI26:
                    previousBuyStochasticRSI26 = False
                    previousSellStochasticRSI26 = False   
                # #--------STOCH26RSI----------#



            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice/nowCount
                if printing:
                    try:
                        print("POS/NEG RATIO: " + str(pos / neg))
                        print(
                            "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                        )
                    except: 
                        print("ERROR 404")
                    print("CANDLES: " + str(len(df) - 2))
                    print(
                        "PERCENT OF TRADES: "
                        + str(percentOfTrades)
                    )
                    print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                if printing:
                    print("AVERAGE PIPS: " + str(totalPips/countPips))
                    print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                posPercent = round((posPips/(pos)/AvgPrice), 5)
                negPercent = round((negPip/AvgPrice), 5)
                AvgPercent = round((avgPips/AvgPrice), 5)
                if printing:
                    print("NEGITIVE PIPS: " + str(negPip))
                    print("AVERAGE %: " + str(AvgPercent))
                    print("POS %: " + str(posPercent))
                    print("NEG %: " + str(negPercent))
                leverage = 50
                if printing:
                    print(f"{leverage}X LEVERAGE")
                    print("AVERAGE %: " + str(AvgPercent*leverage))
                    print("POS %: " + str(posPercent*leverage))
                    print("NEG %: " + str(negPercent*leverage))
                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness-0.5
                tradeDecimal = percentOfTrades/100
                SpecialValue = difference * accuracy * tradeDecimal         
                if printing:
                    print(SpecialValue)
                p = (pos / (neg + pos))
                q = 1-p
                t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                s = ((negPip/AvgPrice)*leverage/100)+1
                # print(s)
                KellyCriterum = p/s - q/t
                if printing:
                    print("Best Bet %: " + str(KellyCriterum))
                # amountOfBets = pos + nuet + neg

                # amount = 10 * pow((1 + 0.76*1.768), amountOfBets)
                # print(amount)
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            # # ------Profilio-----

            lst.append(portfolio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            pos = nuet = neg = 0
            # if avgPips > 1000:
            #     avgPips -= 1000
            #     avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
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
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue
    except KeyboardInterrupt:
        print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj))
        print("K: " + str(worstk))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))






if "__main__" == __name__:
    simulation = 1
    if simulation == 1:
        betTest = True
        if betTest:
            symbolVolume = "CREAMUSDT"
            dic = {}
            printing = False
            count = 0
            totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d'))))
            for x in range(45):
                expFormula = 5*(pow(1.1, -x))
                dic[x] = expFormula
            # print(dic)
            for key, value in dic.items():
                # print(key)
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, key, False, 5)
                totalAmount += AvgPercent * value
                print(AvgPercent)
                count += value
            print("AVG PERCENT: " + str(totalAmount/count))
            for i in range(1, 6):
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, i, False, 0)
                print(AvgPercent)
        else:
            symbolVolume = "CREAMUSDT"
            # dic = {}
            printing = True
            # count = 0
            # totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=90)).strftime('%Y-%m-%d'))))
            print(df)
            # for x in range(45):
            #     expFormula = 5*(pow(1.1, -x))
            #     dic[x] = expFormula
            # # print(dic)
            # for key, value in dic.items():
            #     # print(key)
            #     BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, key, False, 1)
            #     totalAmount += AvgPercent * value
            #     print(AvgPercent)
            #     count += value
            # print("AVG PERCENT: " + str(totalAmount/count))
            # BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, False, 0)
            # print(AvgPercent)
                
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 2, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 3, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 5, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 10, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 14, True, 0)
            
            if printing:
                print("\n\nSIMULATION RESULTS: ")
                print("BestAVGPips: " + str(bestAvgPips))
                print("K: " +str(bestAvgk))
                print("J: " + str(bestAvgj))
                print("\nWORSTAVGPips: " + str(worstAvgPips))
                print("K: " +str(worstAvgk))
                print("J: " + str(worstAvgj))
                print("\n\n\n\n")



def simulateSRSIOptimizedV2(df, days=None, printing=True, endday = 0):
    
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    df = df.dropna()

    j = -1
    k = -1
    pos = 0
    AvgPercent = 0
    nuet = 0
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

    lst = []

    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCH = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortRunSTOCH = {'shortSignal': False, 'luquidate': False, 'entry': []}



    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

    longRunSTOCHRSI2 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI2 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI2, previousSellStochasticRSI2 = False, False

    longRunSTOCHRSI3 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI3 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI3, previousSellStochasticRSI3 = False, False

    longRunSTOCHRSI4 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI4 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI4, previousSellStochasticRSI4 = False, False


    longRunSTOCHRSI5 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI5 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI5, previousSellStochasticRSI5 = False, False

    longRunSTOCHRSI6 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI6 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI6, previousSellStochasticRSI6 = False, False

    longRunSTOCHRSI7 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI7 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI7, previousSellStochasticRSI7 = False, False

    longRunSTOCHRSI8 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI8 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI8, previousSellStochasticRSI8 = False, False

    longRunSTOCHRSI9 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI9 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI9, previousSellStochasticRSI9 = False, False

    longRunSTOCHRSI10 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI10 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI10, previousSellStochasticRSI10 = False, False

    longRunSTOCHRSI11 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI11 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI11, previousSellStochasticRSI11 = False, False

    longRunSTOCHRSI12 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI12 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI12, previousSellStochasticRSI12 = False, False

    longRunSTOCHRSI13 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI13 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI13, previousSellStochasticRSI13 = False, False
    
    longRunSTOCHRSI14 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI14 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI14, previousSellStochasticRSI14 = False, False

    longRunSTOCHRSI15 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI15 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI15, previousSellStochasticRSI15 = False, False

    longRunSTOCHRSI16 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI16 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI16, previousSellStochasticRSI16 = False, False

    longRunSTOCHRSI17 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI17 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI17, previousSellStochasticRSI17 = False, False

    longRunSTOCHRSI18 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI18 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI18, previousSellStochasticRSI18 = False, False

    longRunSTOCHRSI19 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI19 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI19, previousSellStochasticRSI19 = False, False

    longRunSTOCHRSI20 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI20 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI20, previousSellStochasticRSI20 = False, False

    longRunSTOCHRSI21 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI21 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI21, previousSellStochasticRSI21 = False, False

    longRunSTOCHRSI22 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI22 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI22, previousSellStochasticRSI22 = False, False

    longRunSTOCHRSI23 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI23 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI23, previousSellStochasticRSI23 = False, False

    longRunSTOCHRSI24 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI24 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI24, previousSellStochasticRSI24 = False, False

    longRunSTOCHRSI25 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI25 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI25, previousSellStochasticRSI25 = False, False

    longRunSTOCHRSI26 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI26 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousBuyStochasticRSI26, previousSellStochasticRSI26 = False, False
    stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, 366, 3, 1017)
    stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(df, 161, 3, 316)
    stochRSIK3, stochRSID3 = get_StochasticRelitiveStrengthIndex(df, 370, 3, 218)
    stochRSIK4, stochRSID4 = get_StochasticRelitiveStrengthIndex(df, 459, 2, 251)
    stochRSIK5, stochRSID5 = get_StochasticRelitiveStrengthIndex(df, 217, 5, 774)
    stochRSIK6, stochRSID6 = get_StochasticRelitiveStrengthIndex(df, 527, 7, 482)
    stochRSIK7, stochRSID7 = get_StochasticRelitiveStrengthIndex(df, 625, 11, 400)
    stochRSIK8, stochRSID8 = get_StochasticRelitiveStrengthIndex(df, 664, 4, 265)
    stochRSIK9, stochRSID9 = get_StochasticRelitiveStrengthIndex(df, 301, 7, 325)
    stochRSIK10, stochRSID10 = get_StochasticRelitiveStrengthIndex(df, 264, 3, 159)
    stochRSIK11, stochRSID11 = get_StochasticRelitiveStrengthIndex(df, 114, 3, 413)
    stochRSIK12, stochRSID12 = get_StochasticRelitiveStrengthIndex(df, 217, 3, 343)
    stochRSIK13, stochRSID13 = get_StochasticRelitiveStrengthIndex(df, 313, 6, 160)
    stochRSIK14, stochRSID14 = get_StochasticRelitiveStrengthIndex(df, 304, 7, 253)
    stochRSIK15, stochRSID15 = get_StochasticRelitiveStrengthIndex(df, 348, 7, 186)
    stochRSIK16, stochRSID16 = get_StochasticRelitiveStrengthIndex(df, 348, 4, 445)
    stochRSIK17, stochRSID17 = get_StochasticRelitiveStrengthIndex(df, 249, 4, 346)
    stochRSIK18, stochRSID18 = get_StochasticRelitiveStrengthIndex(df, 649, 10, 425)
    stochRSIK19, stochRSID19 = get_StochasticRelitiveStrengthIndex(df, 206, 4, 186)
    stochRSIK20, stochRSID20 = get_StochasticRelitiveStrengthIndex(df, 161, 3, 316)
    stochRSIK21, stochRSID21 = get_StochasticRelitiveStrengthIndex(df, 203, 7, 65)
    stochRSIK22, stochRSID22 = get_StochasticRelitiveStrengthIndex(df, 307, 5, 186)
    stochRSIK23, stochRSID23 = get_StochasticRelitiveStrengthIndex(df, 700, 4, 136)
    stochRSIK24, stochRSID24 = get_StochasticRelitiveStrengthIndex(df, 306, 3, 152)
    stochRSIK25, stochRSID25 = get_StochasticRelitiveStrengthIndex(df, 948, 2, 531)
    stochRSIK26, stochRSID26 = get_StochasticRelitiveStrengthIndex(df, 547, 8, 517)
    
    SpecialValue = 0
    if days == None:
        days = len(df)/48
        
    days = days + endday
    # print(df)
    # countAAA = 0
    try:
        for j in range(1, 2):
            if printing:
                print("K: " + str(j))

            for i in range(len(df)-(days*48), (len(df) - 1)-(endday*48)):
                # countAAA += 1
                # print(countAAA)

                nowPrice += df['close'][i]
                nowCount += 1


                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True
                    
                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)
                
                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                   
                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True
                    
                previousBuyStochasticRSI2, previousSellStochasticRSI2 = swap(previousBuyStochasticRSI2, previousSellStochasticRSI2)

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                # #--------STOCH2RSI----------#

                # #--------STOCH3RSI----------#
                longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                    previousSellStochasticRSI3 = True
                if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                    previousBuyStochasticRSI3 = True

                # previousBuyStochasticRSI3, previousSellStochasticRSI3 = swap(previousBuyStochasticRSI3, previousSellStochasticRSI3)

                if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                    previousBuyStochasticRSI3 = False
                    previousSellStochasticRSI3 = False      
                # #--------STOCH3RSI----------#

                #--------STOCH4RSI----------#
                longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                    previousSellStochasticRSI4 = True
                if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                    previousBuyStochasticRSI4 = True
                previousBuyStochasticRSI4, previousSellStochasticRSI4 = swap(previousBuyStochasticRSI4, previousSellStochasticRSI4)

                if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                    previousBuyStochasticRSI4 = False
                    previousSellStochasticRSI4 = False   

                #--------STOCH4RSI----------#


                # # #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True
                previousSellStochasticRSI5, previousBuyStochasticRSI5 = swap(previousBuyStochasticRSI5, previousSellStochasticRSI5)

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                # # #--------STOCH5RSI----------#

                # # #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True

                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                # # #--------STOCH6RSI----------#

                # #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True

                previousBuyStochasticRSI7, previousSellStochasticRSI7 = swap(previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                # #--------STOCH7RSI----------#

                # # #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True

                previousBuyStochasticRSI8, previousSellStochasticRSI8 = swap(previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                # # #--------STOCH8RSI----------#

                # # --------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI9 = previousBuyStochasticRSI9 = False

                if stochRSIK9[i-1] >= stochRSID9[i-1] and stochRSIK9[i] < stochRSID9[i]:
                    previousSellStochasticRSI9 = True
                if stochRSIK9[i-1] <= stochRSID9[i-1] and stochRSIK9[i] > stochRSID9[i]:
                    previousBuyStochasticRSI9 = True

                previousBuyStochasticRSI9, previousSellStochasticRSI9 = swap(previousBuyStochasticRSI9, previousSellStochasticRSI9)

                if previousSellStochasticRSI9 and previousBuyStochasticRSI9:
                    previousBuyStochasticRSI9 = False
                    previousSellStochasticRSI9 = False   
                # #--------STOCH9RSI----------#
                
                # #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI10 = previousBuyStochasticRSI10 = False

                if stochRSIK10[i-1] >= stochRSID10[i-1] and stochRSIK10[i] < stochRSID10[i]:
                    previousSellStochasticRSI10 = True
                if stochRSIK10[i-1] <= stochRSID10[i-1] and stochRSIK10[i] > stochRSID10[i]:
                    previousBuyStochasticRSI10 = True
                previousBuyStochasticRSI10, previousSellStochasticRSI10 = swap(previousBuyStochasticRSI10, previousSellStochasticRSI10)

                if previousSellStochasticRSI10 and previousBuyStochasticRSI10:
                    previousBuyStochasticRSI10 = False
                    previousSellStochasticRSI10 = False   
                #--------STOCH10RSI----------#

                #--------STOCH11RSI----------#
                longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                    previousSellStochasticRSI11 = True
                if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                    previousBuyStochasticRSI11 = True
                previousSellStochasticRSI11, previousBuyStochasticRSI11 = swap(previousBuyStochasticRSI11, previousSellStochasticRSI11)

                if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                    previousBuyStochasticRSI11 = False
                    previousSellStochasticRSI11 = False   
                #--------STOCH11RSI----------#

                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI12 = previousBuyStochasticRSI12 = False

                if stochRSIK12[i-1] >= stochRSID12[i-1] and stochRSIK12[i] < stochRSID12[i]:
                    previousSellStochasticRSI12 = True
                if stochRSIK12[i-1] <= stochRSID12[i-1] and stochRSIK12[i] > stochRSID12[i]:
                    previousBuyStochasticRSI12 = True
                previousBuyStochasticRSI12, previousSellStochasticRSI12 = swap(previousBuyStochasticRSI12, previousSellStochasticRSI12)

                if previousSellStochasticRSI12 and previousBuyStochasticRSI12:
                    previousBuyStochasticRSI12 = False
                    previousSellStochasticRSI12 = False   
                #--------STOCH12RSI----------#

                # #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                # previousSellStochasticRSI13, previousBuyStochasticRSI13 = swap(previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                # #--------STOCH13RSI----------#

                # #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                previousBuyStochasticRSI14, previousSellStochasticRSI14 = swap(previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                # #--------STOCH14RSI----------#

                # #--------STOCH15RSI-------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                # previousSellStochasticRSI15, previousBuyStochasticRSI15 = swap(previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                # #--------STOCH15RSI----------#

                # #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                previousBuyStochasticRSI16, previousSellStochasticRSI16 = swap(previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                # #--------STOCH16RSI----------#

                # #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                # previousSellStochasticRSI17, previousBuyStochasticRSI17 = swap(previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                # #--------STOCH17RSI----------#

                # #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                # previousSellStochasticRSI18, previousBuyStochasticRSI18 = swap(previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                # #--------STOCH18RSI----------#

                # #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                # previousSellStochasticRSI19, previousBuyStochasticRSI19 = swap(previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                # #--------STOCH19RSI----------#

                #--------STOCH20RSI----------#
                longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                    previousSellStochasticRSI20 = True
                if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                    previousBuyStochasticRSI20 = True
                # previousSellStochasticRSI20, previousBuyStochasticRSI20 = swap(previousBuyStochasticRSI20, previousSellStochasticRSI20)

                if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                    previousBuyStochasticRSI20 = False
                    previousSellStochasticRSI20 = False   
                #--------STOCH20RSI----------#

                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                # previousSellStochasticRSI21, previousBuyStochasticRSI21 = swap(previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                #--------STOCH21RSI----------#

                # #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                # previousSellStochasticRSI22, previousBuyStochasticRSI22 = swap(previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                # #--------STOCH22RSI----------#

                #--------STOCH23RSI----------#
                longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                    previousSellStochasticRSI23 = True
                if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                    previousBuyStochasticRSI23 = True
                # previousSellStochasticRSI23, previousBuyStochasticRSI23 = swap(previousBuyStochasticRSI23, previousSellStochasticRSI23)

                if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                    previousBuyStochasticRSI23 = False
                    previousSellStochasticRSI23 = False   
                # --------STOCH23RSI----------#

                # --------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                # previousSellStochasticRSI24, previousBuyStochasticRSI24 = swap(previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                # --------STOCH24RSI----------#

                # --------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                # previousSellStochasticRSI25, previousBuyStochasticRSI25 = swap(previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                #--------STOCH25RSI----------#
                
                # --------STOCH26RSI----------#
                longRunSTOCHRSI26, shortRunSTOCHRSI26 = findSelection(previousBuyStochasticRSI26, previousSellStochasticRSI26, longRunSTOCHRSI26, shortRunSTOCHRSI26, i) 
                shortRunSTOCHRSI26, longRunSTOCHRSI26, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI26, longRunSTOCHRSI26, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI26 = previousBuyStochasticRSI26 = False

                if stochRSIK26[i-1] >= stochRSID26[i-1] and stochRSIK26[i] < stochRSID26[i]:
                    previousSellStochasticRSI26 = True
                if stochRSIK26[i-1] <= stochRSID26[i-1] and stochRSIK26[i] > stochRSID26[i]:
                    previousBuyStochasticRSI26 = True
                # previousSellStochasticRSI26, previousBuyStochasticRSI26 = swap(previousBuyStochasticRSI26, previousSellStochasticRSI26)

                if previousSellStochasticRSI26 and previousBuyStochasticRSI26:
                    previousBuyStochasticRSI26 = False
                    previousSellStochasticRSI26 = False   
                # #--------STOCH26RSI----------#



            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice/nowCount
                if printing:
                    try:
                        print("POS/NEG RATIO: " + str(pos / neg))
                        print(
                            "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                        )
                    except: 
                        print("ERROR 404")
                    print("CANDLES: " + str(len(df) - 2))
                    print(
                        "PERCENT OF TRADES: "
                        + str(percentOfTrades)
                    )
                    print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                if printing:
                    print("AVERAGE PIPS: " + str(totalPips/countPips))
                    print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                posPercent = round((posPips/(pos)/AvgPrice), 5)
                negPercent = round((negPip/AvgPrice), 5)
                AvgPercent = round((avgPips/AvgPrice), 5)
                if printing:
                    print("NEGITIVE PIPS: " + str(negPip))
                    print("AVERAGE %: " + str(AvgPercent))
                    print("POS %: " + str(posPercent))
                    print("NEG %: " + str(negPercent))
                leverage = 50
                if printing:
                    print(f"{leverage}X LEVERAGE")
                    print("AVERAGE %: " + str(AvgPercent*leverage))
                    print("POS %: " + str(posPercent*leverage))
                    print("NEG %: " + str(negPercent*leverage))
                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness-0.5
                tradeDecimal = percentOfTrades/100
                SpecialValue = difference * accuracy * tradeDecimal         
                if printing:
                    print(SpecialValue)
                p = (pos / (neg + pos))
                q = 1-p
                t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                s = ((negPip/AvgPrice)*leverage/100)+1
                # print(s)
                KellyCriterum = p/s - q/t
                if printing:
                    print("Best Bet %: " + str(KellyCriterum))
                # amountOfBets = pos + nuet + neg

                # amount = 10 * pow((1 + 0.76*1.768), amountOfBets)
                # print(amount)
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            # # ------Profilio-----

            lst.append(portfolio)
            # print(pos / (neg + pos))
            # try:
            #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(data)) * 100, 2))*100
            # except ZeroDivisionError:
            #     ratio = 0
            pos = nuet = neg = 0
            # if avgPips > 1000:
            #     avgPips -= 1000
            #     avgPips = avgPips * percentOfTrades
                # print("Ratio: " + str(ratio))
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
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue
    except KeyboardInterrupt:
        print("\n\nBEST PROFILIO: " + str(BestProfilio) + " must be > 66mil")
        print("BEST K: " + str(k))
        print("BEST J: " + str(j))
        print("\n")
        print("\nBestAVGPips: " + str(bestAvgPips))
        print("K: " +str(bestAvgk))
        print("J: " + str(bestAvgj))
        print("\n\nWorst Portfolio: " + str(WorseProfilio))
        print("J: " + str(worstj))
        print("K: " + str(worstk))
        print("\nWORSTAVGPips: " + str(worstAvgPips))
        print("K: " +str(worstAvgk))
        print("J: " + str(worstAvgj))






if "__main__" == __name__:
    simulation = 1
    if simulation == 1:
        betTest = True
        if betTest:
            symbolVolume = "CREAMUSDT"
            dic = {}
            printing = False
            count = 0
            totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=100)).strftime('%Y-%m-%d'))))
            for x in range(45):
                expFormula = 5*(pow(1.1, -x))
                dic[x] = expFormula
            # print(dic)
            for key, value in dic.items():
                # print(key)
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, key, False, 5)
                totalAmount += AvgPercent * value
                print(AvgPercent)
                count += value
            print("AVG PERCENT: " + str(totalAmount/count))
            for i in range(1, 6):
                BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCryptoSTOCHRSI(df, i, False, 0)
                print(AvgPercent)
        else:
            symbolVolume = "CREAMUSDT"
            # dic = {}
            printing = True
            # count = 0
            # totalAmount = 0
            df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=90)).strftime('%Y-%m-%d'))))
            print(df)
            # for x in range(45):
            #     expFormula = 5*(pow(1.1, -x))
            #     dic[x] = expFormula
            # # print(dic)
            # for key, value in dic.items():
            #     # print(key)
            #     BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, key, False, 1)
            #     totalAmount += AvgPercent * value
            #     print(AvgPercent)
            #     count += value
            # print("AVG PERCENT: " + str(totalAmount/count))
            # BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, False, 0)
            # print(AvgPercent)
                
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 1, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 2, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 3, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 5, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 10, True, 0)
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, 14, True, 0)
            
            if printing:
                print("\n\nSIMULATION RESULTS: ")
                print("BestAVGPips: " + str(bestAvgPips))
                print("K: " +str(bestAvgk))
                print("J: " + str(bestAvgj))
                print("\nWORSTAVGPips: " + str(worstAvgPips))
                print("K: " +str(worstAvgk))
                print("J: " + str(worstAvgj))
                print("\n\n\n\n")
