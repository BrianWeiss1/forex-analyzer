import backtrader as bt
from SpecialFunctions import formatDataset
from V3.testGrabData import calltimes30
import config
from datetime import date, datetime, time, timedelta
# from functions import get_StochasticRelitiveStrengthIndex
from testCounter import run
import decimal
import numpy as np
from ta.momentum import StochRSIIndicator
import concurrent.futures

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
def getData():
    # calltimes30('BTCUSDT')
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df[len(df)-17500:len(df)])
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    for column in columns_to_convert:
        df[column] = df[column].apply(float)
    global dfIndex
    dfIndex = df.index[0]
    return df
run()
class OpeningRangeBreakout(bt.Strategy):
    params = (
        ('rsiK', None),  # External NumPy array for stochRSIK3
        ('rsiD', None),  # External NumPy array for stochRSID3
        # ('k', None),
        # ('j', None),
    )
    def __init__(self):
        self.order = None
        self.i = 0
        self.betPercent = 0.1 # I'm not sure if I should stack indicators since this is so high
        self.shortCount = 0
        self.longCount = 0
        
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
        
        
    def notify_order(self, order):
        return
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return
        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        # Write down: no pending order
        self.order = None
        
    def next(self):
        i = self.i
        rsiK = self.params.rsiK
        rsiD = self.params.rsiD

        if rsiK[i-1] < rsiD[i-1] and rsiK[i] > (rsiD[i]*1.4067):
            self.shortCount = 1
        else:
            self.shortCount = 0
        if rsiK[i-1] > rsiD[i-1] and (rsiK[i]*1.4023) < rsiD[i]:
            self.longCount = 1
        else:
            self.longCount = 0
            
        if self.longCount == 1:
            self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
            self.order = self.buy(size=self.size)
        elif self.shortCount == 1:
            self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
            self.order = self.close(size=self.size)
      
        self.i += 1
        
def run_strategy(j, k, df, stochRSIk, stochRSId):
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(1.00)
    print(f'{j}')
    print(f'{k}')
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(OpeningRangeBreakout, rsiK=stochRSIk, rsiD=stochRSId)
    cerebro.broker.setcommission(mult=53)
    cerebro.run()

    finalVal = cerebro.broker.getvalue()
    print('Final Portfolio Value: %.2f' % finalVal)
    return [(j, k), finalVal]

if __name__ == "__main__":
    maxFinalVal = -1
    maxFinalSym = -1    
    lst = []

    df = getData()
    stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, 73, 1, 21)
    stochRSIk = np.array(stochRSIK)                
    stochRSId = np.array(stochRSID)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(run_strategy, j, k, df, stochRSIk, stochRSId) 
                   for j in range(10) for k in range(10)]
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            lst.append(result)
            if result[1] > maxFinalVal:
                maxFinalVal = result[1]
                maxFinalSym = result[0]

    sortedLst = sorted(lst, key=lambda x: x[1])
    print(maxFinalVal, maxFinalSym)
    print(sortedLst)
