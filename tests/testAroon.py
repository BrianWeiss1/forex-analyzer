from ta.trend import AroonIndicator
def aroon(df, length=14):
    dfd = df.copy()
    aroon_indic = AroonIndicator(df['close'], 14)
    dfd['aroon_down'] = AroonIndicator.aroon_down(aroon_indic) 
    dfd['aroon_up'] = AroonIndicator.aroon_up(aroon_indic)
    dfd['aroon_indicator'] = AroonIndicator.aroon_indicator(aroon_indic)
    return dfd