
from src.testGrabData import grabHistoricalData, grabHistoricalDataBTC

symbol = "BTCUSD"
data = grabHistoricalDataBTC(symbol)
print(data)
f = open('documents/dataCrypto.txt', 'w')
f.write(str(data))
