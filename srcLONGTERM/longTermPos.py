
def findPos(data, pastI, currentI, BuyOrSell, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg):
    betPercent = 0.1
    # multiplierBuy = 1.000500
    # multiplierSell = 0.99980

    p = 0.5
    q = 1-p
    b = 1.00048
    f = p - (q/b)
    betPercent = f

    if len(pastI) == 1:
        # do normal
        bet = betPercent * portfolio
        portfolio = portfolio - (bet)
        if BuyOrSell:
            if data['close'][currentI] > data['close'][pastI[0]]:
                # if close is higher than past close, it's a profitable buy
                pos += 1
                currentPipChange = abs((data['close'][currentI]*100)-(100*data['close'][pastI[0]]))
                currentPrice = data['close'][currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100
                portfolio = portfolio + (bet * changeDecimal+1)
                
                totalPips += currentPipChange
                posPips += currentPipChange
                countPos += 1
                countPips+=1
            elif data['close'][currentI] == data['close'][pastI[0]]:
                print(pastI)
                print(currentI)
                nuet += 1
                portfolio = portfolio + (bet)
            else:
                # if close isn't higher than past close, and it isn't equal, it's a unprofitable buy
                neg += 1
                currentPipChange = abs((100*data['close'][pastI[0]])-(data['close'][currentI]*100))
                currentPrice = data['close'][currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100    
                portfolio = portfolio + (bet * changeDecimal+1)


                totalPips -= currentPipChange
                negPips -= currentPipChange
                countNeg += 1
                countPips += 1
        if not BuyOrSell:
            # If not buy, it must be a sell
            if data['close'][currentI] < data['close'][pastI[0]]:
                # if close is lower than past close, it's a profitable sell
                pos += 1
                currentPipChange = abs((data['close'][currentI]*100)-(100*data['close'][pastI[0]]))
                currentPrice = data['close'][currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100
                portfolio = portfolio + (bet * changeDecimal+1)
                
                totalPips += currentPipChange
                posPips += currentPipChange
                countPos += 1
                countPips+=1
            elif data['close'][currentI] == data['close'][pastI[0]]:
                nuet += 1
                portfolio = portfolio + (bet)
            else:
                # if close isn't lower than past close, and it isn't equal, it's a unprofitable sell
                neg += 1
                currentPipChange = abs((100*data['close'][pastI[0]])-(data['close'][currentI]*100))
                currentPrice = data['close'][currentI]
                percentChange = currentPipChange/currentPrice
                changeDecimal = percentChange/100    
                portfolio = portfolio + (bet * changeDecimal+1)


                totalPips -= currentPipChange
                negPips -= currentPipChange
                countNeg += 1
                countPips += 1

        pastI = []

    elif len(pastI) > 1:
        for i in range(len(pastI)):
            bet = betPercent * portfolio
            portfolio = portfolio - (bet)
            if BuyOrSell:
                if data['close'][currentI] > data['close'][pastI[i]]:
                    # if close is higher than past close, it's a profitable buy
                    pos += 1
                    currentPipChange = abs((data['close'][currentI]*100)-(100*data['close'][pastI[i]]))
                    currentPrice = data['close'][currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100
                    portfolio = portfolio + (bet * changeDecimal+1)
                    
                    totalPips += currentPipChange
                    posPips += currentPipChange
                    countPos += 1
                    countPips+=1
                elif data['close'][currentI] == data['close'][pastI[i]]:
                    nuet += 1
                    portfolio = portfolio + (bet)
                else:
                    # if close isn't higher than past close, and it isn't equal, it's a unprofitable buy
                    neg += 1
                    currentPipChange = abs((100*data['close'][pastI[i]])-(data['close'][currentI]*100))
                    currentPrice = data['close'][currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100    
                    portfolio = portfolio + (bet * changeDecimal+1)


                    totalPips -= currentPipChange
                    negPips -= currentPipChange
                    countNeg += 1
                    countPips += 1
            if not BuyOrSell:
                # If not buy, it must be a sell
                if data['close'][currentI] < data['close'][pastI[i]]:
                    # if close is lower than past close, it's a profitable sell
                    pos += 1
                    currentPipChange = abs((data['close'][currentI]*100)-(100*data['close'][pastI[i]]))
                    currentPrice = data['close'][currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100
                    portfolio = portfolio + (bet * changeDecimal+1)
                    
                    totalPips += currentPipChange
                    posPips += currentPipChange
                    countPos += 1
                    countPips+=1
                elif data['close'][currentI] == data['close'][pastI[i]]:
                    nuet += 1
                    portfolio = portfolio + (bet)
                else:
                    # if close isn't lower than past close, and it isn't equal, it's a unprofitable sell
                    neg += 1
                    currentPipChange = abs((100*data['close'][pastI[i]])-(data['close'][currentI]*100))
                    currentPrice = data['close'][currentI]
                    percentChange = currentPipChange/currentPrice
                    changeDecimal = percentChange/100    
                    portfolio = portfolio + (bet * changeDecimal+1)


                    totalPips -= currentPipChange
                    negPips -= currentPipChange
                    countNeg += 1
                    countPips += 1
        pastI = []
    return pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg



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
        shortI['sellSignal'] = True
        shortI['entry'] = [i]
    elif previousBuy and longI['buySignal']:
        longI['entry'].append(i)
    elif previousSell and shortI['shortSignal']:
        shortI['entry'].append(i)
    elif previousBuy:
        shortI['shortSignal'] = False
        longI['luquidate'] = True
        longI['buySignal'] = True
        longI['entry'] = [i]
    elif previousSell:
        longI['buySignal'] = False
        shortI['luquidate'] = True
        shortI['sellSignal'] = True
        shortI['entry'] = [i]
    return longI, shortI

def checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg):
    if shortI['luquidate']:
        BuyOrSell = False
        pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, longI['entry'], i, BuyOrSell, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg) # Logic to close short position
        longI['entry'] = []
        shortI['luquidate'] = False
    if longI['luquidate']:
        BuyOrSell = True
        pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, shortI['entry'], i, BuyOrSell, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg) # Logic to close long position
        shortI['entry'] = []
        longI['luquidate'] = False
    return shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg
    

        

        

