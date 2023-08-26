from ta.momentum import StochRSIIndicator
def get_STOCHRSI(data, window, smooth1, smooth2):
    stochRSI_ind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSI_ind.stochrsi()