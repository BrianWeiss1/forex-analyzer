
from src.testGrabData import calltimes, calltimes5m, grabHistoricalData, grabHistoricalDataBTC

symbol = "BTCUSD"
# data = grabHistoricalDataBTC(symbol)
# print(data)
# f = open('documents/dataCrypto.txt', 'w')
# f.write(str(data))



calltimes("BTCUSD", 3, "2022-06-27 9:45")
# calltimes5m("BTCUSD", 3, "2022-07-30 9:45")