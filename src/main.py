from datetime import datetime
from functions.StochasticOscillator import compareGetStoch, get_stochastic_oscillator
from functions.specialFunctions import automaticBuy, automaticSell, checkTime
lst = []
try:
    buy = 1118, 387
    sell = 1123, 462


    if __name__ == "__main__":
        symbol = 'AUDCHF'
        infoSTOCH = {}
        while True:
            if checkTime() == True:
                print(datetime.now())
                now = datetime.now()
                infoSTOCH['%k'], infoSTOCH['%d'] = get_stochastic_oscillator('d3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9', symbol)
                print("%K:" + str(infoSTOCH['%k']))
                print("%D:" + str(infoSTOCH['%d']))
                pointOfError = 5
                stochSignals = compareGetStoch(infoSTOCH['%k'], infoSTOCH['%d'], pointOfError)
                lst = []
                # if buyPrevious:

                if (stochSignals['buy']):
                    print('Buy: ' + str(now))
                    automaticBuy(buy)
                    lst.append(now)
                    buyPrevious = True
                if (stochSignals['sell']):
                    print('Sell ' + str(now))
                    automaticSell(sell)
                    lst.append(now)
                    sellPrevious = True
                    
except KeyboardInterrupt:
    print(lst)