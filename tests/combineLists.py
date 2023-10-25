from SortLists import SortLists

lst1 =  SortLists.openFileArrayNormal('lstSpecialNumsDECLINE.txt')
lst2 =  SortLists.openFileArrayNormal('lstSpecialNumsINCLINE.txt')
lst3 = []
for elements in lst1:
    elements[1] = abs(elements[1])
    lst3.append(elements)
for elements in lst2:
    elements[1] = abs(elements[1])
    lst3.append(elements)
print(lst3)
