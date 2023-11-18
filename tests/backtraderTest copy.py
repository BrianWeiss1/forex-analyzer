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

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
def getData():
    # df = calltimes30('BONDUSDT')
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df)
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
    )
    def __init__(self):
        self.opening_range_low = 0
        self.opening_range_high = 0
        self.opening_range = 0
        self.bought_today = False
        self.order = None
        self.long = False
        self.short = False
        self.startTime = dfIndex
        self.i = 0
        self.longPrice = None
        self.shortPrice = None
        
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
        # if self.position and self.short:
        #     if 
        opp = False
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

        if not opp:
            if rsiK[i - 5] > rsiD[i - 5]  and rsiK[i] < rsiD[i]:
                if self.position:
                    self.close() #size=self.position.size
                self.order = self.sell() #price=self.data.close[0], size=size
                self.short = True
                self.long = False
                self.shortPrice = self.data.close[0]
            elif rsiK[i - 5] < rsiD[i - 5] and rsiK[i] >rsiD[i]:
                if self.position:
                    self.close() #size=self.position.size
                self.order = self.buy() # price=self.df_data.close[0], size=size
                self.long = True
                self.short = False
                self.longPrice = self.data.close[0]
        if opp:
            if rsiK[i - 5] > rsiD[i - 5] and 0.05 + rsiK[i] < rsiD[i]:
                if self.position:
                    self.close() #size=self.position.size
                self.order = self.buy() #price=self.data.close[0], size=size
                self.long = True
                self.short = False
                self.longPrice = self.data.close[0]

            elif rsiK[i - 5] < rsiD[i - 5] and rsiK[i] > 0.05 + rsiD[i]:
                if self.position:
                    self.close() #size=self.position.size
                self.order = self.sell() # price=self.df_data.close[0], size=size
                self.short = True
                self.long = False
                self.shortPrice = self.data.close[0]
        self.i += 1
for i in range(10):
    # stop_loss_percent = f"0.01{i}"
    # stop_loss_percent = float(stop_loss_percent)
    # take_profit_percent = 0.02
    cerebro = bt.Cerebro()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    df = getData()
    stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, 348, 4, 445)

    # stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, 1081, 3, 724)
    stochRSIk = np.array(stochRSIK)                
    stochRSId = np.array(stochRSID)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(OpeningRangeBreakout, rsiK=stochRSIk, rsiD=stochRSId)
    cerebro.broker.setcommission(commission=0.0018, leverage=150)
    cerebro.run()


    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()