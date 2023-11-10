import numpy as np

f = open("test2.txt", 'r')
# print(f.readlines())
dic = eval(f.readlines()[0])
print(type(dic))

f.close()


# print(dic)
lst = []
for keys in dic:
    values = dic[keys]
    for value in values:
        # print(value[0])
        if value[0] == "BTCUSDT":
            lst.append([keys, value[1]])
lst = sorted(lst, key=lambda x:x[1])
print(len(lst))