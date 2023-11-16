import sys
import requests
import numpy as np
import random
import pandas as pd
import threading


class IndicatorMixin:
    """Util mixin indicator class"""

    _fillna = False

    def _check_fillna(self, series: pd.Series, value: int = 0) -> pd.Series:
        """Check if fillna flag is True.

        Args:
            series(pandas.Series): calculated indicator series.
            value(int): value to fill gaps; if -1 fill values using 'backfill' mode.

        Returns:
            pandas.Series: New feature generated.
        """
        if self._fillna:
            series_output = series.copy(deep=False)
            series_output = series_output.replace([np.inf, -np.inf], np.nan)
            if isinstance(value, int) and value == -1:
                series = series_output.fillna(method="ffill").fillna(method='bfill')
            else:
                series = series_output.fillna(method="ffill").fillna(value)
        return series

    @staticmethod
    def _true_range(
        high: pd.Series, low: pd.Series, prev_close: pd.Series
    ) -> pd.Series:
        tr1 = high - low
        tr2 = (high - prev_close).abs()
        tr3 = (low - prev_close).abs()
        true_range = pd.DataFrame(data={"tr1": tr1, "tr2": tr2, "tr3": tr3}).max(axis=1)
        return true_range

class RSIIndicator(IndicatorMixin):
    """Relative Strength Index (RSI)

    Compares the magnitude of recent gains and losses over a specified time
    period to measure speed and change of price movements of a security. It is
    primarily used to attempt to identify overbought or oversold conditions in
    the trading of an asset.

    https://www.investopedia.com/terms/r/rsi.asp

    Args:
        close(pandas.Series): dataset 'Close' column.
        window(int): n period.
        fillna(bool): if True, fill nan values.
    """

    def __init__(self, close: pd.Series, window: int = 14, fillna: bool = False):
        self._close = close
        self._window = window
        self._fillna = fillna
        self._run()

    def _run(self):
        diff = self._close.diff(1)
        up_direction = diff.where(diff > 0, 0.0)
        down_direction = -diff.where(diff < 0, 0.0)
        min_periods = 0 if self._fillna else self._window
        emaup = up_direction.ewm(
            alpha=1 / self._window, min_periods=min_periods, adjust=False
        ).mean()
        emadn = down_direction.ewm(
            alpha=1 / self._window, min_periods=min_periods, adjust=False
        ).mean()
        relative_strength = emaup / emadn
        self._rsi = pd.Series(
            np.where(emadn == 0, 100, 100 - (100 / (1 + relative_strength))),
            index=self._close.index,
        )

    def rsi(self) -> pd.Series:
        """Relative Strength Index (RSI)

        Returns:
            pandas.Series: New feature generated.
        """
        rsi_series = self._check_fillna(self._rsi, value=50)
        return pd.Series(rsi_series, name="rsi")

class StochRSIIndicator(IndicatorMixin):
    """Stochastic RSI

    The StochRSI oscillator was developed to take advantage of both momentum
    indicators in order to create a more sensitive indicator that is attuned to
    a specific security's historical performance rather than a generalized analysis
    of price change.

    https://school.stockcharts.com/doku.php?id=technical_indicators:stochrsi
    https://www.investopedia.com/terms/s/stochrsi.asp

    Args:
        close(pandas.Series): dataset 'Close' column.
        window(int): n period
        smooth1(int): moving average of Stochastic RSI
        smooth2(int): moving average of %K
        fillna(bool): if True, fill nan values.
    """

    def __init__(
        self,
        close: pd.Series,
        window: int = 14,
        smooth1: int = 3,
        smooth2: int = 3,
        fillna: bool = False,
    ):
        self._close = close
        self._window = window
        self._smooth1 = smooth1
        self._smooth2 = smooth2
        self._fillna = fillna
        self._run()

    def _run(self):
        self._rsi = RSIIndicator(
            close=self._close, window=self._window, fillna=self._fillna
        ).rsi()
        lowest_low_rsi = self._rsi.rolling(self._window).min()
        self._stochrsi = (self._rsi - lowest_low_rsi) / (
            self._rsi.rolling(self._window).max() - lowest_low_rsi
        )
        self._stochrsi_k = self._stochrsi.rolling(self._smooth1).mean()

    def stochrsi(self):
        """Stochastic RSI

        Returns:
            pandas.Series: New feature generated.
        """
        stochrsi_series = self._check_fillna(self._stochrsi)
        return pd.Series(stochrsi_series, name="stochrsi")

    def stochrsi_k(self):
        """Stochastic RSI %k

        Returns:
            pandas.Series: New feature generated.
        """
        stochrsi_k_series = self._check_fillna(self._stochrsi_k)
        return pd.Series(stochrsi_k_series, name="stochrsi_k")

    def stochrsi_d(self):
        """Stochastic RSI %d

        Returns:
            pandas.Series: New feature generated.
        """
        stochrsi_d_series = self._stochrsi_k.rolling(self._smooth2).mean()
        stochrsi_d_series = self._check_fillna(stochrsi_d_series)
        return pd.Series(stochrsi_d_series, name="stochrsi_d")

