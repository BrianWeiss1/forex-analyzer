import datetime
import time
import pyautogui
from src.testGrabData import grabHistoricalDataBTC
# time.sleep(3)
# print(pyautogui.position()) 
# Point(1414, 946) --> buy
# Point(1268, 938) --> sell

#Martet()
#(1299, 277)
def market():
    pyautogui.click((1299, 277))
def limit():
    pyautogui.click((1379, 285))
#Limit/Stop()
#(1379, 285)

