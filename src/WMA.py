from ta.trend import WMAIndicator
def get_WMA(data, window):
    indc = WMAIndicator(data['close'], window)
    return WMAIndicator.wma(indc)