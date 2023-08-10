import pyautogui
from datetime import datetime
def automaticBuy(buy):
    pyautogui.click(buy)
def automaticSell(sell):
    pyautogui.click(sell)
def checkTime(lastMin = -1):
    if lastMin == datetime.now().minute:
        return False
    lastMin = datetime.now().minute
    if (datetime.now().second >= 1 and datetime.now().second <= 2):
        return True
    else:
        return False