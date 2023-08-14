import pyautogui
from datetime import datetime
import time
def findLocation(wait):
    time.sleep(wait)
    print(pyautogui.position())
def automaticBuy(buy=(1118, 387)):
    pyautogui.click(buy)
def automaticSell(sell=(1123, 462)):
    pyautogui.click(sell)
def checkTime(lastMin = -1):
    if lastMin == datetime.now().minute:
        return False, lastMin
    lastMin = datetime.now().minute
    if (datetime.now().second >= 1 and datetime.now().second <= 2):
        return True, lastMin
    else:
        return False, lastMin
# def openVPN(VPNopen=()):
