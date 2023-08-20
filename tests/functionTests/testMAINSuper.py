from tests.functionTests.testGrabData import grabHistoricalData
from tests.functionTests.testSpecial import formatDataset
from tests.functionTests.testSupertrend import get_supertrend


if '__main__' == __name__:
    symbol = "EURJPY"
    while(True):
        data = grabHistoricalData(symbol)
        data = formatDataset(data)
        st, upt, dt = get_supertrend(data['high'], data['low'], data['close'], 9, 3.9)
        print(st, upt, dt)
