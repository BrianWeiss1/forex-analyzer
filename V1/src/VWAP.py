from ta.volume import VolumeWeightedAveragePrice
def get_VWAP(df, window):
    VWAP_indicator = VolumeWeightedAveragePrice(df['high'], df['low'], df['close'], df['volume'], window)
    df2 = VolumeWeightedAveragePrice.volume_weighted_average_price(VWAP_indicator)
    return df2