def SMA(closedValues):
    close_prices = closedValues
    sma_period = 14 
    sma = close_prices.rolling(window=sma_period).mean()
    return sma