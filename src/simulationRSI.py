

from functions.GrabData import GrabCloseData
from functions.RSI import RSI

symbol = "AAPL"
def calculate_supremeRSIaverage(RSIvalues, dataPoints, time):
    print(len(RSIvalues))
    print(len(dataPoints))
    print(len(time))
    for i in range(len(list(RSIvalues))-1, 0, -1):
        # go through time: if 
        # RSIvalues[time[i]]
        RSIvalues[time[i]]
closeData, time2 = GrabCloseData(symbol)
current = {}
checkNextCandle = 0
RSIvalues = RSI(symbol)
# while True:
#     current = checkPusdo(current, RSIvalue) # check 1 data
#     signal = obtainResult(checkNextCandle, RSIvalue) # check 1 data
#     if signal == "BUY":
#         automaticBuy()
#     if signal == "SELL":
#         automaticSell()
#     checkNextCandle = findCandleNumber(current, number)
#     break

calculate_supremeRSIaverage(RSIvalues, closeData, time2)
