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
def obtainResult(i, st, st2, st3, st4, st5, st6, st7, data, dataRSI, rsiValue):
    contempent = False
    prevBuyRSI = False
    prevSellRSI = False
    prevSellSTOCH = None
    prevBuySTOCH = None
    prevSellRSI = False
    prevBuyRSI = False
    contempent = False
    prevSellSTOCH = None
    prevBuySTOCH = None
    previousSell = previousBuy = False


    def SuperTrendEMA():
        stbuy = None
        stbuy1 = None
        stbuy2 = None
        stbuy3 = None
        stbuy4 = None
        stbuy5 = None
        stbuy6 = None
        stbuy7 = None
        prevBuy = prevSell = False
        signalSuper = ""
        if st[i] > data["close"][i]:
            stbuy = True
        elif st[i] < data["close"][i]:
            stbuy = False

        if st2[i] > data["close"][i]:
            stbuy2 = True
        elif st2[i] < data["close"][i]:
            stbuy2 = False
        if st3[i] > data["close"][i]:
            stbuy3 = True
        elif st3[i] < data["close"][i]:
            stbuy3 = False
        if st4[i] > data["close"][i]:
            stbuy4 = True
        elif st4[i] < data["close"][i]:
            stbuy4 = False
        if st5[i] > data["close"][i]:
            stbuy5 = True
        elif st5[i] < data["close"][i]:
            stbuy5 = False
        if st6[i] > data["close"][i]:
            stbuy6 = True
        elif st6[i] < data["close"][i]:
            stbuy6 = False
        if st7[i] > data["close"][i]:
            stbuy7 = True
        elif st7[i] < data["close"][i]:
            stbuy7 = False

        if (
            stbuy == True
            and stbuy2 == True
            and stbuy3 == True
            and stbuy4 == True
            and stbuy5 == True
            and stbuy6 == True
            and stbuy7 == True
        ):
            signalSuper = "BUY"
        if (
            stbuy == False
            and stbuy2 == False
            and stbuy3 == False
            and stbuy4 == False
            and stbuy5 == False
            and stbuy6 == False
            and stbuy7 == False
        ):
            signalSuper = "SELL"

        if signalSuper == "BUY":
            prevBuy = True

        if signalSuper == "SELL":
            prevSell = True

        return prevBuy, prevSell

    prevBuy, prevSell = SuperTrendEMA()
    if prevBuy == True:
        previousBuy = True
    if prevSell == True:
        previousSell = True

    if prevSell:
        if dataRSI[f"rsi_{rsiValue}"][i] > 57 and data["STOCHk_5_3_3"][i] > 27: # 57, 27
            prevSellSTOCH = False
        else:
            prevSellSTOCH = True
    # -----RSI--------#
    change = f"14.27"
    changeNeg = f"-14.27"
    change = float(change)
    changeNeg = float(changeNeg)

    if prevBuy:
        if (
            dataRSI[f"rsi_{rsiValue}"][i] < 55 + changeNeg
            or dataRSI[f"rsi_{rsiValue}"][i] > 45 + change
        ):  # 45, 100
            # previousBuy = False
            prevBuyRSI = False
            # continue
        else:
            # previousBuy = True
            prevBuyRSI = True
    if prevSell:
        if (
            dataRSI[f"rsi_{rsiValue}"][i] < 55 + changeNeg
            or dataRSI[f"rsi_{rsiValue}"][i] > 45 + change
        ):  # 47
            # previousSell = False
            prevSellRSI = False
            # continue
        else:
            # previousSell = True
            prevSellRSI = True


    if prevBuyRSI and prevSellRSI:
        prevSell = False
        prevBuy = False
    if prevBuyRSI:
        previousBuy = True
    else:
        previousBuy = False
    
    if prevSellRSI:
        previousSell = True
    else:
        previousSell = False
    
    if previousSell == True and previousBuy == True:
        previousBuy = False
        previousSell = False
        contempent = True

    #------Working code-------#

    if not contempent:
        if prevBuySTOCH and prevSellSTOCH:
            prevBuySTOCH = False
            prevSellSTOCH = False
        if prevBuySTOCH:
            previousBuy = True
        if prevSellSTOCH:
            previousSell = True

    #contentment
    if previousSell == True and previousBuy == True:
        previousBuy = False
        previousSell = False
        contempent = True
    return previousBuy, previousSell