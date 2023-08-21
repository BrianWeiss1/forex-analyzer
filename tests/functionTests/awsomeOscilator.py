import pandas as pd
def sma(price, period):
    sma = price.rolling(period).mean()
    return sma

def ao(data, period1=5, period2=34):
    price = data['close']
    median = price.rolling(2).median()
    short = sma(median, period1)
    long = sma(median, period2)
    ao = short - long
    data['ao'] = pd.DataFrame(ao)
    return data

def AwesomeData(data):
    previousBuy = previousSell = None
    if (previousBuy == None or previousBuy == False) and (previousSell == None or previousSell == False):
        if data['ao'][i-1] < 0 and data['ao'][i] > 0:
            previousSell = True
        elif data['ao'][i-1] > 0 and data['ao'][i] < 0:   
            previousBuy = True
    elif previousSell:
        if data['ao'][i-1] < 0 and data['ao'][i] > 0:
            previousSell = True
        elif data['ao'][i-1] > 0 and data['ao'][i] < 0:  
            previousSell = False
    elif previousBuy:
        if data['ao'][i-1] < 0 and data['ao'][i] > 0:
            previousBuy = False
        elif data['ao'][i-1] > 0 and data['ao'][i] < 0:  
            previousBuy = True
    return previousBuy, previousSell
# prevBuy, prevSell = AwesomeData()