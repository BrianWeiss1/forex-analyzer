
# Update data
from src.WMA import get_WMA
from srcLONGTERM.longTermPos import checkLuquidation, findPos, findSelection
from src.VWAP import get_VWAP
from src.specialFunctions import optimize2
from src.testADX import grabADX
from src.testRSI import get_rsi
from src.testSupertrend import superTrend
import sys
from datetime import timedelta
from src.testIchi import get_ichimoku
from src.testSpecial import formatDataset
from src.testEMA import calculate_200ema
from src.testMACD import get_macd
from srcLONGTERM.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex
from srcLONGTERM.underliningProcesses import STOCH, swap
import pandas as pd
def simulateCrypto(data):

    data = grabADX(data, 14)
    rsiValue = 147 #8, 147
    dataRSI = get_rsi(data["close"], rsiValue)
    totalPips = 0
    countPips = 0
    bestAvgPips = -sys.maxsize
    worstAvgPips = sys.maxsize
    data = data.dropna()

    j = -1
    k = -1
    previousBuyStochasticRSI = False
    previousSellStochasticRSI = False
    pos = 0
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
    previousBuyStochastic, previousSellStochastic = False, False
    lst = []

    n = 60
    st10 = superTrend(data, 2, 1) # 2, 87
    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    negPips = 0
    avgPips = 0
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


    # ema2 = calculate_200ema(data2, 200)
    rsiValue2 = 10
    # dataRSI2 = get_rsi(data2["close"], rsiValue2)
    WMA = get_WMA(data, 11)
    ichimoku = get_ichimoku(data, 7, 15) # 7, 15
    # get_StochasticOscilator(data, 14, 10, 3) # ---> returns dataframe
    # stochK = data['%K']
    # stochD = data['%D']
    nowPrice = 0
    nowCount = 0
    STOCHamount2 = 2
    STOCHamount1 = 3

    # get_StochasticOscilator(data, 293, 83, 140) 
    # stochK = data['%K']
    # stochD = data['%D']           
    # get_StochasticOscilator(data, 142, 10, 385)  # 957, 3, 3
    # stochK2 = data['%K']
    # stochD2 = data['%D']
    # get_StochasticOscilator(data, 301, 100, 101) 
    # stochK3 = data['%K']
    # stochD3 = data['%D']
    # get_StochasticOscilator(data, 89, 72, 390) 
    # stochK4 = data['%K']
    # stochD4 = data['%D']       
    # get_StochasticOscilator(data, 872, 2, 69) 
    # stochK5 = data['%K']
    # stochD5 = data['%D']     
    # get_StochasticOscilator(data, 196, 24, 314) 
    # stochK6 = data['%K']
    # stochD6 = data['%D']     
    # get_StochasticOscilator(data, 102, 33, 313) 
    # stochK7 = data['%K']
    # stochD7 = data['%D']  

    stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(data, 677, 70, 872)
    stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(data, 1334, 16, 15)
    stochRSIK3, stochRSID3 = get_StochasticRelitiveStrengthIndex(data, 660, 660, 153)
    stochRSIK4, stochRSID4 = get_StochasticRelitiveStrengthIndex(data, 535, 127, 137)
    stochRSIK5, stochRSID5 = get_StochasticRelitiveStrengthIndex(data, 24, 1956, 25)
    stochRSIK6, stochRSID6 = get_StochasticRelitiveStrengthIndex(data, 787, 1, 328)
    stochRSIK7, stochRSID7 = get_StochasticRelitiveStrengthIndex(data, 401, 127, 80)
    stochRSIK8, stochRSID8 = get_StochasticRelitiveStrengthIndex(data, 468, 9, 152)
    stochRSIK9, stochRSID9 = get_StochasticRelitiveStrengthIndex(data, 154, 120, 586)
    stochRSIK10, stochRSID10 = get_StochasticRelitiveStrengthIndex(data, 123, 123, 153)
    stochRSIK11, stochRSID11 = get_StochasticRelitiveStrengthIndex(data, 133, 120, 133)
    stochRSIK12, stochRSID12 = get_StochasticRelitiveStrengthIndex(data, 154, 120, 613)
    stochRSIK13, stochRSID13 = get_StochasticRelitiveStrengthIndex(data, 202, 52, 152)
    stochRSIK14, stochRSID14 = get_StochasticRelitiveStrengthIndex(data, 817, 50, 15)
    stochRSIK15, stochRSID15 = get_StochasticRelitiveStrengthIndex(data, 817, 200, 15)
    stochRSIK16, stochRSID16 = get_StochasticRelitiveStrengthIndex(data, 560, 5, 200)
    stochRSIK17, stochRSID17 = get_StochasticRelitiveStrengthIndex(data, 468, 9, 324)
    stochRSIK18, stochRSID18 = get_StochasticRelitiveStrengthIndex(data, 154, 263, 586)
    stochRSIK19, stochRSID19 = get_StochasticRelitiveStrengthIndex(data, 1293, 50, 15)
    stochRSIK20, stochRSID20 = get_StochasticRelitiveStrengthIndex(data, 468, 52, 152)
    stochRSIK21, stochRSID21 = get_StochasticRelitiveStrengthIndex(data, 417, 71, 200)
    stochRSIK22, stochRSID22 = get_StochasticRelitiveStrengthIndex(data, 281, 120, 281)
    stochRSIK23, stochRSID23 = get_StochasticRelitiveStrengthIndex(data, 401, 127, 137)
    stochRSIK24, stochRSID24 = get_StochasticRelitiveStrengthIndex(data, 293, 83, 316)
    stochRSIK25, stochRSID25 = get_StochasticRelitiveStrengthIndex(data, 401, 127, 153)

    get_StochasticOscilator(data, 196, 731, 314)
    stochK1 = data['%K']
    stochD1 = data['%D']
 
 
    try:
        for j in range(1, 2):

            print("K: " + str(j))


            for i in range(1, len(data) - 1):

                nowPrice += data['close'][i]
                nowCount += 1


                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True

                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                   
                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                #--------STOCH2RSI----------#

                #--------STOCH3RSI----------#
                longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                    previousSellStochasticRSI3 = True
                if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                    previousBuyStochasticRSI3 = True

                if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                    previousBuyStochasticRSI3 = False
                    previousSellStochasticRSI3 = False      
                #--------STOCH3RSI----------#

                #--------STOCH4RSI----------#
                longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                    previousSellStochasticRSI4 = True
                if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                    previousBuyStochasticRSI4 = True

                if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                    previousBuyStochasticRSI4 = False
                    previousSellStochasticRSI4 = False   

                #--------STOCH4RSI----------#


                #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                #--------STOCH5RSI----------#

                #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True

                previousBuyStochasticRSI6, previousSellStochasticRSI6 = swap(previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                #--------STOCH6RSI----------#

                #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True

                previousBuyStochasticRSI7, previousSellStochasticRSI7 = swap(previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                #--------STOCH7RSI----------#

                #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True

                previousBuyStochasticRSI8, previousSellStochasticRSI8 = swap(previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                #--------STOCH8RSI----------#

                # #--------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
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
                
                #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
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

                # #--------STOCH11RSI----------#
                longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                    previousSellStochasticRSI11 = True
                if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                    previousBuyStochasticRSI11 = True
                previousBuyStochasticRSI11, previousSellStochasticRSI11 = swap(previousBuyStochasticRSI11, previousSellStochasticRSI11)

                if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                    previousBuyStochasticRSI11 = False
                    previousSellStochasticRSI11 = False   
                # #--------STOCH11RSI----------#

                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
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

                #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                previousBuyStochasticRSI13, previousSellStochasticRSI13 = swap(previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                #--------STOCH13RSI----------#

                #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                previousBuyStochasticRSI14, previousSellStochasticRSI14 = swap(previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                #--------STOCH14RSI----------#

                #--------STOCH15RSI-------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                previousBuyStochasticRSI15, previousSellStochasticRSI15 = swap(previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                #--------STOCH15RSI----------#

                #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                previousBuyStochasticRSI16, previousSellStochasticRSI16 = swap(previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                #--------STOCH16RSI----------#

                #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                previousBuyStochasticRSI17, previousSellStochasticRSI17 = swap(previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                #--------STOCH17RSI----------#

                #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                previousBuyStochasticRSI18, previousSellStochasticRSI18 = swap(previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                #--------STOCH18RSI----------#

                #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                previousBuyStochasticRSI19, previousSellStochasticRSI19 = swap(previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                #--------STOCH19RSI----------#

                #--------STOCH20RSI----------#
                longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                    previousSellStochasticRSI20 = True
                if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                    previousBuyStochasticRSI20 = True
                previousBuyStochasticRSI20, previousSellStochasticRSI20 = swap(previousBuyStochasticRSI20, previousSellStochasticRSI20)

                if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                    previousBuyStochasticRSI20 = False
                    previousSellStochasticRSI20 = False   
                #--------STOCH20RSI----------#

                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                previousBuyStochasticRSI21, previousSellStochasticRSI21 = swap(previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                #--------STOCH21RSI----------#

                #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                previousBuyStochasticRSI22, previousSellStochasticRSI22 = swap(previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                #--------STOCH22RSI----------#

                #--------STOCH23RSI----------#
                longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                    previousSellStochasticRSI23 = True
                if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                    previousBuyStochasticRSI23 = True
                previousBuyStochasticRSI23, previousSellStochasticRSI23 = swap(previousBuyStochasticRSI23, previousSellStochasticRSI23)

                if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                    previousBuyStochasticRSI23 = False
                    previousSellStochasticRSI23 = False   
                #--------STOCH23RSI----------#

                #--------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                previousBuyStochasticRSI24, previousSellStochasticRSI24 = swap(previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                #--------STOCH24RSI----------#

                #--------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    
                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                previousBuyStochasticRSI25, previousSellStochasticRSI25 = swap(previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                #--------STOCH25RSI----------#

                #--------STOCH----------#
                # longRunSTOCH, shortRunSTOCH = findSelection(previousBuyStochastic, previousSellStochastic, longRunSTOCH, shortRunSTOCH, i) 
                # shortRunSTOCH, longRunSTOCH, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCH, longRunSTOCH, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                # previousBuyStochastic, previousSellStochastic = False, False

                # previousBuyStochastic, previousSellStochastic = STOCH(i, stochK, stochD, stochK2, stochD2, stochK3, stochD3, stochK4, stochD4, stochK5, stochD5, stochK6, stochD6, stochK7, stochD7)

                # -------- STOCH ------------#

            try:
                percentOfTrades = round(((pos + nuet + neg) / len(data)) * 100, 2)
                AvgPrice = nowPrice/nowCount
                print(pos, nuet, neg)
                try:
                    print("POS/NEG RATIO: " + str(pos / neg))
                    print(
                        "Percentage Correct: " + str(round((pos / (neg + pos)) * 100, 2)) + "%"
                    )
                except: 
                    print("ERROR 404")
                print("CANDLES: " + str(len(data) - 2))
                print(
                    "PERCENT OF TRADES: "
                    + str(percentOfTrades)
                )
                print("protfilio: " + str(portfolio))
                avgPips = totalPips/countPips
                print("AVERAGE PIPS: " + str(totalPips/countPips))
                print("POSITIVE PIPS: " + str(posPips/(countPos)))
                try:
                    negPip = negPips/(neg)
                except:
                    negPip = 0
                print("NEGITIVE PIPS: " + str(negPip))
                print("AVERAGE %: " + str(round((avgPips/AvgPrice), 5)))
                print("POS %: " + str(round(posPips/(pos)/AvgPrice, 5)))
                print("NEG %: " + str(round(negPip/AvgPrice, 5)))
                leverage = 50
                print(f"{leverage}X LEVERAGE")
                print("AVERAGE %: " + str(round((avgPips/AvgPrice)*leverage, 5)))
                print("POS %: " + str(round((posPips/(pos)/AvgPrice)*leverage, 5)))
                print("NEG %: " + str(round((negPip/AvgPrice)*leverage, 5)))
                p = (pos / (neg + pos))
                q = 1-p
                t = (((posPips/(pos)/AvgPrice)*leverage)/100)+1
                s = ((negPip/AvgPrice)*leverage/100)+1
                # print(s)
                KellyCriterum = p/s - q/t
                print("Best Bet %: " + str(KellyCriterum))
                amountOfBets = pos + nuet + neg

                amount = 10 * pow((1 + 0.76*1.768), amountOfBets)
                print(amount)
            except ZeroDivisionError:
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
                bestAvgPips = avgPips
                bestAvgj = j
                bestAvgk = k
            if avgPips*percentOfTrades < worstAvgPips:
                worstAvgPips = avgPips
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
        return BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj
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
    f = open("documents/dataCryptoTest15min.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data)
    df = pd.read_csv('output.csv')
    df.rename(columns={'High': 'high', 'Low': 'low', "Open": 'open', 'Close':'close'}, inplace=True)
    df = df.set_index('Datetime')
    df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    print(df)    

    # print(data)
    
    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj = simulateCrypto(df)
    #720mi
    # 77mil
    # 200bil


    # if not lst:
    #     exit()
    
    # total = sum(lst)
    # average = total / len(lst)


    # sorted_arr = sorted(lst)
    # n = len(sorted_arr)
    
    # if n % 2 == 1:
    #     median = sorted_arr[n // 2]
    # else:
    #     middle_right = n // 2
    #     middle_left = middle_right - 1
    #     median = (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2
    print("\n\nSIMULATION RESULTS: ")
    print("BestAVGPips: " + str(bestAvgPips))
    print("K: " +str(bestAvgk))
    print("J: " + str(bestAvgj))
    print("\nWORSTAVGPips: " + str(worstAvgPips))
    print("K: " +str(worstAvgk))
    print("J: " + str(worstAvgj))



    # BestAVGPips*percentOfTrades
    print("\n\n\n\n")
    print("Best Portfolio: \n" + str(BestProfilio))
    print("J:" + str(Bestj))
    print("K: " + str(Bestk))
    print('\n\n')
    print("Worst Portfolio: \n" + str(WorseProfilio))
    print("J: " + str(worstj))
    print("K: " + str(worstk))

# posLev = 151.51361
# negLev = -34.83314
# SucessPos = 0.5992
# SucessNeg = 1-SucessPos
#((posLev/100)+1)*SucessPos + ((negLev/100)+1)*(SucessNeg)
