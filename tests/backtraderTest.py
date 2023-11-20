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
import itertools
#    lstSet =  [(78, 3, 46), (195, 89, 18), (290, 8, 209), (114, 3, 58), (105, 3, 46), (99, 3, 45), (290, 3, 214), (115, 3, 43), (92, 3, 45), (103, 2, 53), (258, 7, 212), (41, 3, 114), (52, 4, 262), (96, 3, 58), (53, 3, 257), (84, 4, 43), (139, 3, 51), (87, 2, 54), (53, 3, 269), (60, 2, 66), (41, 3, 105), (182, 11, 296), (66, 4, 69), (72, 4, 50), (223, 8, 266), (274, 5, 225), (245, 9, 194), (66, 3, 61), (226, 8, 249), (135, 2, 297), (58, 3, 97), (98, 3, 51), (55, 3, 102), (180, 11, 268), (204, 13, 231), (292, 14, 198), (245, 12, 188), (169, 2, 39), (101, 3, 36), (197, 3, 290), (133, 3, 29), (242, 11, 199), (70, 5, 43), (74, 3, 59), (197, 12, 234), (115, 3, 35), (194, 14, 246), (52, 3, 205), (43, 3, 90), (195, 12, 239), (274, 1, 274), (42, 3, 96), (180, 11, 277), (34, 4, 183), (66, 3, 28), (84, 3, 28), (148, 3, 36), (34, 4, 178), (274, 1, 266), (238, 3, 292), (179, 2, 29), (66, 3, 23), (168, 3, 26), (205, 3, 287), (141, 2, 29), (18, 6, 105), (114, 2, 48), (98, 3, 57), (50, 3, 266), (194, 4, 272), (50, 3, 253), (114, 5, 42), (151, 10, 181), (115, 3, 61), (194, 3, 299), (136, 2, 295), (50, 3, 259), (153, 3, 40), (146, 2, 41), (130, 3, 34), (131, 4, 42), (99, 2, 48), (98, 3, 70), (163, 2, 30), (140, 4, 49), (98, 3, 65), (114, 3, 53), (84, 3, 43), (98, 3, 42), (146, 3, 35), (194, 14, 240), (130, 4, 47), (146, 10, 191), (114, 3, 35), (148, 2, 178), (132, 3, 29), (163, 13, 8), (167, 2, 40), (148, 3, 28), (179, 11, 275), (114, 3, 66), (138, 2, 31), (168, 3, 28), (99, 4, 35), (130, 2, 24), (146, 3, 21), (66, 3, 24), (114, 3, 26), (154, 3, 28)]
#hesistant: [114, 3, 58], [79, 3, 216]
#[78, 3, 46], [290, 8, 209], [92, 3, 45], 
hiddenNums = (179, 2, 29) # 379, 3, 216 
stop_loss_price = 1
def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
def getData():
    # Ones That Made it: BTC, 
#symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "SOLUSDT", "ADAUSDT", "TRONUSDT", "LINKUSDT", "MATICUSDT"]
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df[len(df)-70000:len(df)-68000])
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
        ('j', None),

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
        self.shortPrice = None
        self.longPrice = None
        self.betPercent = 0.14 # I'm not sure if I should stack indicators since this is so high
        self.size = 0
        self.stopMachine = False
        stop_loss_percentage = f"0.012" #need this value, this or lower is required.
        self.stop_loss_percentage = float(stop_loss_percentage)
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
            
            
            if self.position and self.long and self.data.close[0] < (1 - self.stop_loss_percentage) * self.longPrice: #prior: [[(84, 3, 28), 1.4861467698959665e+192], [(84, 3, 43), 8.390303035431468e+140], [(130, 2, 24), 2.246013891772523e+216], [(66, 3, 28), 8.544174406628138e+201], [(41, 3, 105), 7.757502842264305e+171], [(42, 3, 96), 6.26539968915441e+158], [(43, 3, 90), 5.638268983752525e+146], [(78, 3, 46), 1.0952429407331773e+148], [(114, 3, 35), 1.0217120405335898e+130], [(99, 2, 48), 3.135681021030289e+185]]
                self.close()
            if self.position and self.short and self.data.close[0] > (1 + self.stop_loss_percentage) * self.short: #prior: [[(84, 3, 28), 1.4861467698959665e+192], [(84, 3, 43), 8.390303035431468e+140], [(130, 2, 24), 2.246013891772523e+216], [(66, 3, 28), 8.544174406628138e+201], [(41, 3, 105), 7.757502842264305e+171], [(42, 3, 96), 6.26539968915441e+158], [(43, 3, 90), 5.638268983752525e+146], [(78, 3, 46), 1.0952429407331773e+148], [(114, 3, 35), 1.0217120405335898e+130], [(99, 2, 48), 3.135681021030289e+185]]
                self.close() 
            if rsiK[i - 1] < rsiD[i - 1] and rsiK[i] > rsiD[i]:
                if self.position:
                    self.close() 
                self.size = (self.betPercent * self.broker.cash)
                self.order = self.buy(size=self.size)
                self.long = True
                self.short = False
                self.longPrice = self.data.close[0]
            elif rsiK[i-1] > rsiD[i-1] and rsiK[i] < rsiD[i]:
                if self.position:
                    self.close()
                self.size = (self.betPercent * self.broker.cash)
                self.order = self.sell(size=self.size) 
                self.long = False
                self.short = True  
                self.shortPrice = self.data.close[0]
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
    lstSet =  [(84, 3, 28), (84, 3, 43), (130, 2, 24), (66, 3, 28), (41, 3, 105), (42, 3, 96), (43, 3, 90), (78, 3, 46), (114, 3, 35), (99, 2, 48)]
    # lstSet = [lstSet[]]
    
    
    dataAnylsis = False
    Parrel = True
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
                    #[[2, 1.935794646847023e+301], [2, -1.7541193565950618e+78], [2, 8.91042898079313e+37], [2, 2.297374024072508e+252], [2, -2.161597934857899e+260], [2, 5.4929405719598e+258], [2, -3.93386466946166e+61], [2, -3.4218047023988907e+256], [2, 4.345319689056776e+272], [2, 8.346708492041984e+301], [2, 7.279091483600074e+55], [2, 1.710450823515068e+297], [2, 5.180727089070031e+198], [2, 1.5283951430880767e+245], [2, 2.6270058134493946e+223], [2, 3.866964561452851e+265], [2, 2.089831168507913e+219], [2, 1.6009171149004943e+298], [2, 2.3238734290318018e+230], [2, 4.999449321974848e+307], [2, 7.66187085656722e+307], [2, -2.0894925546559653e+39], [2, -3.188461602739346e+238], [2, -1.948030109527697e+267], [2, 2.467211086060584e+55], [2, 2.2353985156959003e+59], [2, -8.783476043567202e+46], [2, -8.643199844091132e+299], [2, 9.505008987689782e+47], [2, -2.2007511902060122e+110], [2, 8.923635897679127e+284], [2, 3.4599762430002835e+234], [2, 1.7143914455693136e+287], [2, -1.0206318665021566e+50], [2, -6.507008988297594e+43], [2, 1.062602007846162e+26], [2, 6.798422617767861e+43], [2, np.nan], [2, 2.720657167489855e+291], [2, 1.1151782714341413e+66], [2, 1.7397211736075855e+305], [2, -1.08421978555333e+43], [2, -2.0248327438354286e+266], [2, 7.653771740035359e+287], [2, 4.733306357755209e+41], [2, 1.78822951889474e+295], [2, -7.611772856819191e+39], [2, 7.661722946582369e+251], [2, 4.066522926496791e+307], [2, 5.0439205725135055e+41], [2, -1.1974503336967822e+90], [2, 7.601962918977266e+307], [2, -6.078571603397443e+42], [2, -1.3531271245698496e+301], [2, 1.5106499119908517e+308], [2, np.nan], [2, 1.5345549984311949e+273], [2, -3.314412004946957e+290], [2, -1.5239971149649626e+86], [2, 4.9049906655853505e+91], [2, np.nan], [2, np.nan], [2, np.nan], [2, 3.9118475760983674e+69], [2, 4.992640043644563e+307], [2, 6.348727910490511e+307], [2, 2.596095448027321e+294], [2, 8.847840552297933e+237], [2, 9.141952774079136e+233], [2, 1.304311033727945e+59], [2, 6.164836617917708e+244], [2, -3.792262432311615e+188], [2, -5.060148738855514e+92], [2, 4.4046714381308866e+237], [2, 1.2460653793116812e+66], [2, -5.701053198789941e+106], [2, 3.347812904325669e+237], [2, 2.928216283675615e+252], [2, 3.582393652433176e+265], [2, 3.817996352980135e+280], [2, 1.7945106943116528e+245], [2, 1.0635571052966949e+298], [2, 1.1523301640118204e+245], [2, 9.251758492579311e+307], [2, 1.0004769056215218e+198], [2, 2.5585329789703798e+241], [2, 2.851082343029107e+234], [2, np.nan], [2, 4.875144411289744e+266], [2, 8.745416137551392e+261], [2, -6.233036381308568e+39], [2, 1.107638245832097e+213], [2, -9.63017382556966e+81], [2, 7.403799305289067e+298], [2, -3.2886412244912055e+142], [2, 1.960622566503349e+305], [2, -3.2893373654982835e+293], [2, np.nan], [2, -1.599798804914007e+306], [2, -7.29396591563488e+42], [2, 1.4853890549176352e+249], [2, 8.422269434494564e+307], [2, np.nan], [2, 2.551959356946093e+259], [2, np.nan], [2, 1.3994796206011728e+308], [2, -3.253336296230227e+306], [2, 5.231807844833984e+307], [2, 1.455223326789091e+308]]
                    # if "added it!!!" in message:
                    #     lst.append(i)
                    # elif "added it (inf)!!!" in message:
                    #     lstinf.append(i)
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
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)
        cerebro.addstrategy(OpeningRangeBreakout, rsiK=stochRSIk, rsiD=stochRSId, j=i)
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
            data = [[(78, 3, 46), 1.935794646847023e+301], [(195, 89, 18), -1.7541193565950618e+78], [(290, 8, 209), 8.91042898079313e+37], [(114, 3, 58), 2.297374024072508e+252], [(105, 3, 46), -2.161597934857899e+260], [(99, 3, 45), 5.4929405719598e+258], [(290, 3, 214), -3.93386466946166e+61], [(115, 3, 43), -3.4218047023988907e+256], [(92, 3, 45), 4.345319689056776e+272], [(103, 2, 53), 8.346708492041984e+301], [(258, 7, 212), 7.279091483600074e+55], [(41, 3, 114), 1.710450823515068e+297], [(52, 4, 262), 5.180727089070031e+198], [(96, 3, 58), 1.5283951430880767e+245], [(53, 3, 257), 2.6270058134493946e+223], [(84, 4, 43), 3.866964561452851e+265], [(139, 3, 51), 2.089831168507913e+219], [(87, 2, 54), 1.6009171149004943e+298], [(53, 3, 269), 2.3238734290318018e+230], [(60, 2, 66), 4.999449321974848e+307], [(41, 3, 105), 7.66187085656722e+307], [(182, 11, 296), -2.0894925546559653e+39], [(66, 4, 69), -3.188461602739346e+238], [(72, 4, 50), -1.948030109527697e+267], [(223, 8, 266), 2.467211086060584e+55], [(274, 5, 225), 2.2353985156959003e+59], [(245, 9, 194), -8.783476043567202e+46], [(66, 3, 61), -8.643199844091132e+299], [(226, 8, 249), 9.505008987689782e+47], [(135, 2, 297), -2.2007511902060122e+110], [(58, 3, 97), 8.923635897679127e+284], [(98, 3, 51), 3.4599762430002835e+234], [(55, 3, 102), 1.7143914455693136e+287], [(180, 11, 268), -1.0206318665021566e+50], [(204, 13, 231), -6.507008988297594e+43], [(292, 14, 198), 1.062602007846162e+26], [(245, 12, 188), 6.798422617767861e+43], [(169, 2, 39), np.nan], [(101, 3, 36), 2.720657167489855e+291], [(197, 3, 290), 1.1151782714341413e+66], [(133, 3, 29), 1.7397211736075855e+305], [(242, 11, 199), -1.08421978555333e+43], [(70, 5, 43), -2.0248327438354286e+266], [(74, 3, 59), 7.653771740035359e+287], [(197, 12, 234), 4.733306357755209e+41], [(115, 3, 35), 1.78822951889474e+295], [(194, 14, 246), -7.611772856819191e+39], [(52, 3, 205), 7.661722946582369e+251], [(43, 3, 90), 4.066522926496791e+307], [(195, 12, 239), 5.0439205725135055e+41], [(274, 1, 274), -1.1974503336967822e+90], [(42, 3, 96), 7.601962918977266e+307], [(180, 11, 277), -6.078571603397443e+42], [(34, 4, 183), -1.3531271245698496e+301], [(66, 3, 28), 1.5106499119908517e+308], [(84, 3, 28), np.nan], [(148, 3, 36), 1.5345549984311949e+273], [(34, 4, 178), -3.314412004946957e+290], [(274, 1, 266), -1.5239971149649626e+86], [(238, 3, 292), 4.9049906655853505e+91], [(179, 2, 29), np.nan], [(66, 3, 23), np.nan], [(168, 3, 26), np.nan], [(205, 3, 287), 3.9118475760983674e+69], [(141, 2, 29), 4.992640043644563e+307], [(18, 6, 105), 6.348727910490511e+307], [(114, 2, 48), 2.596095448027321e+294], [(98, 3, 57), 8.847840552297933e+237], [(50, 3, 266), 9.141952774079136e+233], [(194, 4, 272), 1.304311033727945e+59], [(50, 3, 253), 6.164836617917708e+244], [(114, 5, 42), -3.792262432311615e+188], [(151, 10, 181), -5.060148738855514e+92], [(115, 3, 61), 4.4046714381308866e+237], [(194, 3, 299), 1.2460653793116812e+66], [(136, 2, 295), -5.701053198789941e+106], [(50, 3, 259), 3.347812904325669e+237], [(153, 3, 40), 2.928216283675615e+252], [(146, 2, 41), 3.582393652433176e+265], [(130, 3, 34), 3.817996352980135e+280], [(131, 4, 42), 1.7945106943116528e+245], [(99, 2, 48), 1.0635571052966949e+298], [(98, 3, 70), 1.1523301640118204e+245], [(163, 2, 30), 9.251758492579311e+307], [(140, 4, 49), 1.0004769056215218e+198], [(98, 3, 65), 2.5585329789703798e+241], [(114, 3, 53), 2.851082343029107e+234], [(84, 3, 43), np.nan], [(98, 3, 42), 4.875144411289744e+266], [(146, 3, 35), 8.745416137551392e+261], [(194, 14, 240), -6.233036381308568e+39], [(130, 4, 47), 1.107638245832097e+213], [(146, 10, 191), -9.63017382556966e+81], [(114, 3, 35), 7.403799305289067e+298], [(148, 2, 178), -3.2886412244912055e+142], [(132, 3, 29), 1.960622566503349e+305], [(163, 13, 8), -3.2893373654982835e+293], [(167, 2, 40), np.nan], [(148, 3, 28), -1.599798804914007e+306], [(179, 11, 275), -7.29396591563488e+42], [(114, 3, 66), 1.4853890549176352e+249], [(138, 2, 31), 8.422269434494564e+307], [(168, 3, 28), np.nan], [(99, 4, 35), 2.551959356946093e+259], [(130, 2, 24), np.nan], [(146, 3, 21), 1.3994796206011728e+308], [(66, 3, 24), -3.253336296230227e+306], [(103, 2, 53), 5.231807844833984e+307], [(154, 3, 28), 1.455223326789091e+308]]              
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
        list = [(84, 3, 28), (84, 3, 43), (130, 2, 24), (66, 3, 28), (146, 3, 21), (163, 2, 30), (138, 2, 31), (41, 3, 105), (42, 3, 96), (18, 6, 105), (114, 3, 26), (60, 2, 66), (141, 2, 29), (43, 3, 90), (132, 3, 29), (133, 3, 29), (103, 2, 53), (78, 3, 46), (114, 3, 35), (87, 2, 54), (99, 2, 48)]
        print(len(list))
        # (84, 3, 28), (179, 2, 29), (66, 3, 23), (168, 3, 26), (84, 3, 43), (168, 3, 28), (130, 2, 24), (66, 3, 28), (154, 3, 28), (146, 3, 21), (163, 2, 30), (138, 2, 31), (41, 3, 105), (42, 3, 96), (18, 6, 105), (114, 3, 26), (60, 2, 66), (141, 2, 29), (43, 3, 90), (132, 3, 29), (133, 3, 29), (103, 2, 53), (78, 3, 46), (114, 3, 35), (87, 2, 54), (99, 2, 48)]
        #[[(169, 2, 39), nan], [(84, 3, 28), nan], [(179, 2, 29), nan], [(66, 3, 23), nan], [(168, 3, 26), nan], [(84, 3, 43), nan], [(168, 3, 28), nan], [(130, 2, 24), nan], [(66, 3, 28), 1.5106499119908517e+308], [(154, 3, 28), 1.455223326789091e+308], [(146, 3, 21), 1.3994796206011728e+308], [(163, 2, 30), 9.251758492579311e+307], [(138, 2, 31), 8.422269434494564e+307], [(41, 3, 105), 7.66187085656722e+307], [(42, 3, 96), 7.601962918977266e+307], [(18, 6, 105), 6.348727910490511e+307], [(114, 3, 26), 5.231807844833984e+307], [(60, 2, 66), 4.999449321974848e+307], [(141, 2, 29), 4.992640043644563e+307], [(43, 3, 90), 4.066522926496791e+307], [(132, 3, 29), 1.960622566503349e+305], [(133, 3, 29), 1.7397211736075855e+305], [(103, 2, 53), 8.346708492041984e+301], [(78, 3, 46), 1.935794646847023e+301], [(114, 3, 35), 7.403799305289067e+298], [(87, 2, 54), 1.6009171149004943e+298], [(99, 2, 48), 1.0635571052966949e+298], [(41, 3, 114), 1.710450823515068e+297], [(115, 3, 35), 1.78822951889474e+295], [(114, 2, 48), 2.596095448027321e+294], [(101, 3, 36), 2.720657167489855e+291], [(74, 3, 59), 7.653771740035359e+287], [(55, 3, 102), 1.7143914455693136e+287], [(58, 3, 97), 8.923635897679127e+284], [(130, 3, 34), 3.817996352980135e+280], [(148, 3, 36), 1.5345549984311949e+273], [(92, 3, 45), 4.345319689056776e+272], [(98, 3, 42), 4.875144411289744e+266], [(84, 4, 43), 3.866964561452851e+265], [(146, 2, 41), 3.582393652433176e+265], [(146, 3, 35), 8.745416137551392e+261], [(99, 4, 35), 2.551959356946093e+259], [(99, 3, 45), 5.4929405719598e+258], [(153, 3, 40), 2.928216283675615e+252], [(114, 3, 58), 2.297374024072508e+252], [(52, 3, 205), 7.661722946582369e+251], [(114, 3, 66), 1.4853890549176352e+249], [(131, 4, 42), 1.7945106943116528e+245], [(96, 3, 58), 1.5283951430880767e+245], [(98, 3, 70), 1.1523301640118204e+245], [(50, 3, 253), 6.164836617917708e+244], [(98, 3, 65), 2.5585329789703798e+241], [(98, 3, 57), 8.847840552297933e+237], [(115, 3, 61), 4.4046714381308866e+237], [(50, 3, 259), 3.347812904325669e+237], [(98, 3, 51), 3.4599762430002835e+234], [(114, 3, 53), 2.851082343029107e+234], [(50, 3, 266), 9.141952774079136e+233]]
        #1.022675520727791772710849448E+309
        
        
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]
#[112, 113, 114]

#1.017822371243422482168647878E+309