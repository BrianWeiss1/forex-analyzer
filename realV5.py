from datetime import datetime
import telebot
import time
from SpecialFunctions import formatDataset
from V3.testGrabData import getYahoo, calltimes15m, calltimes30FIXED
from src.functions import get_StochasticRelitiveStrengthIndex, get_StochasticOscilator
from src.longTermPos import findSelection, checkLuquidationV1
from src.underliningProcesses import swap
from src.sendTelegramMessage import send_message
# import pandas_datareader
import pandas
import time
from src.createPosition import buyLong, buyShort, closeLong, closeShort
# pip install python-bingx
from bingX.perpetual.v2 import PerpetualV2
from bingX.perpetual.v2.types import (
    ForceOrder,
    HistoryOrder,
    MarginType,
    Order,
    PositionSide,
    Side,
)
import numpy as np
# createPosition(bingx_client, symbol, betAmount, maxLev)


APIURL = "https://open-api.bingx.com"
f = open('documents/api_key.txt', 'r')
APIKEY = 'zGnYUEbpDvOI36v9DnPIvMLQEVz44Vgme7AUAyFeonkUAusiLDi9PFM65nyjAuijESmpmC2eGAuqmFfHVQ'
SECRETKEY = f.readline()
f.close()
sim = "BTC"
maxLev = 53
totalValueOfAccount = 3
betAmount = totalValueOfAccount/10
symbol = f'{sim}-USDT'
symbolVolume = f'{sim}USDT'

BOT_TOKEN = '6913673966:AAGVUweik0EpNrPxUgFVA35Ve0Dyayo5waw'

bingx_client = PerpetualV2(api_key=APIKEY, secret_key=SECRETKEY)



bot = telebot.TeleBot(BOT_TOKEN)    

firstPurchace = True

previousMinute = -1
stopLoss = 0.5

yes = False
opp = False

while True:
    count = 0
    yes = False
    if ((datetime.now().minute == 47 or datetime.now().minute == 0) and previousMinute != datetime.now().minute):
        yes = True
        while (yes and count < 5):
            count += 1
            try:
                previousMinute = datetime.now().minute
                data = calltimes30FIXED(symbolVolume)
                opp = True

                df = formatDataset(data)
                columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
                for column in columns_to_convert:
                    df[column] = df[column].astype(float)
                i = len(df)-1 

                rsiK, rsiD = get_StochasticRelitiveStrengthIndex(df, 73, 1, 21)

                #--------STOCH1RSI----------#
                if rsiK[i-1] < rsiD[i-1] and rsiK[i] > (rsiD[i]*1.4067):
                    shortCount = 1
                else:
                    shortCount = 0
                if rsiK[i-1] > rsiD[i-1] and (rsiK[i]*1.4023) < rsiD[i]:
                    longCount = 1
                else:
                    longCount = 0
            
                if longCount == 1:
                    send_message("BUY: 1", bot)
                    if not firstPurchace:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            send_message("No position to close RQTRQT", bot)
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        firstPurchace = True

                elif shortCount == 1:
                    send_message("SELL: 1", bot)
                    if not firstPurchace:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            send_message("No position to close RQTRQT", bot)       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        firstPurchace = False
                #--------STOCH1RSI----------#

                yes = False
                break
            except Exception as e:
                yes = True
                send_message(str(e), bot)
    else:
        # print('L BOZO')
        time.sleep(59)
