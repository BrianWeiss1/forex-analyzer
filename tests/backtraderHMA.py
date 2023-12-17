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
import pandas_ta as ta
import pandas as pd

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()

def get_HMA(df: pd.DataFrame, period_1: int, period_2: int) -> pd.Series:
    hma_1 = ta.hma(df["close"], period_1)
    hma_2 = ta.hma(df["close"], period_2)    
    return hma_1, hma_2

def getData():
    # calltimes30('BTCUSDT')
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df[len(df)-17500:len(df)-600])
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    for column in columns_to_convert:
        df[column] = df[column].apply(float)
    global dfIndex
    dfIndex = df.index[0]
    return df
run()
class OpeningRangeBreakout(bt.Strategy):
    params = (
        ('hull_20', None),  # External NumPy array for stochRSIK3
        ('hull_50', None),  # External NumPy array for stochRSID3
    )
    def __init__(self):
        self.opening_range_low = 0
        self.opening_range_high = 0
        self.opening_range = 0
        self.bought_today = False
        self.order = None
        self.long = True
        self.short = True
        self.startTime = dfIndex
        self.i = 0
        self.shortPrice = None
        self.longPrice = None
        self.betPercent = 0.1 # I'm not sure if I should stack indicators since this is so high
        self.shortCount = 0
        self.longCount = 0
        self.cross = ""
        self.hullSignal = ""
        
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
        hull_20 = self.params.hull_20
        hull_50 = self.params.hull_50
        hull_50 = hull_50
        hull_20 = hull_20
        # print(self.data.open[-1])
        # print(self.data.open[0])
        # current_bar_datetime = self.data.num2date(self.data.datetime[0])        
        # previous_bar_datetime = self.data.num2date(self.data.datetime[-1])
        # print(previous_bar_datetime)
        # print(current_bar_datetime)
        # if current_bar_datetime.date() != previous_bar_datetime.date(): # every day
        #     self.opening_range_low = self.data.low[0]
        #     self.opening_range_high = self.data.high[0]
        #     self.bought_today = False
        # opening_range_start_time = time(0, 0, 0)
        # dt = datetime.combine(date.today(), opening_range_start_time) + timedelta(minutes=1)
        # amount_to_spend = 1000  # Replace with your desired amount
        # current_price = self.data.close[0]
        # size = int(amount_to_spend / current_price)
        # opening_range_end_time = dt.time()
        # if current_bar_datetime.time() >= opening_range_start_time \
        #     and current_bar_datetime.time() < opening_range_end_time: 
        #     self.opening_range_low = min(self.data.low[0], self.opening_range_low)
        #     self.opening_range_high = max(self.data.high[0], self.opening_range_high)
        #     self.opening_range = self.opening_range_high - self.opening_range_low
        # else:
        # if self.long and self.position:
        #     stop_loss_price = self.longPrice * (1 - stop_loss_percent)
        #     # take_profit_price = self.longPrice * (1 + take_profit_percent)

        #     if self.data.close[0] <= stop_loss_price:
        #         self.close()  # Close the long
        #     # elif self.data.close[0] >= take_profit_price:
        #     #     self.close()  # Close the long position if take-profit is triggered
        # if self.short and self.position:
        #     stop_loss_price = self.shortPrice * (1 + stop_loss_percent)
        #     # take_profit_price = self.shortPrice * (1 - take_profit_percent)

        #     if self.data.close[0] <= stop_loss_price:
        #         self.close()  # Close the long
        #     # elif self.data.close[0] >= take_profit_price:
        #     #     self.close()  # Close the long position if take-profit is triggered
        if not np.isnan(hull_20[i]) and not np.isnan(hull_50[i]):  
            if hull_20[i] > hull_50[i]:
                if self.data.close[0] > hull_20[i]:
                    self.hullSignal = "BUY SIGNAL"
                elif self.data.close[0] < hull_20[i] and self.data.close[0] > hull_50[i]: 
                    self.hullSignal = "LUQUIDATE CURRENT POSITION"
                elif self.data.close[0] < hull_50[i]: 
                    self.hullSignal = "SELL SIGNAL"
                else:
                    print("ERROR 1")
            elif hull_50[i] > hull_20[i]:
                if self.data.close[0] > hull_50[i]:
                    self.hullSignal = "SELL SIGNAL"
                elif self.data.close[0] < hull_50[i] and self.data.close[0] > hull_20[i]:
                    self.hullSignal = "LUQUIDATE CURRENT POSITION"
                elif self.data.close[0] < hull_20[i]:
                    self.hullSignal = "BUY SIGNAL"
                else:
                    print("ERROR 2")
            elif hull_50[i] == hull_20[i]:
                print("EQUALITY ERROR 4")
            else:
                print(hull_50[i], hull_20[i])
                print("ERROR 3")
                
                        
            if hull_20[i-1] > hull_50[i-1] and hull_20[i] < hull_50[i] :
                self.shortCount += 1
            else:
                self.shortCount = 0
            if hull_20[i - 1] < hull_50[i - 1] and (hull_20[i]) > hull_50[i]:
                self.longCount += 1
            else:
                self.longCount = 0
                
            # '''
            if self.hullSignal == 'BUY SIGNAL':
                self.long = True
                self.short = False
                self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
                # if self.position:
                #     self.close() #size=self.position.size
                self.order = self.buy(size=self.size) #price=self.data.close[0], size=size

                self.longPrice = self.data.close[0]
            # '''
            
            # '''
            if self.hullSignal == 'SELL SIGNAL':
                self.short = True  
                self.long = False

                self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
                # if self.position:
                self.order = self.sell(size=self.size) # price=self.df_data.close[0], size=size
                # if self.broker.cash < 0.1*self.broker.getvalue():
                #     self.close()
                self.shortPrice = self.data.close[0]

            # '''
            # if self.broker.cash < 0.5*self.broker.getvalue():
            #         self.close()    
            if (self.longCount == 1 and self.short): #or self.hullSignal == 'BUY SIGNAL'
                self.long = True
                self.short = False
                self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
                # if self.position:
                #     self.close() #size=self.position.size
                self.order = self.buy(size=self.size) #price=self.data.close[0], size=size

                self.longPrice = self.data.close[0]
            elif (self.shortCount == 1 and self.long): #or self.hullSignal == 'SELL SIGNAL'
                self.long = False
                self.short = True  
                self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
                # if self.position:
                self.order = self.sell(size=self.size) # price=self.df_data.close[0], size=size
                self.shortPrice = self.data.close[0]
      
        self.i += 1
maxFinalVal = -1
maxFinalSym = -1  
lst = []  
k = -1
for k in range(0, 100, 1):
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(1.00)
    print(k)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    df = getData()
    hma_20, hma_50 = get_HMA(df, 27, 50)
    # stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, 7, 1, k) # 117
    # print(stochRSIK)
    npHMA_20 = np.array(hma_20)                
    npHMA_50 = np.array(hma_50)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(OpeningRangeBreakout, hull_20=npHMA_20, hull_50=npHMA_50)
    cerebro.broker.setcommission(mult=53)
    cerebro.run()
    finalVal = cerebro.broker.getvalue()
    print('Final Portfolio Value: %.2f' % finalVal + "\n")
    # cerebro.plot()
    lst.append([finalVal, k])
    if finalVal > maxFinalVal:
        maxFinalVal = finalVal
        maxFinalSym = k 


print(maxFinalVal, maxFinalSym)
sortedLst = sorted(lst, key=lambda x: x[0], reverse=True) # How to sort a lst by the first elemenet in python
print(lst)

print(sortedLst)