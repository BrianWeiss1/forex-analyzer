# from src.testGrabData import calltimes30
# from longTermCryptoFINALV3 import simulateCrypto
# from src.testSpecial import formatDataset
# import time
# import threading


# if __name__ == '__main__':
#     f = open('documents/binanceSymbols.txt', 'r')
#     dataSymbol = f.readlines()
#     dataSymbol = eval(dataSymbol[0])
#     f.close()
#     def funct(dataSymbol):
#         bestAvgPercent = 0
#         worstAvgPercent = 0
#         # print(data)
#         for i in range(len(dataSymbol)):
#             print(i)
#             try:
#                 calltimes30(dataSymbol[i])
#                 # time.sleep(5)
#                 f = open("documents/binance30.txt", "r")
#                 data = f.readlines()
#                 data = eval(data[0])
#                 f.close()
#                 data = formatDataset(data)
#                 columns_to_convert = ['open', 'high', 'low', 'close', 'volume']

#                 for column in columns_to_convert:
#                     data[column] = data[column].astype(float)
                
#                 BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent = simulateCrypto(data)
#                 # time.sleep(5)
#                 if AvgPercent > bestAvgPercent:
#                     bestAvgPercent = AvgPercent
#                     bestSymbol = dataSymbol[i]
#                 if AvgPercent < worstAvgPercent:
#                     worstAvgPercent = AvgPercent
#                     worstSymbol = dataSymbol[i]
#             except Exception as e:
#                 print(e)

                
#     print("END OF SIMULATION: \n\n\n")
#     print("BestPercent: " + str(bestAvgPercent))
#     print('\nSYMBOL: ' + str(bestSymbol))
#     print("WorstPercent: " + str(worstAvgPercent))
#     print('\nSYMBOL: ' + str(worstSymbol))
    
#     # XVSUSDT
#     # RADUSDT
import threading
from src.testGrabData import calltimes30
from longTermCryptoFINALV3 import simulateCrypto
from src.testSpecial import formatDataset
import time

def process_symbol(dataSymbol, best_results, worst_results):
    bestAvgPercent = 0
    worstAvgPercent = 0
    bestSymbol = None
    worstSymbol = None

    for i in range(len(dataSymbol)):
        print(i)
        try:
            calltimes30(dataSymbol[i])
            # time.sleep(5)
            f = open("documents/binance30.txt", "r")
            data = f.readlines()
            data = eval(data[0])
            f.close()
            data = formatDataset(data)
            columns_to_convert = ['open', 'high', 'low', 'close', 'volume']

            for column in columns_to_convert:
                data[column] = data[column].astype(float)
            
            BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent = simulateCrypto(data)
            # time.sleep(5)
            if AvgPercent > bestAvgPercent:
                bestAvgPercent = AvgPercent
                bestSymbol = dataSymbol[i]
            if AvgPercent < worstAvgPercent:
                worstAvgPercent = AvgPercent
                worstSymbol = dataSymbol[i]
        except Exception as e:
            print(e)
    
    best_results.append((bestSymbol, bestAvgPercent))
    worst_results.append((worstSymbol, worstAvgPercent))

if __name__ == '__main__':
    f = open('documents/binanceSymbols.txt', 'r')
    dataSymbol = f.readlines()
    dataSymbol = eval(dataSymbol[0])
    f.close()

    # Number of threads you want to create
    num_threads = 40  # Adjust this as needed
    
    # Split the dataSymbol list into chunks for parallel processing
    chunk_size = len(dataSymbol) // num_threads
    data_chunks = [dataSymbol[i:i + chunk_size] for i in range(0, len(dataSymbol), chunk_size)]

    best_results = []
    worst_results = []

    threads = []
    for chunk in data_chunks:
        thread = threading.Thread(target=process_symbol, args=(chunk, best_results, worst_results))
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

    print("END OF SIMULATION: \n\n\n")
    print("BestPercent: " + str(best_result[1]))
    print('\nSYMBOL: ' + str(best_result[0]))
    print("WorstPercent: " + str(worst_result[1]))
    print('\nSYMBOL: ' + str(worst_result[0]))
