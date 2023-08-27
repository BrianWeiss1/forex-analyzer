
from src.testGrabData import calltimes, grabHistoricalData, grabHistoricalDataBTC

symbol = "BTCUSD"
# data = grabHistoricalDataBTC(symbol)
# print(data)
# f = open('documents/dataCrypto.txt', 'w')
# f.write(str(data))



calltimes("BTCUSD", 10, "2022-07-30 9:45")