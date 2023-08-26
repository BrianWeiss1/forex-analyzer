

from src.testGrabData import grabHistoricalData

symbol = "EURJPY"
data = grabHistoricalData(symbol)
f = open('documents/data.txt', 'w')
f.write(str(data))
