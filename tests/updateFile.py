

from tests.testGrabData import grabHistoricalData

symbol = "EURUSD"
data = grabHistoricalData(symbol)
f = open('documents/dataSIM.txt', 'w')
f.write(str(data))
