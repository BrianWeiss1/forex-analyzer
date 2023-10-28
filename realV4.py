from datetime import datetime
import telebot
import time
from SpecialFunctions import formatDataset
from V3.testGrabData import getYahoo, calltimes15m, calltimes30FIXED
from src.functions import get_StochasticRelitiveStrengthIndex, get_StochasticOscilator
from src.longTermPos import checkLuquidation, findSelection
from src.underliningProcesses import swap
from src.sendTelegramMessage import send_message
import pandas_datareader
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
# createPosition(bingx_client, symbol, betAmount, maxLev)


APIURL = "https://open-api.bingx.com"
f = open('documents/api_key.txt', 'r')
APIKEY = 'zGnYUEbpDvOI36v9DnPIvMLQEVz44Vgme7AUAyFeonkUAusiLDi9PFM65nyjAuijESmpmC2eGAuqmFfHVQ'
SECRETKEY = f.readline()
f.close()
sim = "GFT"
maxLev = 10
betAmount = 0.23
symbol = f'{sim}-USDT'
symbolVolume = f'{sim}USDT'

BOT_TOKEN = '6715543523:AAEq-eAYesOweL3N_nMGyFr1nmMmvtspkU8'

bingx_client = PerpetualV2(api_key=APIKEY, secret_key=SECRETKEY)



bot = telebot.TeleBot(BOT_TOKEN)    

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0

longRunSTOCHRSI1 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI1 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False


longRunSTOCHRSI2 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI2 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI2, previousSellStochasticRSI2 = False, False

longRunSTOCHRSI3 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI3 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI3, previousSellStochasticRSI3 = False, False

longRunSTOCHRSI4 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI4 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI4, previousSellStochasticRSI4 = False, False


longRunSTOCHRSI5 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI5 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI5, previousSellStochasticRSI5 = False, False

longRunSTOCHRSI6 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI6 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI6, previousSellStochasticRSI6 = False, False

longRunSTOCHRSI7 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI7 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI7, previousSellStochasticRSI7 = False, False

longRunSTOCHRSI8 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI8 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI8, previousSellStochasticRSI8 = False, False

longRunSTOCHRSI9 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI9 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI9, previousSellStochasticRSI9 = False, False

longRunSTOCHRSI10 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI10 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI10, previousSellStochasticRSI10 = False, False

longRunSTOCHRSI11 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI11 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI11, previousSellStochasticRSI11 = False, False

longRunSTOCHRSI12 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI12 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI12, previousSellStochasticRSI12 = False, False

longRunSTOCHRSI13 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI13 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI13, previousSellStochasticRSI13 = False, False

longRunSTOCHRSI14 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI14 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI14, previousSellStochasticRSI14 = False, False

longRunSTOCHRSI15 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI15 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI15, previousSellStochasticRSI15 = False, False

longRunSTOCHRSI16 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI16 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI16, previousSellStochasticRSI16 = False, False

longRunSTOCHRSI17 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI17 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI17, previousSellStochasticRSI17 = False, False

longRunSTOCHRSI18 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI18 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI18, previousSellStochasticRSI18 = False, False

longRunSTOCHRSI19 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI19 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI19, previousSellStochasticRSI19 = False, False

longRunSTOCHRSI20 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI20 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI20, previousSellStochasticRSI20 = False, False

longRunSTOCHRSI21 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI21 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI21, previousSellStochasticRSI21 = False, False

longRunSTOCHRSI22 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI22 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI22, previousSellStochasticRSI22 = False, False

longRunSTOCHRSI23 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI23 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI23, previousSellStochasticRSI23 = False, False

longRunSTOCHRSI24 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI24 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI24, previousSellStochasticRSI24 = False, False

longRunSTOCHRSI25 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI25 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI25, previousSellStochasticRSI25 = False, False

longRunSTOCHRSI26 = {"buySignal": False, 'luquidate': False, 'entry': []}    
shortRunSTOCHRSI26 = {'shortSignal': False, 'luquidate': False, 'entry': []}
previousBuyStochasticRSI26, previousSellStochasticRSI26 = False, False

previousMinute = -1
stopLoss = 0.25

pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg, nowPrice, nowCount = 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0

yes = False
opp = False

