import SortLists

lst1 =  SortLists.openFileArrayNormal('lstSpecialNumsDECLINE.txt')
lst2 =  SortLists.openFileArrayNormal('lstSpecialNumsINCLINE.txt')
lst3 = []
# for i in range(len(lst1)):
#     value = str(lst1[i][0])
#     value = value.strip("(")
#     value = value.strip(")")
#     print(f'stochRSIK{1+i}, stochRSID{i+1} = get_StochasticRelitiveStrengthIndex(df, {value})')

for elements in lst1:
    elements[1] = abs(elements[1])
    lst3.append(elements)
for elements in lst2:
    print(elements)
    elements[1] = abs(elements[1])
    lst3.append(elements)
print(lst3)