def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()

def formatDataset2(df: pd.DataFrame):
    columns_to_convert = ['open', 'high', 'low', 'close']
    for column in columns_to_convert:
        df[column] = df[column].astype(float)
    return df
def formatDataset3(data: list):
    df = pd.DataFrame(data)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index('datetime')
    return df

def findPos(data, pastI, currentI, BuyOrSell, pos, nuet, neg, posPips, negPips):
    if BuyOrSell:
        if data[currentI] > data[pastI[0]]:
            # if close is higher than past close, it's a profitable buy
            pos += 1
            currentPipChange = abs((data[currentI]*100)-(100*data[pastI[0]]))
            currentPrice = data[currentI]
            percentChange = currentPipChange/currentPrice
            changeDecimal = percentChange/100
            posPips += currentPipChange
        elif data[currentI] == data[pastI[0]]:

            nuet += 1
        else:
            # if close isn't higher than past close, and it isn't equal, it's a unprofitable buy
            neg += 1
            currentPipChange = abs((100*data[pastI[0]])-(data[currentI]*100))
            currentPrice = data[currentI]
            percentChange = currentPipChange/currentPrice
            changeDecimal = -percentChange/100  
            negPips -= currentPipChange
    if not BuyOrSell:
        # If not buy, it must be a sell
        if data[currentI] < data[pastI[0]]:
            # if close is lower than past close, it's a profitable sell
            pos += 1
            currentPipChange = abs((data[currentI]*100)-(100*data[pastI[0]]))
            currentPrice = data[currentI]
            percentChange = currentPipChange/currentPrice
            changeDecimal = percentChange/100
            
            posPips += currentPipChange
        elif data[currentI] == data[pastI[0]]:
            nuet += 1
        else:
            # if close isn't lower than past close, and it isn't equal, it's a unprofitable sell
            neg += 1
            currentPipChange = abs((100*data[pastI[0]])-(data[currentI]*100))
            currentPrice = data[currentI]
            percentChange = currentPipChange/currentPrice
            changeDecimal = -percentChange/100    
            negPips -= currentPipChange

        pastI = []
    return pos, nuet, neg, posPips, negPips

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
        shortI['shortSignal'] = True
        shortI['entry'] = [i]
    elif previousBuy and longI['buySignal']:
        longI['entry'].append(i)
    elif previousSell and shortI['shortSignal']:
        shortI['entry'].append(i)
    elif previousBuy:
        shortI['shortSignal'] = False
        longI['buySignal'] = True
        longI['entry'] = [i]
    elif previousSell:
        longI['buySignal'] = False
        shortI['shortSignal'] = True
        shortI['entry'] = [i]
    return longI, shortI

def checkLuquidation(shortI, longI, data, i, pos, nuet, neg, posPips, negPips):
    if shortI['luquidate']:
        BuyOrSell = False
        pos, nuet, neg, posPips, negPips = findPos(data, longI['entry'], i, BuyOrSell, pos, nuet, neg, posPips, negPips) # Logic to close short position
        longI['entry'] = []
        shortI['luquidate'] = False
    if longI['luquidate']:
        BuyOrSell = True
        pos, nuet, neg, posPips, negPips = findPos(data, shortI['entry'], i, BuyOrSell, pos, nuet, neg, posPips, negPips) # Logic to close long position
        shortI['entry'] = []
        longI['luquidate'] = False
    return shortI, longI, pos, nuet, neg, posPips, negPips
    

