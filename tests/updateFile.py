

from tests.testGrabData import grabHistoricalData

symbol = "EURJPY"
data = grabHistoricalData(symbol)
f = open('documents/dataSIM.txt', 'w')
f.write(str(data))
