import multiprocessing
from temp.RunSTOCHExpands import simulateCryptoExpands, grabForex
from temp.SpecialFunctions import formatDataset, formatDataset1, formatDataset3, formatDataset2
from temp.longTermPos import checkLuquidation, findSelection

def main():
    df = formatDataset2(formatDataset3(grabForex(5000)))
    num_processes = 18  # Adjust the number of processes as needed
    total_items = 300  # The total number of iterations in the loop
    chunk_size = total_items // num_processes

    pool = multiprocessing.Pool(processes=num_processes)

    # Split the loop into chunks and distribute them to processes
    chunks = [(df, i, i + chunk_size) for i in range(2, total_items, chunk_size)]
    results = pool.starmap(simulateCryptoExpands, chunks)
    pool.close()
    pool.join()
    combined_result = []
    for result in results:
        combined_result.extend(result)

    print(combined_result)


if "__main__" == __name__:
    main()
    
    # bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE = simulateCryptoExpands(df, 1, 2)
    # a
    # print("\n\nSIMULATION RESULTS: ")
    # print(lstSpecialNumsINCLINE)
    # print(lstSpecialNumsDECLINE)
    # f = open("documents/lstSpecialNumsINCLINE.txt", 'w')
    # f.write(str(lstSpecialNumsINCLINE))
    # f.close()
    # f = open("documents/lstSpecialNumsDECLINE.txt", 'w')
    # f.write(str(lstSpecialNumsDECLINE))
    # f.close()

    
    # print("\nBest Special Value: " + str(bestSpecialValue))
    # print("Values for which: " + str(BestSpecialValues))
    # print("\nWorst Special Value: " + str(worstSpecialValue))
    # print("Values for which" + str(WorstSpecialValues))
