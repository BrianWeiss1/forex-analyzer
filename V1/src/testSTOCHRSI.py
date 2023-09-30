from ta.momentum import StochRSIIndicator
def get_STOCHRSI(data, window=14, smooth1=3, smooth2=3):
    stochRSI_ind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSI_ind.stochrsi_k(), stochRSI_ind.stochrsi_d()

# if its changed 