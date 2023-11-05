import SortLists

# lst1 =  SortLists.openFileArrayNormal('lstSpecialNumsDECLINE.txt')
# lst2 =  SortLists.openFileArrayNormal('lstSpecialNumsINCLINE.txt')

lst1 = SortLists.openFileArrayNormal('BinanceSymbolsV2.txt')
lst2 = SortLists.openFileArrayNormal('binanceSymbols.txt')
lst3 = []
# for i in range(len(lst1)):
#     value = str(lst1[i][0])
#     value = value.strip("(")
#     value = value.strip(")")
#     print(f'stochRSIK{1+i}, stochRSID{i+1} = get_StochasticRelitiveStrengthIndex(df, {value})')
# print(lst1)
print(len(lst1))
print(len(lst2))
for elements in lst1:
    # print(elements)
    # elements = eval(elements)
    lst3.append(elements)
for elements in lst2:
    # print(elements)
    # elements[1] = eval(elements[1])
    lst3.append(elements)
from collections import OrderedDict

# Remove duplicates while preserving order
symbols = list(OrderedDict.fromkeys(lst3))

print(len(symbols))