
def openFileArray(file):
    doc = open(f'documents/special/{file}.txt', 'r')
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

    BestPercentNumOct14 = openFileArray("bestPercentOct14")
    specialValueOct15 = openFileArray('lstSpecialValueOct15')
    specialValueSTOCHRSIOct18 = openFileArray('lstSpecialValueSTOCHRSIOct18')
    specialValueOct20 = openFileArray('lstSpecialValyueOct20')
    stochSpeicalValueOct23 = openFileArray('stochSpecialNumOct23')
    stochRSISpeicalValueOct23 = openFileArray('stochRSISpecialNumOct23')
    bestStochRSIOct25 = openFileArray('bestStochRSIOct25')
    bestSTOCHRSIOct28 = openFileArray('bestStochRSIOct28')
    bestSTOCHRSIOptimizdNov5 = openFileArray('stochRSISpecialNumNov5')
    bestSTOCHRSInormalNov6 = openFileArray('SRSINNov6')
    lstSpecialNov9OptV2 = openFileArray("lstSpecialNov9OptV2")
    ALllist = lstSpecialNov9OptV2 
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


