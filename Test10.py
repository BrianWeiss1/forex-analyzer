from src.testGrabData import calltimes30
from longTermCryptoFINALV3 import simulateCrypto
from src.testSpecial import formatDataset
import time
import threading
import queue

def process_symbol(symbol, result_queue, finished_event):
    try:
        calltimes30(symbol)
        f = open("documents/binance30.txt", "r")
        data = f.readlines()
        data = eval(data[0])
        f.close()
        data = formatDataset(data)
        columns_to_convert = ['open', 'high', 'low', 'close', 'volume']

        for column in columns_to_convert:
            data[column] = data[column].astype(float)

        BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent = simulateCrypto(data)
        result_queue.put((symbol, AvgPercent))
    except Exception as e:
        print(e)
        result_queue.put((symbol, None))
    finally:
        finished_event.set()

if __name__ == '__main__':
    f = open('documents/binanceSymbols.txt', 'r')
    dataSymbol = f.readlines()
    dataSymbol = eval(dataSymbol[0])
    f.close()

    bestAvgPercent = 0
    worstAvgPercent = 0
    bestSymbol = None
    worstSymbol = None

    result_queue = queue.Queue()
    finished_event = threading.Event()
    threads = []

    for symbol in dataSymbol:
        thread = threading.Thread(target=process_symbol, args=(symbol, result_queue, finished_event))
        threads.append(thread)
        thread.start()

    # Wait for all of the worker threads to finish processing symbols
    finished_event.wait()

    # Join all of the worker threads
    for thread in threads:
        thread.join()

    while not result_queue.empty():
        symbol, AvgPercent = result_queue.get()

        if AvgPercent is not None:
            # Check if the AvgPercent value is valid
            try:
                float(AvgPercent)
            except ValueError:
                continue

            if AvgPercent > bestAvgPercent:
                bestAvgPercent = AvgPercent
                bestSymbol = symbol
            if AvgPercent < worstAvgPercent:
                worstAvgPercent = AvgPercent
                worstSymbol = symbol

    print("END OF SIMULATION: \n\n\n")
    print("BestPercent: " + str(bestAvgPercent))
    print('\nSYMBOL: ' + str(bestSymbol))
    print("WorstPercent: " + str(worstAvgPercent))
    print('\nSYMBOL: ' + str(worstSymbol))
