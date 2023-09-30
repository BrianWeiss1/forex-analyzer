from src.simulate import simulate
from SpecialFunctions import formatDataset

if "__main__" == __name__:
    f = open("documents/data.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    data = formatDataset(data)
    
    lst, BestProfilio, WorseProfilio, Bestk, Bestj, worstk, worstj = simulate(data, 1.5, 0.1)
    #720mi
    # 77mil
    # 200bil


    if not lst:
        exit()
    
    total = sum(lst)
    average = total / len(lst)


    sorted_arr = sorted(lst)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        median = sorted_arr[n // 2]
    else:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2

    
    print("\n")
    print("Average Result: " + str(average))
    print("Median Result: " + str(median))
    print("\n")
    print("Best Portfolio: " + str(BestProfilio))
    print("J:" + str(Bestj))
    print("K: " + str(Bestk))
    print("Worst Portfolio: " + str(WorseProfilio))
    print("J: " + str(worstj))
    print("K: " + str(worstk))
