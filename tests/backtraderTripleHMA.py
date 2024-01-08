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
from ta.volume import MFIIndicator
import matplotlib as plt


def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
def get_MFI(data, window):
    MFIind = MFIIndicator(data['high'], data['low'], data['close'], data['volume'], window)
    return MFIind.money_flow_index()
def findMFI(value):
    if value > 55:
        return "BULLISH"
    elif value < 45:
        return 'BEARISH'
    else:
        return 'SIDEWAYS'
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
def get_HMA(df: pd.DataFrame, period_1: int, period_2: int, period_3: int) -> tuple:
    hma_1 = ta.hma(df["close"], period_1)
    hma_2 = ta.hma(df["close"], period_2)
    hma_3 = ta.hma(df["close"], period_3)
    return hma_1, hma_2, hma_3