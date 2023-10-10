import threading
from src.testGrabData import calltimes30
from longTermFINALV3 import simulateCrypto
from SpecialFunctions import formatDataset, formatDataset1
from src.testGrabData import calltimes30FIXED
from datetime import datetime, timedelta


def process_symbol(dataSymbol, best_results, worst_results, lst):
    try:
        bestAvgPercent = 0
        worstAvgPercent = 0
        bestSymbol = None
        worstSymbol = None
        bestNumSymbol = None
        worstNumSymbol = None
        worstNumPercent = 0
        bestNumPercent = 0
        
        

        for i in range(len(dataSymbol)):
            print(i)
            continment = True
            try:
                # calltimes30(dataSymbol[i], '2022-02-23')
                # # time.sleep(5)
                # f = open("documents/binance30.txt", "r")
                # data = f.readlines()
                # data = eval(data[0])
                # f.close()
                # data = formatDataset(data)
                # columns_to_convert = ['open', 'high', 'low', 'close', 'volume']

                # for column in columns_to_convert:
                #     data[column] = data[column].astype(float)
                DIFFERENCEYOUWANT = 10
                dic = {}
                printing = False
                count = 0
                totalAmount = 0
                df = formatDataset1(formatDataset(calltimes30FIXED(dataSymbol[i], (datetime.now()-timedelta(days=70)).strftime('%Y-%m-%d'))))
                
                # print(symbolVolume + ":")
                for x in range(48, 0, -1):
                    expFormula = 5*(pow(1.05, -x))
                    dic[x] = expFormula
                # print(dic)
                for key, value in dic.items():
                    # print(key)
                    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, key, False, 1+DIFFERENCEYOUWANT)
                    totalAmount += AvgPercent * value
                    # print(AvgPercent)
                    count += value
                predictedPercent = totalAmount/count
                print("PREDICTED PERCENT: " + str(round(predictedPercent, 3)) + "%")
                avgSum = 0
                countAAAAAAAAAA = 0
                for j in range(6, 1, -1):
                    BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue = simulateCrypto(df, j, False, 0)
                    # print(AvgPercent)
                    avgSum += AvgPercent
                    countAAAAAAAAAA += 1
                actualPercent = avgSum/countAAAAAAAAAA
                print("ACTUAL PERCENT: " + str(round(actualPercent, 2)) + "%")
                percentError = (abs(actualPercent-predictedPercent)/actualPercent)*100 # Percent error formula
                print("PERCENT ERROR: " + str(round(percentError, 2)) + "%")
                lst.append([dataSymbol[i], percentError])
                specialNum = 0
                AvgPercent = 0
                bestAvgPercent = 0
                worstAvgPercent = 0
                bestSymbol = 0
                worstSymbol = 0
                bestNumSymbol = 0
                worstNumSymbol = 0
                worstNumPercent = 0
                bestNumPercent = 0
                if AvgPercent > bestAvgPercent:
                    bestAvgPercent = AvgPercent
                    bestSymbol = dataSymbol[i]
                    bestSymbol = dataSymbol[i]
                if AvgPercent < worstAvgPercent:
                    worstAvgPercent = AvgPercent
                    worstSymbol = dataSymbol[i]
                if specialNum > bestNumPercent:
                    bestNumPercent = specialNum
                    bestNumSymbol = dataSymbol[i]
                if specialNum < worstNumPercent:
                    worstNumPercent = specialNum
                    worstNumSymbol = dataSymbol[i]
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print(lst)
            
    bestSymbol = bestNumSymbol
    worstSymbol = worstNumSymbol
    bestAvgPercent = bestNumPercent
    worstAvgPercent = worstNumPercent 
    
    best_results.append((bestSymbol, bestAvgPercent))
    worst_results.append((worstSymbol, worstAvgPercent))
    # bestNumSymbol.append()

if __name__ == '__main__':
    try:
        f = open('documents/binanceSymbols.txt', 'r')
        dataSymbol = f.readlines()
        dataSymbol = eval(dataSymbol[0])
        f.close()
        print(len(dataSymbol))
        lst = []

        # Number of threads you want to create
        num_threads = 10  # Adjust this as needed
        
        # Split the dataSymbol list into chunks for parallel processing
        chunk_size = len(dataSymbol) // num_threads
        
        data_chunks = [dataSymbol[i:i + chunk_size] for i in range(0, len(dataSymbol), chunk_size)]
        print(data_chunks)
        best_results = []
        worst_results = []

        threads = []
        for chunk in data_chunks:
            thread = threading.Thread(target=process_symbol, args=(chunk, best_results, worst_results, lst))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        
        #unterminated string literal (detected at line 1) (<string>, line 1)
        #leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers (<string>, line 1)
        #'{' was never closed (<string>, line 1)
        for thread in threads:
            thread.join()

        # Find the best and worst results from all threads
        best_result = max(best_results, key=lambda x: x[1])
        worst_result = min(worst_results, key=lambda x: x[1])
        print(lst)
        print("END OF SIMULATION: \n\n\n")
        print('\nSYMBOL: ' + str(best_result[0]))
        print("BestPercent: " + str(best_result[1]))
        print('\nSYMBOL: ' + str(worst_result[0]))
        print("WorstPercent: " + str(worst_result[1]))
    except KeyboardInterrupt:
        print(lst)
    
