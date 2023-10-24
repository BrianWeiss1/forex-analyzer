from src.longTermPos import checkLuquidation, findSelection
import sys
import requests
from SpecialFunctions import formatDataset, formatDataset1, formatDataset3, formatDataset2
from src.underliningProcesses import swap
from src.functions import get_StochasticOscilator, get_StochasticRelitiveStrengthIndex, get_supertrend
from datetime import datetime, timedelta

def grabForex(values):
    # Define your API key
    api_key = "d6e8542914aa439e92fceaccca1c2708"

    # Define the API endpoint URL
    base_url = "https://api.twelvedata.com/time_series"

    # Define the parameters for the request
    params = {
        "symbol": "EUR/USD",  # The forex symbol you want to retrieve
        "interval": "30min",   # Time interval (e.g., 1min, 1day)
        "outputsize": values,     # Number of data points to retrieve
        "apikey": api_key     # Your Twelve Data API key
        
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data['values']
    
def simulateCrypto(df):
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

    lst = []
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
    longRunSTOCH = {"buySignal": False, 'luquidate': False, 'entry': []}
    shortRunSTOCH = {'shortSignal': False, 'luquidate': False, 'entry': []}



    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False
    lstSpecialNumsDECLINE = []
    lstSpecialNumsINCLINE = []


    SpecialValue = 0
    # print(df)
    # countAAA = 0
    try:
        for j in range(2, 150):
            for k in range(1, 150):
                for c in range(1, 150):
                    if printingSpecific:
                        if k != oldj:
                            print("K: " + str(k))
                            oldj = k
                    stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, k, c)# 31, 290, 36
                    
                    for i in range(len(df)):
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
                            
                        previousBuyStochasticRSI1, previousSellStochasticRSI1 = swap(previousBuyStochasticRSI1, previousSellStochasticRSI1)
                        
                        if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                            previousBuyStochasticRSI1 = False
                            previousSellStochasticRSI1 = False   
                        #--------STOCH1RSI----------#  
                        


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
                    #     ratio = (100-round((pos / (neg + pos)) * 100, 2))/(100-round(((pos + nuet + neg) / len(df)) * 100, 2))*100
                    # except ZeroDivisionError:
                    #     ratio = 0
                    pos = nuet = neg = 0
                    # if avgPips > 1000:
                    #     avgPips -= 1000
                    #     avgPips = avgPips * percentOfTrades
                        # print("Ratio: " + str(ratio))
                    try: 
                        SpecialValue = difference * accuracy * tradeDecimal
                        if SpecialValue < 0:
                            lstSpecialNumsDECLINE.append([(j, k, c),SpecialValue])
                            lstSpecialNumsDECLINE = sorted(lstSpecialNumsDECLINE, key=lambda x: x[1])
                            # print(lstSpecialNumsDECLINE)
                            countr += 1
                            if countr > 100:
                                lstSpecialNumsDECLINE.pop()
                                # print(len(lstSpecialNumsDECLINE))
                        if SpecialValue > 0:
                            lstSpecialNumsINCLINE.append([(j, k, c),SpecialValue])
                            lstSpecialNumsINCLINE = sorted(lstSpecialNumsINCLINE, key=lambda x: x[1], reverse=True)
                            # print(lstSpecialNumsINCLINE)
                            countrUp += 1
                            if countrUp > 100:
                                lstSpecialNumsINCLINE.pop()
                                # print(len(lstSpecialNumsINCLINE))
                                
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
        
        
        return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE
    except KeyboardInterrupt:
        print("\n\nSIMULATION RESULTS: ")
        print(lstSpecialNumsINCLINE)
        
        print(lstSpecialNumsDECLINE)
        
        f = open("documents/lstSpecialNumsINCLINE.txt", 'w')
        f.write(str(lstSpecialNumsINCLINE))
        f.close()
        f = open("documents/lstSpecialNumsDECLINE.txt", 'w')
        f.write(str(lstSpecialNumsDECLINE))
        f.close()
        print("\nBest Special Value: " + str(bestSpecialValue))
        print("Values for which: " + str(BestSpecialValues))
        print("\nWorst Special Value: " + str(worstSpecialValue))
        print("Values for which" + str(WorstSpecialValues))
        return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE




if "__main__" == __name__:
    symbolVolume = "BTCUSDT"
    printing = True
    df = formatDataset2(formatDataset3(grabForex(5000)))
    # df = formatDataset1(formatDataset(calltimes30FIXED(symbolVolume, (datetime.now()-timedelta(days=30)).strftime('%Y-%m-%d'))))
    print(len(df))

    bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE = simulateCrypto(df)
    
    print("\n\nSIMULATION RESULTS: ")
    print(lstSpecialNumsINCLINE)
    print(lstSpecialNumsDECLINE)
    f = open("documents/lstSpecialNumsINCLINE.txt", 'w')
    f.write(str(lstSpecialNumsINCLINE))
    f.close()
    f = open("documents/lstSpecialNumsDECLINE.txt", 'w')
    f.write(str(lstSpecialNumsDECLINE))
    f.close()

    
    print("\nBest Special Value: " + str(bestSpecialValue))
    print("Values for which: " + str(BestSpecialValues))
    print("\nWorst Special Value: " + str(worstSpecialValue))
    print("Values for which" + str(WorstSpecialValues))
