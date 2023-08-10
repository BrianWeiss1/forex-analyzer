from datetime import datetime
from functions.StochasticOscillator import compareGetStoch, get_stochastic_oscillator
from specialFunctions import automaticBuy, automaticSell, checkTime

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
                infoSTOCH['%k'], infoSTOCH['%d'] = get_stochastic_oscillator((r'api_key.txt')[0], symbol)
                print("%K:" + str(infoSTOCH['%k']))
                print("%D:" + str(infoSTOCH['%d']))
                pointOfError = 5
                stochSignals = compareGetStoch(infoSTOCH['%k'], infoSTOCH['%d'], pointOfError)
                lst = []
                if (stochSignals['buy']):
                    print('Buy: ' + str(now))
                    automaticBuy(buy)
                    lst.append(now)

                if (stochSignals['sell']):
                    print('Sell ' + str(now))
                    automaticSell(sell)
                    lst.append(now)
                    
except KeyboardInterrupt:
    print(lst)