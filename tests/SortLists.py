class SortLists:
    def openFileArray(file):
        doc = open(f'documents/special/{file}', 'r')
        aaa = doc.readline()
        lstSpecialValueOct15=eval(aaa)
        doc.close()
        return lstSpecialValueOct15
    def openFileArrayNormal(file):
        doc = open(f'documents/{file}', 'r')
        aaa = doc.readline()
        lstSpecialValueOct15=eval(aaa)
        doc.close()
        return lstSpecialValueOct15

if __name__ == '__main__':
    sortlist = SortLists()
    BestPercentNumOct14 = sortlist.openFileArray('bestPercentOct14.txt')
    specialValueOct15 = sortlist.openFileArray('lstSpecialValueOct15.txt')
    specialValueSTOCHRSIOct18 = sortlist.openFileArray('lstSpecialValueSTOCHRSIOct18.txt')
    specialValueOct20 = sortlist.openFileArray('lstSpecialValyueOct20.txt')
    stochSpeicalValueOct23 = sortlist.openFileArray('stochSpecialNumOct23.txt')
    stochRSISpeicalValueOct23 = sortlist.openFileArray('stochRSISpecialNumOct23.txt')
    ALllist = stochSpeicalValueOct23 
    dic = {}
    for i in range(len(ALllist)):
        # print(farDatapoints[i][0])
        # print(type(dic[farDatapoints[i][0]]))
        try:
            if dic[ALllist[i][0]]:
                dic[ALllist[i][0]] += dic[ALllist[i][1]]
        except KeyError:
            dic[ALllist[i][0]] = ALllist[i][1]
    my_list = list(dic.items())
    sorted_data = sorted(my_list, key=lambda x: x[1])
    print(sorted_data)


