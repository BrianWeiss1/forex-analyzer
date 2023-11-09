def STOCH(i, stochK, stochD, stochK2, stochD2, stochK3, stochD3, stochK4, stochD4, stochK5, stochD5, stochK6, stochD6, stochK7, stochD7):
    previousSell = previousBuy = False
    if stochK[i-1] >= stochD[i-1] and stochK[i] < stochD[i]:
        previousSell = True
    if stochK[i-1] <= stochD[i-1] and stochK[i] > stochD[i]:
        previousBuy = True            

    if stochK2[i-1] >= stochD2[i-1] and stochK2[i] < stochD2[i]:
        previousSell = True
    if stochK2[i-1] <= stochD2[i-1] and stochK2[i] > stochD2[i]:
        previousBuy = True

    if stochK3[i-1] >= stochD3[i-1] and stochK3[i] < stochD3[i]:
        previousSell = True
    if stochK3[i-1] <= stochD3[i-1] and stochK3[i] > stochD3[i]:
        previousBuy = True

    if stochK4[i-1] >= stochD4[i-1] and stochK4[i] < stochD4[i]:
        previousSell = True
    if stochK4[i-1] <= stochD4[i-1] and stochK4[i] > stochD4[i]:
        previousBuy = True

    if stochK5[i-1] >= stochD5[i-1] and stochK5[i] < stochD5[i]:
        previousSell = True
    if stochK5[i-1] <= stochD5[i-1] and stochK5[i] > stochD5[i]:
        previousBuy = True

    if stochK6[i-1] >= stochD6[i-1] and stochK6[i] < stochD6[i]:
        previousSell = True
    if stochK6[i-1] <= stochD6[i-1] and stochK6[i] > stochD6[i]:
        previousBuy = True

    if stochK7[i-1] >= stochD7[i-1] and stochK7[i] < stochD7[i]:
        previousSell = True
    if stochK7[i-1] <= stochD7[i-1] and stochK7[i] > stochD7[i]:
        previousBuy = True

    if previousBuy and previousSell:
        previousBuy = False
        previousSell = False

    return previousBuy, previousSell
def swap(previousBuyStochasticRSI6, previousSellStochasticRSI6):
    return previousBuyStochasticRSI6, previousSellStochasticRSI6
