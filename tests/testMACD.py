import pandas as pd

def get_macd(price, slow, fast, smooth):
    price = price['close']
    exp1 = price.ewm(span = fast, adjust = False).mean()
    exp2 = price.ewm(span = slow, adjust = False).mean()
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'close':'macd'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    frames =  [macd, signal, hist]
    df = pd.concat(frames, join = 'inner', axis = 1)
    return df
def solveSlope(last_3_macd):
    first = last_3_macd[0]
    sumOf = 0
    for i in range(len(last_3_macd)):
        sumOf+=last_3_macd[i]
    return ((sumOf)-first*len(last_3_macd))/len(last_3_macd)

def findMACDslope(MACDdata, amount, amount2):
    last_3_macd = MACDdata['macd'].tail(amount)
    last_5_macd = MACDdata['macd'].tail(amount2)

    slope3 = solveSlope(last_3_macd)
    slope5 = solveSlope(last_5_macd)

    return slope3, slope5

def findMACDslopeSIM(MACDdata, amount, amount2, i):
    last_3_macd = MACDdata['macd'][i-amount:i]
    last_5_macd = MACDdata['macd'][i-amount2:i]

    slope3 = solveSlope(last_3_macd)
    slope5 = solveSlope(last_5_macd)
    
    return slope3, slope5