api_key = "d6e8542914aa439e92fceaccca1c2708"
api_key2= "0d27bad2c7854a18bc4cafcb5d7f3583"

def grabForex(values):
    base_url = "https://api.twelvedata.com/time_series"
    '''
    GBPUSD=X/GBP/USD
    AUDUSD=X/AUD/USD
    NZDUSD=X/NZD/USD
    EURJPY=X/EUR/JPY
    GBPJPY=X/GBP/JPY
    EURGBP=X/EUR/GBP
    EURCAD=X/EUR/CAD
    EURSEK=X/EUR/SEK
    EURCHF=X/EUR/CHF
    EURHUF=X/EUR/HUF
    EURJPY=X/EUR/JPY
    CNY=X/USD/CNY
    HKD=X/USD/HKD
    SGD=X/USD/SGD
    INR=X/USD/INR
    MXN=X/USD/MXN
    PHP=X/USD/PHP
    IDR=X/USD/IDR
    THB=X/USD/THB
    MYR=X/USD/MYR
    ZAR=X/USD/ZAR
    RUB=X/USD/RUB
    '''
    params = {
        "symbol": "USD/NZD", #USD/NZD 0.003, NZD/USD 0.002
        "interval": "30min",
        "outputsize": values,
        "apikey": api_key2
        
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    ForexData = open('documents/forexData.txt', 'w')
    ForexData.write(str(data['values']))
    ForexData.close()
    return data['values']

def simulateCrypto(df: pd.DataFrame, amountTo: int, a: bool, b: bool, c: bool, aVal: int, bVal: int, cVal: int, incerment: int):
    printing = False
    printingSpecific = True
    df = df.dropna()
    bestSpecialValue = -sys.maxsize
    worstSpecialValue = sys.maxsize
    j = -1
    k = -1
    pos = 0
    nuet = 0
    neg = 0
    BestSpecialValues = (0, 0)
    WorstSpecialValues = (0, 0)
    oldj = -1
    posPips = 0
    negPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
    shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False
    SpecialValue = 0
    try:
        for j in range(2, amountTo, incerment):
            if printingSpecific: 
                if j != oldj:
                    oldj = j
            if a:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, bVal, cVal) 
            elif b:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, j, cVal) 
            elif c:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, bVal, j) 
            else:
                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, 100, 680)
            stochRSIK1 = np.array(stochRSIK1)                
            stochRSID1 = np.array(stochRSID1)
            closeData = np.array(df['close'])
            for i in range(len(df)):
                
                nowPrice += closeData[i]
                nowCount += 1
                
                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, posPips, negPips = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, closeData, i, pos, nuet, neg, posPips, negPips)
    
                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] > stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] < stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True                
                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                #--------STOCH1RSI----------#  
                
            try:
                percentOfTrades = round(((pos + nuet + neg) / len(df)) * 100, 2)
                AvgPrice = nowPrice / nowCount

                negPip = np.where(neg != 0, negPips / neg, 0)

                posPercent = round((posPips / pos / AvgPrice), 5)
                negPercent = round((negPip / AvgPrice), 5)

                difference = (posPercent + negPercent)
                correctness = round((pos / (neg + pos)), 2)
                accuracy = correctness - 0.5
                tradeDecimal = percentOfTrades / 100
            except ZeroDivisionError:
                if printing:
                    print("ERROR GO BRRRR")
            pos = nuet = neg = 0
            try: 
                SpecialValue = difference * accuracy * tradeDecimal
                if SpecialValue > bestSpecialValue:
                    bestSpecialValue = SpecialValue
                    BestSpecialValues = (j, k)
                if SpecialValue < worstSpecialValue:
                    worstSpecialValue = SpecialValue
                    WorstSpecialValues = (j, k)
            except:
                if printing:
                    print("ERROR")
            negPips = 0
            posPips = 0
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues
    except KeyboardInterrupt:
        return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues



