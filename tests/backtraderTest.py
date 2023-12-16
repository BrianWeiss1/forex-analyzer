import backtrader as bt
from SpecialFunctions import formatDataset
from V3.testGrabData import calltimes30
from testCounter import run
import decimal
import numpy as np
from ta.momentum import StochRSIIndicator
import concurrent.futures

hiddenNums = (130, 2, 24) 
hiddenNums1 = (130, 2, 24)
stop_loss_price = 1
currentPositions = {}

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
def getData():
    # Ones That Made it: BTC, 
#symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "ADAUSDT", "TRONUSDT", "LINKUSDT", "MATICUSDT"]
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df[0:len(df)])
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
        ('rsiK2', None),  # External NumPy array for stochRSIK3
        ('rsiD2', None),  # External NumPy array for stochRSID3
        ('j', None),

    )
    def __init__(self):
        self.i = 0
        self.size = 0
        self.stopMachine = False
        self.betPercent = 0.14 # I'm not sure if I should stack indicators since this is so high
        self.stop_loss_percentage = 0.012
        
        self.shortPrice = self.shortPrice1 = self.shortPrice2 = self.shortPrice3 = self.shortPrice4 = self.shortPrice5 = self.shortPrice6 = self.shortPrice7 = self.shortPrice8 = self.shortPrice9 = self.shortPrice1 = None
        self.longPrice = self.longPrice1 = self.longPrice2 = self.longPrice3 = self.longPrice4 = self.longPrice5 = self.longPrice6 = self.longPrice7 = self.longPrice8 = self.longPrice9 = self.longPrice1 = None
        self.short = self.short2 = self.short3 = self.short4 = self.short5 = self.short6 = self.short7 = self.short8 = self.short9 = self.short10 = False
        self.long = self.long2 = self.long3 = self.long4 = self.long5 = self.long6 = self.long7 = self.long8 = self.long9 = self.long10 = False

        #1.0782222930632772e+303 from 75
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
        
        
    def notify_order(self, order):
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
        #1.935794646847023e+301 from 80
    def next(self):
        if not self.stopMachine:
            i = self.i
            rsiK = self.params.rsiK
            rsiD = self.params.rsiD
            rsiK2 = self.params.rsiK2
            rsiD2 = self.params.rsiD2
            
            def ind1Logic():
                if self.long and self.data.close[0] < (1 - self.stop_loss_percentage) * self.longPrice: 
                    self.close()
                if self.short and self.data.close[0] > (1 + self.stop_loss_percentage) * self.shortPrice: 
                    self.close() 
                if rsiK[i - 1] < rsiD[i - 1] and rsiK[i] > rsiD[i]:
                    if self.short:
                        self.close() 
                    self.size = ((self.betPercent * self.broker.cash) / self.data.close[0])
                    self.order = self.buy(size=self.size)
                    if currentPositions.get('long1') is None:
                        currentPositions['long1'] = [self.size, self.data.close[0]]
                    else:
                        currentPositions['long1'].append([self.size, self.data.close[0]])
                    self.long = True
                    self.short = False
                    self.longPrice = self.data.close[0]
                elif rsiK[i-1] > rsiD[i-1] and rsiK[i] < rsiD[i]:
                    if self.long: 
                        self.close()
                    self.size = ((self.betPercent * self.broker.cash)/ self.data.close[0])
                    self.order = self.sell(size=self.size) 
                    if currentPositions.get('short1') is None:
                        currentPositions['short1'] = [self.size, self.data.close[0]]
                    else:
                        currentPositions['short1'].append([self.size, self.data.close[0]])
                    self.long = False
                    self.short = True  
                    self.shortPrice = self.data.close[0]
            def ind2Logic():
                if self.long2 and self.data.close[0] < (1 - self.stop_loss_percentage) * self.longPrice2: 
                    self.close(size=self.size)
                if self.short2 and self.data.close[0] > (1 + self.stop_loss_percentage) * self.shortPrice:
                    self.close() 
                    
                if rsiK2[i - 1] < rsiD2[i - 1] and rsiK2[i] > rsiD2[i]:
                    if self.position:
                        self.close() 
                    self.size = (self.betPercent * self.broker.cash)
                    self.order = self.buy(size=self.size)
                    self.long2 = True
                    self.short2 = False
                    self.longPrice2 = self.data.close[0]
                elif rsiK2[i-1] > rsiD2[i-1] and rsiK2[i] < rsiD2[i]: 
                    if self.position:
                        self.close()
                    self.size = (self.betPercent * self.broker.cash)
                    self.order = self.sell(size=self.size) 
                    self.long2 = False
                    self.short2 = True  
                    self.shortPrice2 = self.data.close[0]                
            ind1Logic()
            print(currentPositions)
            
            
            
            
            #PRIOR: [[(84, 3, 28), 2.4744907683170743e+191], [(84, 3, 43), 8.390303035431468e+140], [(130, 2, 24), 2.246013891772523e+216], [(66, 3, 28), 1.6453612440390208e+202], [(41, 3, 105), 4.975049423779153e+171], [(42, 3, 96), 3.7953084085630574e+158], [(43, 3, 90), 2.0742333060340744e+146], [(78, 3, 46), 1.0766178556528188e+148], [(114, 3, 35), 1.0217120405335898e+130], [(99, 2, 48), 3.135681021030289e+185]]
            if self.broker.cash < 0:
                self.stopMachine = True
                lastVal = self.broker.cash
            if np.isinf(self.broker.cash):
                self.stopMachine = True
                self.broker.cash = np.inf
                lastVal = np.inf

            self.i += 1
            lastVal = self.broker.cash