while True:
    count = 0
    yes = False
    if ((datetime.now().minute == 30 or datetime.now().minute == 0) and previousMinute != datetime.now().minute):
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
                i = len(df)-1 # rlly weird...

                stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, 223, 418, 132)
                stochRSIK2, stochRSID2 = get_StochasticRelitiveStrengthIndex(df, 250, 418, 132)
                stochRSIK3, stochRSID3 = get_StochasticRelitiveStrengthIndex(df, 66, 70, 131)
                stochRSIK4, stochRSID4 = get_StochasticRelitiveStrengthIndex(df, 535, 127, 137) # --> 30000
                stochRSIK5, stochRSID5 = get_StochasticRelitiveStrengthIndex(df, 214, 47, 39)
                stochRSIK6, stochRSID6 = get_StochasticRelitiveStrengthIndex(df, 180, 33, 132)
                stochRSIK7, stochRSID7 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 80)
                stochRSIK8, stochRSID8 = get_StochasticRelitiveStrengthIndex(df, 69, 148, 59)
                stochRSIK9, stochRSID9 = get_StochasticRelitiveStrengthIndex(df, 154, 120, 586)
                stochRSIK10, stochRSID10 = get_StochasticRelitiveStrengthIndex(df, 96, 64, 110)
                stochRSIK11, stochRSID11 = get_StochasticRelitiveStrengthIndex(df, 145, 145, 39)
                stochRSIK12, stochRSID12 = get_StochasticRelitiveStrengthIndex(df, 153, 53, 56)
                stochRSIK13, stochRSID13 = get_StochasticRelitiveStrengthIndex(df, 77, 60, 136)
                stochRSIK14, stochRSID14 = get_StochasticRelitiveStrengthIndex(df, 51, 59, 156) 
                stochRSIK15, stochRSID15 = get_StochasticRelitiveStrengthIndex(df, 184, 62, 62) # 0%
                stochRSIK16, stochRSID16 = get_StochasticRelitiveStrengthIndex(df, 143, 143, 62)
                stochRSIK17, stochRSID17 = get_StochasticRelitiveStrengthIndex(df, 143, 424, 424) # 1%
                stochRSIK18, stochRSID18 = get_StochasticRelitiveStrengthIndex(df, 143, 49, 210) 
                stochRSIK19, stochRSID19 = get_StochasticRelitiveStrengthIndex(df, 53, 52, 194)
                stochRSIK20, stochRSID20 = get_StochasticRelitiveStrengthIndex(df, 53, 53, 199) # 0.8
                stochRSIK21, stochRSID21 = get_StochasticRelitiveStrengthIndex(df, 171, 57, 150) # 0.7
                stochRSIK22, stochRSID22 = get_StochasticRelitiveStrengthIndex(df, 65, 150, 65)
                stochRSIK23, stochRSID23 = get_StochasticRelitiveStrengthIndex(df, 134, 47, 238) # 1.09
                stochRSIK24, stochRSID24 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 137)
                stochRSIK25, stochRSID25 = get_StochasticRelitiveStrengthIndex(df, 401, 127, 153)
                stochRSIK26, stochRSID26 = get_StochasticRelitiveStrengthIndex(df, 293, 83, 316)
                    
                #--------STOCH1RSI----------#
                longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i) 
                shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI1 = previousBuyStochasticRSI1 = False

                if stochRSIK1[i-1] >= stochRSID1[i-1] and stochRSIK1[i] < stochRSID1[i]:
                    previousSellStochasticRSI1 = True
                if stochRSIK1[i-1] <= stochRSID1[i-1] and stochRSIK1[i] > stochRSID1[i]:
                    previousBuyStochasticRSI1 = True
                # previousSellStochasticRSI1, previousBuyStochasticRSI1 = previousBuyStochasticRSI1, previousSellStochasticRSI1)

                if previousSellStochasticRSI1 and previousBuyStochasticRSI1:
                    previousBuyStochasticRSI1 = False
                    previousSellStochasticRSI1 = False   
                if previousSellStochasticRSI1 == True:
                    print("SELL: 1")
                    send_message("SELL: 1", bot)
                                      
                    if count1 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count1+=1
                
                if previousBuyStochasticRSI1 == True:
                    print("BUY: 1")
                    send_message("BUY: 1", bot)
                                         
                    if count1 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count1+=1
                #--------STOCH1RSI----------#


                #--------STOCH2RSI----------#
                longRunSTOCHRSI2, shortRunSTOCHRSI2 = findSelection(previousBuyStochasticRSI2, previousSellStochasticRSI2, longRunSTOCHRSI2, shortRunSTOCHRSI2, i) 
                shortRunSTOCHRSI2, longRunSTOCHRSI2, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI2, longRunSTOCHRSI2, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI2 = previousBuyStochasticRSI2 = False

                if stochRSIK2[i-1] >= stochRSID2[i-1] and stochRSIK2[i] < stochRSID2[i]:
                    previousSellStochasticRSI2 = True
                if stochRSIK2[i-1] <= stochRSID2[i-1] and stochRSIK2[i] > stochRSID2[i]:
                    previousBuyStochasticRSI2 = True
                # previousSellStochasticRSI2, previousBuyStochasticRSI2 = previousBuyStochasticRSI2, previousSellStochasticRSI2)

                if previousSellStochasticRSI2 and previousBuyStochasticRSI2:
                    previousBuyStochasticRSI2 = False
                    previousSellStochasticRSI2 = False   
                if previousSellStochasticRSI2 == True:
                    print("SELL: 2")
                    send_message("SELL: 2", bot)
                    if count2 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count2+=1
                
                if previousBuyStochasticRSI2 == True:
                    print("BUY: 2")
                    send_message("BUY: 2", bot)
                    if count2 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count2+=1
                #--------STOCH2RSI----------#


                #--------STOCH3RSI----------#
                longRunSTOCHRSI3, shortRunSTOCHRSI3 = findSelection(previousBuyStochasticRSI3, previousSellStochasticRSI3, longRunSTOCHRSI3, shortRunSTOCHRSI3, i) 
                shortRunSTOCHRSI3, longRunSTOCHRSI3, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI3, longRunSTOCHRSI3, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI3 = previousBuyStochasticRSI3 = False

                if stochRSIK3[i-1] >= stochRSID3[i-1] and stochRSIK3[i] < stochRSID3[i]:
                    previousSellStochasticRSI3 = True
                if stochRSIK3[i-1] <= stochRSID3[i-1] and stochRSIK3[i] > stochRSID3[i]:
                    previousBuyStochasticRSI3 = True
                # previousSellStochasticRSI3, previousBuyStochasticRSI3 = previousBuyStochasticRSI3, previousSellStochasticRSI3)

                if previousSellStochasticRSI3 and previousBuyStochasticRSI3:
                    previousBuyStochasticRSI3 = False
                    previousSellStochasticRSI3 = False   
                if previousSellStochasticRSI3 == True:
                    print("SELL: 3")
                    send_message("SELL: 3", bot)
                                      
                    if count3 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count3+=1
                
                if previousBuyStochasticRSI3 == True:
                    print("BUY: 3")
                    send_message("BUY: 3", bot)
                                         
                    if count3 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count3+=1
                #--------STOCH3RSI----------#



                #--------STOCH4RSI----------#
                longRunSTOCHRSI4, shortRunSTOCHRSI4 = findSelection(previousBuyStochasticRSI4, previousSellStochasticRSI4, longRunSTOCHRSI4, shortRunSTOCHRSI4, i) 
                shortRunSTOCHRSI4, longRunSTOCHRSI4, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI4, longRunSTOCHRSI4, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI4 = previousBuyStochasticRSI4 = False

                if stochRSIK4[i-1] >= stochRSID4[i-1] and stochRSIK4[i] < stochRSID4[i]:
                    previousSellStochasticRSI4 = True
                if stochRSIK4[i-1] <= stochRSID4[i-1] and stochRSIK4[i] > stochRSID4[i]:
                    previousBuyStochasticRSI4 = True
                # previousSellStochasticRSI4, previousBuyStochasticRSI4 = previousBuyStochasticRSI4, previousSellStochasticRSI4)

                if previousSellStochasticRSI4 and previousBuyStochasticRSI4:
                    previousBuyStochasticRSI4 = False
                    previousSellStochasticRSI4 = False   
                if previousSellStochasticRSI4 == True:
                    print("SELL: 4")
                    send_message("SELL: 4", bot)
                                      
                    if count4 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count4+=1
                
                if previousBuyStochasticRSI4 == True:
                    print("BUY: 4")
                    send_message("BUY: 4", bot)
                                         
                    if count4 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count4+=1
                #--------STOCH4RSI----------#



                #--------STOCH5RSI----------#
                longRunSTOCHRSI5, shortRunSTOCHRSI5 = findSelection(previousBuyStochasticRSI5, previousSellStochasticRSI5, longRunSTOCHRSI5, shortRunSTOCHRSI5, i) 
                shortRunSTOCHRSI5, longRunSTOCHRSI5, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI5, longRunSTOCHRSI5, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI5 = previousBuyStochasticRSI5 = False

                if stochRSIK5[i-1] >= stochRSID5[i-1] and stochRSIK5[i] < stochRSID5[i]:
                    previousSellStochasticRSI5 = True
                if stochRSIK5[i-1] <= stochRSID5[i-1] and stochRSIK5[i] > stochRSID5[i]:
                    previousBuyStochasticRSI5 = True
                # previousSellStochasticRSI5, previousBuyStochasticRSI5 = previousBuyStochasticRSI5, previousSellStochasticRSI5)

                if previousSellStochasticRSI5 and previousBuyStochasticRSI5:
                    previousBuyStochasticRSI5 = False
                    previousSellStochasticRSI5 = False   
                if previousSellStochasticRSI5 == True:
                    print("SELL: 5")
                    send_message("SELL: 5", bot)
                    if count5 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count5+=1
                
                if previousBuyStochasticRSI5 == True:
                    print("BUY: 5")
                    send_message("BUY: 5", bot)
                    if count5 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count5+=1
                #--------STOCH5RSI----------#


                #--------STOCH6RSI----------#
                longRunSTOCHRSI6, shortRunSTOCHRSI6 = findSelection(previousBuyStochasticRSI6, previousSellStochasticRSI6, longRunSTOCHRSI6, shortRunSTOCHRSI6, i) 
                shortRunSTOCHRSI6, longRunSTOCHRSI6, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI6, longRunSTOCHRSI6, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI6 = previousBuyStochasticRSI6 = False

                if stochRSIK6[i-1] >= stochRSID6[i-1] and stochRSIK6[i] < stochRSID6[i]:
                    previousSellStochasticRSI6 = True
                if stochRSIK6[i-1] <= stochRSID6[i-1] and stochRSIK6[i] > stochRSID6[i]:
                    previousBuyStochasticRSI6 = True
                # previousSellStochasticRSI6, previousBuyStochasticRSI6 = previousBuyStochasticRSI6, previousSellStochasticRSI6)

                if previousSellStochasticRSI6 and previousBuyStochasticRSI6:
                    previousBuyStochasticRSI6 = False
                    previousSellStochasticRSI6 = False   
                if previousSellStochasticRSI6 == True:
                    print("SELL: 6")
                    send_message("SELL: 6", bot)
                    if count6 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count6+=1
                
                if previousBuyStochasticRSI6 == True:
                    print("BUY: 6")
                    send_message("BUY: 6", bot)
                    if count6 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count6+=1
                #--------STOCH6RSI----------#



                #--------STOCH7RSI----------#
                longRunSTOCHRSI7, shortRunSTOCHRSI7 = findSelection(previousBuyStochasticRSI7, previousSellStochasticRSI7, longRunSTOCHRSI7, shortRunSTOCHRSI7, i) 
                shortRunSTOCHRSI7, longRunSTOCHRSI7, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI7, longRunSTOCHRSI7, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI7 = previousBuyStochasticRSI7 = False

                if stochRSIK7[i-1] >= stochRSID7[i-1] and stochRSIK7[i] < stochRSID7[i]:
                    previousSellStochasticRSI7 = True
                if stochRSIK7[i-1] <= stochRSID7[i-1] and stochRSIK7[i] > stochRSID7[i]:
                    previousBuyStochasticRSI7 = True
                # previousSellStochasticRSI7, previousBuyStochasticRSI7 = previousBuyStochasticRSI7, previousSellStochasticRSI7)

                if previousSellStochasticRSI7 and previousBuyStochasticRSI7:
                    previousBuyStochasticRSI7 = False
                    previousSellStochasticRSI7 = False   
                if previousSellStochasticRSI7 == True:
                    print("SELL: 7")
                    send_message("SELL: 7", bot)
                    if count7 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count7+=1
                
                if previousBuyStochasticRSI7 == True:
                    print("BUY: 7")
                    send_message("BUY: 7", bot)
                    if count7 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count7+=1
                #--------STOCH7RSI----------#



                #--------STOCH8RSI----------#
                longRunSTOCHRSI8, shortRunSTOCHRSI8 = findSelection(previousBuyStochasticRSI8, previousSellStochasticRSI8, longRunSTOCHRSI8, shortRunSTOCHRSI8, i) 
                shortRunSTOCHRSI8, longRunSTOCHRSI8, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI8, longRunSTOCHRSI8, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI8 = previousBuyStochasticRSI8 = False

                if stochRSIK8[i-1] >= stochRSID8[i-1] and stochRSIK8[i] < stochRSID8[i]:
                    previousSellStochasticRSI8 = True
                if stochRSIK8[i-1] <= stochRSID8[i-1] and stochRSIK8[i] > stochRSID8[i]:
                    previousBuyStochasticRSI8 = True
                # previousSellStochasticRSI8, previousBuyStochasticRSI8 = previousBuyStochasticRSI8, previousSellStochasticRSI8)

                if previousSellStochasticRSI8 and previousBuyStochasticRSI8:
                    previousBuyStochasticRSI8 = False
                    previousSellStochasticRSI8 = False   
                if previousSellStochasticRSI8 == True:
                    print("SELL: 8")
                    send_message("SELL: 8", bot)
                    if count8 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count8+=1
                
                if previousBuyStochasticRSI8 == True:
                    print("BUY: 8")
                    send_message("BUY: 8", bot)
                    if count8 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count8+=1
                #--------STOCH8RSI----------#



                #--------STOCH9RSI----------#
                longRunSTOCHRSI9, shortRunSTOCHRSI9 = findSelection(previousBuyStochasticRSI9, previousSellStochasticRSI9, longRunSTOCHRSI9, shortRunSTOCHRSI9, i) 
                shortRunSTOCHRSI9, longRunSTOCHRSI9, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI9, longRunSTOCHRSI9, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI9 = previousBuyStochasticRSI9 = False

                if stochRSIK9[i-1] >= stochRSID9[i-1] and stochRSIK9[i] < stochRSID9[i]:
                    previousSellStochasticRSI9 = True
                if stochRSIK9[i-1] <= stochRSID9[i-1] and stochRSIK9[i] > stochRSID9[i]:
                    previousBuyStochasticRSI9 = True
                # previousSellStochasticRSI9, previousBuyStochasticRSI9 = previousBuyStochasticRSI9, previousSellStochasticRSI9)

                if previousSellStochasticRSI9 and previousBuyStochasticRSI9:
                    previousBuyStochasticRSI9 = False
                    previousSellStochasticRSI9 = False   
                if previousSellStochasticRSI9 == True:
                    print("SELL: 9")
                    send_message("SELL: 9", bot)
                    if count9 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count9+=1
                
                if previousBuyStochasticRSI9 == True:
                    print("BUY: 9")
                    send_message("BUY: 9", bot)
                    if count9 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count9+=1
                #--------STOCH9RSI----------#


                
                #--------STOCH10RSI----------#
                longRunSTOCHRSI10, shortRunSTOCHRSI10 = findSelection(previousBuyStochasticRSI10, previousSellStochasticRSI10, longRunSTOCHRSI10, shortRunSTOCHRSI10, i) 
                shortRunSTOCHRSI10, longRunSTOCHRSI10, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI10, longRunSTOCHRSI10, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI10 = previousBuyStochasticRSI10 = False

                if stochRSIK10[i-1] >= stochRSID10[i-1] and stochRSIK10[i] < stochRSID10[i]:
                    previousSellStochasticRSI10 = True
                if stochRSIK10[i-1] <= stochRSID10[i-1] and stochRSIK10[i] > stochRSID10[i]:
                    previousBuyStochasticRSI10 = True
                # previousSellStochasticRSI10, previousBuyStochasticRSI10 = previousBuyStochasticRSI10, previousSellStochasticRSI10)

                if previousSellStochasticRSI10 and previousBuyStochasticRSI10:
                    previousBuyStochasticRSI10 = False
                    previousSellStochasticRSI10 = False   
                if previousSellStochasticRSI10 == True:
                    print("SELL: 10")
                    send_message("SELL: 10", bot)
                    if count10 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count10+=1
                
                if previousBuyStochasticRSI10 == True:
                    print("BUY: 10")
                    send_message("BUY: 10", bot)
                    if count10 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count10+=1
                #--------STOCH10RSI----------#



                #--------STOCH11RSI----------#
                longRunSTOCHRSI11, shortRunSTOCHRSI11 = findSelection(previousBuyStochasticRSI11, previousSellStochasticRSI11, longRunSTOCHRSI11, shortRunSTOCHRSI11, i) 
                shortRunSTOCHRSI11, longRunSTOCHRSI11, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI11, longRunSTOCHRSI11, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI11 = previousBuyStochasticRSI11 = False

                if stochRSIK11[i-1] >= stochRSID11[i-1] and stochRSIK11[i] < stochRSID11[i]:
                    previousSellStochasticRSI11 = True
                if stochRSIK11[i-1] <= stochRSID11[i-1] and stochRSIK11[i] > stochRSID11[i]:
                    previousBuyStochasticRSI11 = True
                # previousSellStochasticRSI11, previousBuyStochasticRSI11 = previousBuyStochasticRSI11, previousSellStochasticRSI11)

                if previousSellStochasticRSI11 and previousBuyStochasticRSI11:
                    previousBuyStochasticRSI11 = False
                    previousSellStochasticRSI11 = False   
                if previousSellStochasticRSI11 == True:
                    print("SELL: 11")
                    send_message("SELL: 11", bot)
                                      
                    if count11 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count11+=1
                
                if previousBuyStochasticRSI11 == True:
                    print("BUY: 11")
                    send_message("BUY: 11", bot)
                                         
                    if count11 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count11+=1
                #--------STOCH11RSI----------#



                #--------STOCH12RSI----------#
                longRunSTOCHRSI12, shortRunSTOCHRSI12 = findSelection(previousBuyStochasticRSI12, previousSellStochasticRSI12, longRunSTOCHRSI12, shortRunSTOCHRSI12, i) 
                shortRunSTOCHRSI12, longRunSTOCHRSI12, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI12, longRunSTOCHRSI12, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI12 = previousBuyStochasticRSI12 = False

                if stochRSIK12[i-1] >= stochRSID12[i-1] and stochRSIK12[i] < stochRSID12[i]:
                    previousSellStochasticRSI12 = True
                if stochRSIK12[i-1] <= stochRSID12[i-1] and stochRSIK12[i] > stochRSID12[i]:
                    previousBuyStochasticRSI12 = True
                # previousSellStochasticRSI12, previousBuyStochasticRSI12 = previousBuyStochasticRSI12, previousSellStochasticRSI12)

                if previousSellStochasticRSI12 and previousBuyStochasticRSI12:
                    previousBuyStochasticRSI12 = False
                    previousSellStochasticRSI12 = False   
                if previousSellStochasticRSI12 == True:
                    print("SELL: 12")
                    send_message("SELL: 12", bot)
                    if count12 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count12+=1
                
                if previousBuyStochasticRSI12 == True:
                    print("BUY: 12")
                    send_message("BUY: 12", bot)
                    
                    if count12 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count12+=1
                #--------STOCH12RSI----------#



                #--------STOCH13RSI----------#
                longRunSTOCHRSI13, shortRunSTOCHRSI13 = findSelection(previousBuyStochasticRSI13, previousSellStochasticRSI13, longRunSTOCHRSI13, shortRunSTOCHRSI13, i) 
                shortRunSTOCHRSI13, longRunSTOCHRSI13, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI13, longRunSTOCHRSI13, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI13 = previousBuyStochasticRSI13 = False

                if stochRSIK13[i-1] >= stochRSID13[i-1] and stochRSIK13[i] < stochRSID13[i]:
                    previousSellStochasticRSI13 = True
                if stochRSIK13[i-1] <= stochRSID13[i-1] and stochRSIK13[i] > stochRSID13[i]:
                    previousBuyStochasticRSI13 = True
                # previousSellStochasticRSI13, previousBuyStochasticRSI13 = previousBuyStochasticRSI13, previousSellStochasticRSI13)

                if previousSellStochasticRSI13 and previousBuyStochasticRSI13:
                    previousBuyStochasticRSI13 = False
                    previousSellStochasticRSI13 = False   
                if previousSellStochasticRSI13 == True:
                    print("SELL: 13")
                    send_message("SELL: 13", bot)
                    if count13 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count13+=1
                
                if previousBuyStochasticRSI13 == True:
                    print("BUY: 13")
                    send_message("BUY: 13", bot)
                    if count13 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count13+=1
                #--------STOCH13RSI----------#



                #--------STOCH14RSI----------#
                longRunSTOCHRSI14, shortRunSTOCHRSI14 = findSelection(previousBuyStochasticRSI14, previousSellStochasticRSI14, longRunSTOCHRSI14, shortRunSTOCHRSI14, i) 
                shortRunSTOCHRSI14, longRunSTOCHRSI14, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI14, longRunSTOCHRSI14, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI14 = previousBuyStochasticRSI14 = False

                if stochRSIK14[i-1] >= stochRSID14[i-1] and stochRSIK14[i] < stochRSID14[i]:
                    previousSellStochasticRSI14 = True
                if stochRSIK14[i-1] <= stochRSID14[i-1] and stochRSIK14[i] > stochRSID14[i]:
                    previousBuyStochasticRSI14 = True
                # previousSellStochasticRSI14, previousBuyStochasticRSI14 = previousBuyStochasticRSI14, previousSellStochasticRSI14)

                if previousSellStochasticRSI14 and previousBuyStochasticRSI14:
                    previousBuyStochasticRSI14 = False
                    previousSellStochasticRSI14 = False   
                if previousSellStochasticRSI14 == True:
                    print("SELL: 14")
                    send_message("SELL: 14", bot)
                    if count14 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count14+=1
                
                if previousBuyStochasticRSI14 == True:
                    print("BUY: 14")
                    send_message("BUY: 14", bot)
                    if count14 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count14+=1
                #--------STOCH14RSI----------#


                #--------STOCH15RSI----------#
                longRunSTOCHRSI15, shortRunSTOCHRSI15 = findSelection(previousBuyStochasticRSI15, previousSellStochasticRSI15, longRunSTOCHRSI15, shortRunSTOCHRSI15, i) 
                shortRunSTOCHRSI15, longRunSTOCHRSI15, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI15, longRunSTOCHRSI15, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI15 = previousBuyStochasticRSI15 = False

                if stochRSIK15[i-1] >= stochRSID15[i-1] and stochRSIK15[i] < stochRSID15[i]:
                    previousSellStochasticRSI15 = True
                if stochRSIK15[i-1] <= stochRSID15[i-1] and stochRSIK15[i] > stochRSID15[i]:
                    previousBuyStochasticRSI15 = True
                # previousSellStochasticRSI15, previousBuyStochasticRSI15 = previousBuyStochasticRSI15, previousSellStochasticRSI15)

                if previousSellStochasticRSI15 and previousBuyStochasticRSI15:
                    previousBuyStochasticRSI15 = False
                    previousSellStochasticRSI15 = False   
                if previousSellStochasticRSI15 == True:
                    print("SELL: 15")
                    send_message("SELL: 15", bot)
                    if count15 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count15+=1
                
                if previousBuyStochasticRSI15 == True:
                    print("BUY: 15")
                    send_message("BUY: 15", bot)
                    if count15 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count15+=1
                #--------STOCH15RSI----------#



                #--------STOCH16RSI----------#
                longRunSTOCHRSI16, shortRunSTOCHRSI16 = findSelection(previousBuyStochasticRSI16, previousSellStochasticRSI16, longRunSTOCHRSI16, shortRunSTOCHRSI16, i) 
                shortRunSTOCHRSI16, longRunSTOCHRSI16, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI16, longRunSTOCHRSI16, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI16 = previousBuyStochasticRSI16 = False

                if stochRSIK16[i-1] >= stochRSID16[i-1] and stochRSIK16[i] < stochRSID16[i]:
                    previousSellStochasticRSI16 = True
                if stochRSIK16[i-1] <= stochRSID16[i-1] and stochRSIK16[i] > stochRSID16[i]:
                    previousBuyStochasticRSI16 = True
                # previousSellStochasticRSI16, previousBuyStochasticRSI16 = previousBuyStochasticRSI16, previousSellStochasticRSI16)

                if previousSellStochasticRSI16 and previousBuyStochasticRSI16:
                    previousBuyStochasticRSI16 = False
                    previousSellStochasticRSI16 = False   
                if previousSellStochasticRSI16 == True:
                    print("SELL: 16")
                    send_message("SELL: 16", bot)
                    if count16 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count16+=1
                
                if previousBuyStochasticRSI16 == True:
                    print("BUY: 16")
                    send_message("BUY: 16", bot)
                    if count16 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count16+=1
                #--------STOCH16RSI----------#


                #--------STOCH17RSI----------#
                longRunSTOCHRSI17, shortRunSTOCHRSI17 = findSelection(previousBuyStochasticRSI17, previousSellStochasticRSI17, longRunSTOCHRSI17, shortRunSTOCHRSI17, i) 
                shortRunSTOCHRSI17, longRunSTOCHRSI17, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI17, longRunSTOCHRSI17, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI17 = previousBuyStochasticRSI17 = False

                if stochRSIK17[i-1] >= stochRSID17[i-1] and stochRSIK17[i] < stochRSID17[i]:
                    previousSellStochasticRSI17 = True
                if stochRSIK17[i-1] <= stochRSID17[i-1] and stochRSIK17[i] > stochRSID17[i]:
                    previousBuyStochasticRSI17 = True
                # previousSellStochasticRSI17, previousBuyStochasticRSI17 = previousBuyStochasticRSI17, previousSellStochasticRSI17)

                if previousSellStochasticRSI17 and previousBuyStochasticRSI17:
                    previousBuyStochasticRSI17 = False
                    previousSellStochasticRSI17 = False   
                if previousSellStochasticRSI17 == True:
                    print("SELL: 17")
                    send_message("SELL: 17", bot)
                    if count17 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)                    
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count17+=1
                
                if previousBuyStochasticRSI17 == True:
                    print("BUY: 17")
                    send_message("BUY: 17", bot)
                    if count17 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count17+=1
                #--------STOCH17RSI----------#



                #--------STOCH18RSI----------#
                longRunSTOCHRSI18, shortRunSTOCHRSI18 = findSelection(previousBuyStochasticRSI18, previousSellStochasticRSI18, longRunSTOCHRSI18, shortRunSTOCHRSI18, i) 
                shortRunSTOCHRSI18, longRunSTOCHRSI18, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI18, longRunSTOCHRSI18, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI18 = previousBuyStochasticRSI18 = False

                if stochRSIK18[i-1] >= stochRSID18[i-1] and stochRSIK18[i] < stochRSID18[i]:
                    previousSellStochasticRSI18 = True
                if stochRSIK18[i-1] <= stochRSID18[i-1] and stochRSIK18[i] > stochRSID18[i]:
                    previousBuyStochasticRSI18 = True
                # previousSellStochasticRSI18, previousBuyStochasticRSI18 = previousBuyStochasticRSI18, previousSellStochasticRSI18)

                if previousSellStochasticRSI18 and previousBuyStochasticRSI18:
                    previousBuyStochasticRSI18 = False
                    previousSellStochasticRSI18 = False   
                if previousSellStochasticRSI18 == True:
                    print("SELL: 18")
                    send_message("SELL: 18", bot)
                    if count18 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count18+=1
                
                if previousBuyStochasticRSI18 == True:
                    print("BUY: 18")
                    send_message("BUY: 18", bot)
                    if count18 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count18+=1
                #--------STOCH18RSI----------#



                #--------STOCH19RSI----------#
                longRunSTOCHRSI19, shortRunSTOCHRSI19 = findSelection(previousBuyStochasticRSI19, previousSellStochasticRSI19, longRunSTOCHRSI19, shortRunSTOCHRSI19, i) 
                shortRunSTOCHRSI19, longRunSTOCHRSI19, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI19, longRunSTOCHRSI19, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI19 = previousBuyStochasticRSI19 = False

                if stochRSIK19[i-1] >= stochRSID19[i-1] and stochRSIK19[i] < stochRSID19[i]:
                    previousSellStochasticRSI19 = True
                if stochRSIK19[i-1] <= stochRSID19[i-1] and stochRSIK19[i] > stochRSID19[i]:
                    previousBuyStochasticRSI19 = True
                # previousSellStochasticRSI19, previousBuyStochasticRSI19 = previousBuyStochasticRSI19, previousSellStochasticRSI19)

                if previousSellStochasticRSI19 and previousBuyStochasticRSI19:
                    previousBuyStochasticRSI19 = False
                    previousSellStochasticRSI19 = False   
                if previousSellStochasticRSI19 == True:
                    print("SELL: 19")
                    send_message("SELL: 19", bot)
                    if count19 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count19+=1
                
                if previousBuyStochasticRSI19 == True:
                    print("BUY: 19")
                    send_message("BUY: 19", bot)
                    if count19 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count19+=1
                #--------STOCH19RSI----------#



                #--------STOCH20RSI----------#
                longRunSTOCHRSI20, shortRunSTOCHRSI20 = findSelection(previousBuyStochasticRSI20, previousSellStochasticRSI20, longRunSTOCHRSI20, shortRunSTOCHRSI20, i) 
                shortRunSTOCHRSI20, longRunSTOCHRSI20, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI20, longRunSTOCHRSI20, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI20 = previousBuyStochasticRSI20 = False

                if stochRSIK20[i-1] >= stochRSID20[i-1] and stochRSIK20[i] < stochRSID20[i]:
                    previousSellStochasticRSI20 = True
                if stochRSIK20[i-1] <= stochRSID20[i-1] and stochRSIK20[i] > stochRSID20[i]:
                    previousBuyStochasticRSI20 = True
                # previousSellStochasticRSI20, previousBuyStochasticRSI20 = previousBuyStochasticRSI20, previousSellStochasticRSI20)

                if previousSellStochasticRSI20 and previousBuyStochasticRSI20:
                    previousBuyStochasticRSI20 = False
                    previousSellStochasticRSI20 = False   
                if previousSellStochasticRSI20 == True:
                    print("SELL: 20")
                    send_message("SELL: 20", bot)
                                      
                    if count20 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count20+=1
                
                if previousBuyStochasticRSI20 == True:
                    print("BUY: 20")
                    send_message("BUY: 20", bot)
                                         
                    if count20 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count20+=1
                #--------STOCH20RSI----------#


                #--------STOCH21RSI----------#
                longRunSTOCHRSI21, shortRunSTOCHRSI21 = findSelection(previousBuyStochasticRSI21, previousSellStochasticRSI21, longRunSTOCHRSI21, shortRunSTOCHRSI21, i) 
                shortRunSTOCHRSI21, longRunSTOCHRSI21, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI21, longRunSTOCHRSI21, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI21 = previousBuyStochasticRSI21 = False

                if stochRSIK21[i-1] >= stochRSID21[i-1] and stochRSIK21[i] < stochRSID21[i]:
                    previousSellStochasticRSI21 = True
                if stochRSIK21[i-1] <= stochRSID21[i-1] and stochRSIK21[i] > stochRSID21[i]:
                    previousBuyStochasticRSI21 = True
                # previousSellStochasticRSI21, previousBuyStochasticRSI21 = previousBuyStochasticRSI21, previousSellStochasticRSI21)

                if previousSellStochasticRSI21 and previousBuyStochasticRSI21:
                    previousBuyStochasticRSI21 = False
                    previousSellStochasticRSI21 = False   
                if previousSellStochasticRSI21 == True:
                    print("SELL: 21")
                    send_message("SELL: 21", bot)
                    if count21 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count21+=1
                
                if previousBuyStochasticRSI21 == True:
                    print("BUY: 21")
                    send_message("BUY: 21", bot)
                    if count21 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count21+=1
                #--------STOCH21RSI----------#



                #--------STOCH22RSI----------#
                longRunSTOCHRSI22, shortRunSTOCHRSI22 = findSelection(previousBuyStochasticRSI22, previousSellStochasticRSI22, longRunSTOCHRSI22, shortRunSTOCHRSI22, i) 
                shortRunSTOCHRSI22, longRunSTOCHRSI22, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI22, longRunSTOCHRSI22, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI22 = previousBuyStochasticRSI22 = False

                if stochRSIK22[i-1] >= stochRSID22[i-1] and stochRSIK22[i] < stochRSID22[i]:
                    previousSellStochasticRSI22 = True
                if stochRSIK22[i-1] <= stochRSID22[i-1] and stochRSIK22[i] > stochRSID22[i]:
                    previousBuyStochasticRSI22 = True
                # previousSellStochasticRSI22, previousBuyStochasticRSI22 = previousBuyStochasticRSI22, previousSellStochasticRSI22)

                if previousSellStochasticRSI22 and previousBuyStochasticRSI22:
                    previousBuyStochasticRSI22 = False
                    previousSellStochasticRSI22 = False   
                if previousSellStochasticRSI22 == True:
                    print("SELL: 22")
                    send_message("SELL: 22", bot)
                    if count22 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count22+=1
                
                if previousBuyStochasticRSI22 == True:
                    print("BUY: 22")
                    send_message("BUY: 22", bot)
                    if count22 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count22+=1
                #--------STOCH22RSI----------#



                #--------STOCH23RSI----------#
                longRunSTOCHRSI23, shortRunSTOCHRSI23 = findSelection(previousBuyStochasticRSI23, previousSellStochasticRSI23, longRunSTOCHRSI23, shortRunSTOCHRSI23, i) 
                shortRunSTOCHRSI23, longRunSTOCHRSI23, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI23, longRunSTOCHRSI23, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI23 = previousBuyStochasticRSI23 = False

                if stochRSIK23[i-1] >= stochRSID23[i-1] and stochRSIK23[i] < stochRSID23[i]:
                    previousSellStochasticRSI23 = True
                if stochRSIK23[i-1] <= stochRSID23[i-1] and stochRSIK23[i] > stochRSID23[i]:
                    previousBuyStochasticRSI23 = True
                # previousSellStochasticRSI23, previousBuyStochasticRSI23 = previousBuyStochasticRSI23, previousSellStochasticRSI23)

                if previousSellStochasticRSI23 and previousBuyStochasticRSI23:
                    previousBuyStochasticRSI23 = False
                    previousSellStochasticRSI23 = False   
                if previousSellStochasticRSI23 == True:
                    print("SELL: 23")
                    send_message("SELL: 23", bot)
                                      
                    if count23 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)     
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count23+=1
                
                if previousBuyStochasticRSI23 == True:
                    print("BUY: 23")
                    send_message("BUY: 23", bot)
                                         
                    if count23 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")
                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count23+=1
                #--------STOCH23RSI----------#



                #--------STOCH24RSI----------#
                longRunSTOCHRSI24, shortRunSTOCHRSI24 = findSelection(previousBuyStochasticRSI24, previousSellStochasticRSI24, longRunSTOCHRSI24, shortRunSTOCHRSI24, i) 
                shortRunSTOCHRSI24, longRunSTOCHRSI24, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI24, longRunSTOCHRSI24, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI24 = previousBuyStochasticRSI24 = False

                if stochRSIK24[i-1] >= stochRSID24[i-1] and stochRSIK24[i] < stochRSID24[i]:
                    previousSellStochasticRSI24 = True
                if stochRSIK24[i-1] <= stochRSID24[i-1] and stochRSIK24[i] > stochRSID24[i]:
                    previousBuyStochasticRSI24 = True
                # previousSellStochasticRSI24, previousBuyStochasticRSI24 = previousBuyStochasticRSI24, previousSellStochasticRSI24)

                if previousSellStochasticRSI24 and previousBuyStochasticRSI24:
                    previousBuyStochasticRSI24 = False
                    previousSellStochasticRSI24 = False   
                if previousSellStochasticRSI24 == True:
                    print("SELL: 24")
                    send_message("SELL: 24", bot)
                    if count24 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count24+=1
                
                if previousBuyStochasticRSI24 == True:
                    print("BUY: 24")
                    send_message("BUY: 24", bot)
                    if count24 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")


                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count24+=1
                #--------STOCH24RSI----------#

                #--------STOCH25RSI----------#
                longRunSTOCHRSI25, shortRunSTOCHRSI25 = findSelection(previousBuyStochasticRSI25, previousSellStochasticRSI25, longRunSTOCHRSI25, shortRunSTOCHRSI25, i) 
                shortRunSTOCHRSI25, longRunSTOCHRSI25, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI25, longRunSTOCHRSI25, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

                previousSellStochasticRSI25 = previousBuyStochasticRSI25 = False

                if stochRSIK25[i-1] >= stochRSID25[i-1] and stochRSIK25[i] < stochRSID25[i]:
                    previousSellStochasticRSI25 = True
                if stochRSIK25[i-1] <= stochRSID25[i-1] and stochRSIK25[i] > stochRSID25[i]:
                    previousBuyStochasticRSI25 = True
                # previousSellStochasticRSI25, previousBuyStochasticRSI25 = previousBuyStochasticRSI25, previousSellStochasticRSI25)

                if previousSellStochasticRSI25 and previousBuyStochasticRSI25:
                    previousBuyStochasticRSI25 = False
                    previousSellStochasticRSI25 = False   
                if previousSellStochasticRSI25 == True:
                    print("SELL: 25")
                    send_message("SELL: 25", bot)
                    if count25 > 0:
                        try:
                            closeLong(bingx_client, symbol, betAmount, maxLev)
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            print("No position to close RQTRQT")       
                            buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)             
                    else:
                        buyShort(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count25+=1
                
                if previousBuyStochasticRSI25 == True:
                    print("BUY: 25")
                    send_message("BUY: 25", bot)
                    if count25 > 0:
                        try:
                            closeShort(bingx_client, symbol, betAmount, maxLev)
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                        except:
                            buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                            print("No position to close RQTRQT")

                    else:
                        buyLong(bingx_client, symbol, betAmount, maxLev, stopLoss)
                    count25+=1
                #--------STOCH25RSI----------#
                yes = False
                print(datetime.now())
                break
            except Exception as e:
                yes = True
                send_message(str(e), bot)
    else:
        # print('L BOZO')
        time.sleep(59)