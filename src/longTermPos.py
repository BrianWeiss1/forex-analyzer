import numpy as np
def findPos(data, pastI, currentI, BuyOrSell, pos, nuet, neg, posPips, negPips):
    betPercent = 0.1


    if len(pastI) == 1:
        if BuyOrSell:
            if data[currentI] > data[pastI[0]]:
                # if close is higher than past close, it's a profitable buy
                pos += 1
                currentPipChange = abs((data[currentI]*100)-(100*data[pastI[0]]))
                currentPrice = data[currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100
                posPips += currentPipChange
            elif data[currentI] == data[pastI[0]]:

                nuet += 1
            else:
                # if close isn't higher than past close, and it isn't equal, it's a unprofitable buy
                neg += 1
                currentPipChange = abs((100*data[pastI[0]])-(data[currentI]*100))
                currentPrice = data[currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = -percentChange/100  
                negPips -= currentPipChange
        if not BuyOrSell:
            # If not buy, it must be a sell
            if data[currentI] < data[pastI[0]]:
                # if close is lower than past close, it's a profitable sell
                pos += 1
                currentPipChange = abs((data[currentI]*100)-(100*data[pastI[0]]))
                currentPrice = data[currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100
                
                posPips += currentPipChange
            elif data[currentI] == data[pastI[0]]:
                nuet += 1
            else:
                # if close isn't lower than past close, and it isn't equal, it's a unprofitable sell
                neg += 1
                currentPipChange = abs((100*data[pastI[0]])-(data[currentI]*100))
                currentPrice = data[currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = -percentChange/100    
                negPips -= currentPipChange

        pastI = []

    elif len(pastI) > 1:
        for i in range(len(pastI)):
            if BuyOrSell:
                if data[currentI] > data[pastI[i]]:
                    # if close is higher than past close, it's a profitable buy
                    pos += 1
                    currentPipChange = abs((data[currentI]*100)-(100*data[pastI[i]]))
                    currentPrice = data[currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100
                    posPips += currentPipChange
                elif data[currentI] == data[pastI[i]]:
                    nuet += 1
                else:
                    # if close isn't higher than past close, and it isn't equal, it's a unprofitable buy
                    neg += 1
                    currentPipChange = abs((100*data[pastI[i]])-(data[currentI]*100))
                    currentPrice = data[currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100    
                    changeDecimal = -changeDecimal
                    negPips -= currentPipChange
            if not BuyOrSell:
                # If not buy, it must be a sell
                if data[currentI] < data[pastI[i]]:
                    # if close is lower than past close, it's a profitable sell
                    pos += 1
                    currentPipChange = abs((data[currentI]*100)-(100*data[pastI[i]]))
                    # currentPipChange = -currentPipChange
                    currentPrice = data[currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100
                    
                    posPips += currentPipChange
                elif data[currentI] == data[pastI[i]]:
                    nuet += 1
                else:
                    # if close isn't lower than past close, and it isn't equal, it's a unprofitable sell
                    neg += 1
                    currentPipChange = abs((100*data[pastI[i]])-(data[currentI]*100))
                    currentPrice = data[currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100    
                    changeDecimal = -changeDecimal
                    negPips -= currentPipChange
        pastI = []
    return pos, nuet, neg, posPips, negPips



def findSelection(previousBuy, previousSell, longI, shortI, i):
    # Logic to determine how a long or short position will be opened
    if previousBuy and shortI['shortSignal']:
        shortI['shortSignal'] = False
        longI['luquidate'] = True
        longI['buySignal'] = True
        longI['entry'] = [i]
    elif previousSell and longI['buySignal']:
        longI['buySignal'] = False
        shortI['luquidate'] = True
        shortI['shortSignal'] = True
        shortI['entry'] = [i]
    elif previousBuy and longI['buySignal']:
        longI['entry'].append(i)
    elif previousSell and shortI['shortSignal']:
        shortI['entry'].append(i)
    elif previousBuy:
        shortI['shortSignal'] = False
        longI['buySignal'] = True
        longI['entry'] = [i]
    elif previousSell:
        longI['buySignal'] = False
        shortI['shortSignal'] = True
        shortI['entry'] = [i]
    return longI, shortI

def checkLuquidation(shortI, longI, data, i, pos, nuet, neg, posPips, negPips):
    if shortI['luquidate']:
        BuyOrSell = False
        pos, nuet, neg, posPips, negPips = findPos(data, longI['entry'], i, BuyOrSell, pos, nuet, neg, posPips, negPips) # Logic to close short position
        longI['entry'] = []
        shortI['luquidate'] = False
    if longI['luquidate']:
        BuyOrSell = True
        pos, nuet, neg, posPips, negPips = findPos(data, shortI['entry'], i, BuyOrSell, pos, nuet, neg, posPips, negPips) # Logic to close long position
        shortI['entry'] = []
        longI['luquidate'] = False
    return shortI, longI, pos, nuet, neg, posPips, negPips
    

        

        

