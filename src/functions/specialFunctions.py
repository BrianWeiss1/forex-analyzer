import pyautogui
from datetime import datetime, timedelta
import time
def findLocation(wait):
    time.sleep(wait)
    print(pyautogui.position())
def automaticBuy(buy=(1118, 387)):
    pyautogui.click(buy)
def automaticReset(automaticReset=(1459, 494)):
    pyautogui.click(automaticReset)
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
def obtainCurrentTime(minute):
    current_time = datetime.now()
    previous_minute = current_time - timedelta(minutes=minute)
    formatted_time = previous_minute.strftime('%Y-%m-%d %H:%M')
    return formatted_time
def obtainPastTimeFormatted(minute):
    current_time = datetime.now()
    previous_minute = current_time - timedelta(minutes=minute)
    formatted_time = previous_minute.strftime('%Y-%m-%d %H:%M')
    return (str(formatted_time) + ':00')
# def obtainCurrentTimeFormatted():


# def openVPN(VPNopen=()):
