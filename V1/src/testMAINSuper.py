from SpecialFunctions import formatDataset
from testSupertrend import get_supertrend
from testGrabData import grabHistoricalData


if '__main__' == __name__:
    symbol = "EURJPY"
    data = grabHistoricalData(symbol)
    data = formatDataset(data)
    st, upt, dt = get_supertrend(data['high'], data['low'], data['close'], 9, 3.9)
    data['supertrend'] = st
    data['uptrend'] = upt
    data['downtrend'] = dt
    print(data)