def main(df):
    a = b = c = False
    aVal = bVal = cVal = 50
    i = 50
    stochValues = []
    lastBestVal = -1
    amountTo = 1400
    countRep = 0
    while(True):
        a = b = c = False
        abOrC = random.randint(0, 2)
        if abOrC == 0:
            a = True  
        if abOrC == 1:
            b = True
        if abOrC == 2:
            c = True 
        aVal = random.randint(1, 1000) 
        bVal = random.randint(1, 1000) 
        cVal = random.randint(1, 1000) 
        amountTo = 1400
        repeatA = False
        repeatB = False
        repeatC = False
        onceA = onceB = onceC = False
        while True:
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 5)
            randomNum = random.randint(0, 1)
            if abs(bestSpecialValue) > abs(worstSpecialValue):
                bestVal = BestSpecialValues[0]
                bestPer = bestSpecialValue
            else:
                bestVal = WorstSpecialValues[0]
                bestPer = worstSpecialValue
            if a:
                onceA = True
                a = False
                if round(aVal, 5) == round(bestVal, 5):
                    repeatA = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                if bestVal != 0:
                    aVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatB):
                    b = True
                elif (randomNum == 0 or repeatB) and (not repeatC):
                    c = True
            elif b:
                onceB = True
                if round(bVal, 5) == round(bestVal, 5):
                    repeatB = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                b = False
                if bestVal != 0:
                    bVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatC):
                    c = True
            elif c:
                onceC = True
                if round(cVal, 5) == round(bestVal, 5):
                    repeatC = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                c = False
                if bestVal != 0:
                    cVal = bestVal
                if (randomNum == 1 or repeatB) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatB):
                    b = True
            else:
                print("ERROR: No value for a b c")
            
            if repeatA and repeatB and repeatC:
                break
            if onceC and onceB and onceA:
                amountTo = int(max(aVal, bVal, cVal)*2)
            lastBestVal = bestVal
        repeatA = repeatB = repeatC = False
        a = b = c = False
        abOrC = random.randint(0, 2)
        if abOrC == 0:
            a = True  
        if abOrC == 1:
            b = True
        if abOrC == 2:
            c = True 
        onceA = onceB = onceC = False
        while True:
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 1)
            randomNum = random.randint(0, 1)
            if abs(bestSpecialValue) > abs(worstSpecialValue):
                bestVal = BestSpecialValues[0]
                bestPer = bestSpecialValue
            else:
                bestVal = WorstSpecialValues[0]
                bestPer = worstSpecialValue
            if a:
                onceA = True
                a = False
                if round(aVal, 5) == round(bestVal, 5):
                    repeatA = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                if bestVal != 0:
                    aVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatB):
                    b = True
                elif (randomNum == 0 or repeatB) and (not repeatC):
                    c = True
            elif b:
                onceB = True
                if round(bVal, 5) == round(bestVal, 5):
                    repeatB = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                b = False
                if bestVal != 0:
                    bVal = bestVal
                if (randomNum == 1 or repeatC) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatC):
                    c = True
            elif c:
                onceC = True
                if round(cVal, 5) == round(bestVal, 5):
                    repeatC = True
                else:
                    repeatA = False
                    repeatB = False
                    repeatC = False
                c = False
                if bestVal != 0:
                    cVal = bestVal
                if (randomNum == 1 or repeatB) and (not repeatA):
                    a = True
                elif (randomNum == 0 or repeatA) and (not repeatB):
                    b = True
            else:
                print("ERROR: No value for a b c")
            
            if repeatA and repeatB and repeatC:
                # print(f"get_StochasticRelitiveStrengthIndex(df, {aVal}, {bVal}, {cVal})")
                stochValues.append([bestPer, (aVal, bVal, cVal)])
                break
            if onceC and onceB and onceA:
                amountTo = int(max(aVal, bVal, cVal)*2)
            lastBestVal = bestVal
        # print(stochValues)
        if len(stochValues) == 150:
            return stochValues
if __name__ == '__main__':
    def run_main(i, df):
        result_array = main(df)
        print(f"Thread {i}: Result Array: {result_array}")

    df = formatDataset2(formatDataset3(grabForex(5000))) # obtains a pandas dataframe
    # Create and start 20 threads with unique IDs
    threads = []
    for i in range(20):
        thread = threading.Thread(target=run_main, args=(i,df))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