def run_strategy(hiddenNums):
    print(hiddenNums)
    # print(i)
    try:
        value=hiddenNums
        i = 0
        cerebro = bt.Cerebro()
        cerebro.broker.set_cash(10.00)
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        df = getData()
        stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, hiddenNums[0], hiddenNums[1], hiddenNums[2])
        stochRSIk = np.array(stochRSIK)
        stochRSId = np.array(stochRSID)
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)
        cerebro.addstrategy(OpeningRangeBreakout, rsiK=stochRSIk, rsiD=stochRSId, j=i)
        cerebro.broker.setcommission(commission=0.0018, mult=75)
        cerebro.run()
        finalBlanace = cerebro.broker.getvalue()
        print('Final Portfolio Value: %.2f' % finalBlanace)
        if np.isinf(lastVal):
            print("ACTUAL VALUE: " + str(lastVal))
            return finalBlanace, lastVal 
        # if np.isnp.nan(finalBlanace):
        #     return i
        # elif np.isinf(finalBlanace):
        
        #     return 5
        return finalBlanace, value
    except Exception as e:
        print(f"Exception in run_strategy: {e}")
        return None
    print(i)
    # cerebro.plot()
    return None
lastVal =  0
if __name__ == '__main__':
    lastVal =  0
    lst = []
    lstinf = []
    lstSet =  [(84, 3, 28), (84, 3, 43), (130, 2, 24), (66, 3, 28), (41, 3, 105), (42, 3, 96), (43, 3, 90), (78, 3, 46), (114, 3, 35), (99, 2, 48)] # weird how they all are between 1:100, 1:3, 1:100 conicidence? I think NOT
    # lstSet = [lstSet[]]
    
    
    dataAnylsis = False
    Parrel = False
    i = 2
    if Parrel:
        
        if i == 1:
            # Define the range of values for 'i'
            range_values = list(range(0, 100, 1))
            # combinations = list(itertools.product([[195, 89, 18]], range_values))
            # print(combinations)
            # Use concurrent.futures for parallel execution
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = executor.map(run_strategy, lstSet)

            # Process the results
            print(results)
            sum = 0
            for result in results:
                if result is not None:
                    j, message = result
                    lst.append([j, message])
                    sum+=decimal(message)
            print(sum)
            # print(lst)
            # print(lstinf)
            print(lst)
            total_sum = 0
            for value in lst:
                if isinstance(value[0], (int, float)):
                    print(f"{value[0]} from {value[1]}")
                    # total_sum += value

            # print(total_sum)
            
            
        if i == 2:
            sum = decimal.Decimal(0)
            # print(sum)
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = executor.map(run_strategy, lstSet)
            lst = []
            for result in results:
                if result is not None:
                    balance, j = result
                    print(balance)
                    if not np.isnan(balance):
                        sum+=decimal.Decimal(balance)  
                    lst.append([j, balance]) 
            print(sum)
            print(lst)
        # if i == 3:
            

    else:
        i = 0
        cerebro = bt.Cerebro()
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        df = getData()
        stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(df, hiddenNums[0], hiddenNums[1], hiddenNums[2])
        stochRSIk = np.array(stochRSIK)
        stochRSId = np.array(stochRSID)
        stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(df, hiddenNums1[0], hiddenNums1[1], hiddenNums1[2])
        stochRSIk2 = np.array(stochRSIK)
        stochRSId2 = np.array(stochRSID)
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)
        cerebro.addstrategy(OpeningRangeBreakout, rsiK=stochRSIk, rsiD=stochRSId, rsiK2=stochRSIk2, rsiD2=stochRSId2, j=i)
        cerebro.broker.setcommission(commission=0.0018, mult=75)
        cerebro.run()
        finalBlanace = cerebro.broker.getvalue()
        print('Final Portfolio Value: %.2f' % finalBlanace)
        if np.isnan(finalBlanace):
            print( i, "added it!!!")
        elif np.isinf(finalBlanace):
            print( i, "added it (inf)!!!")
        print(i)
        cerebro.plot()
        
        if dataAnylsis:
            data = []
            sorted_data = sorted(data, key=lambda x: (np.isnan(x[1]), x[1]), reverse=True)

            print(sorted_data[0:-50])
            print(len(sorted_data[0:-82]))
            data = sorted_data[0:-81]
            indicatorList = []
            sum = decimal.Decimal(0)
            for i in data:
                indicatorList.append(i[0])
                if not np.isnan(i[1]):
                    sum+=decimal.Decimal(i[1])  
            print(indicatorList)
            print(sum)
