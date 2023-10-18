def openFileArray(file):
    doc = open(f'documents/{file}', 'r')
    aaa = doc.readline()
    lstSpecialValueOct15=eval(aaa)
    doc.close()
    return lstSpecialValueOct15

if __name__ == '__main__':
    BestPercentNumOct14 = openFileArray('bestPercentOct14.txt')
    specialValueOct15 = openFileArray('lstSpecialValueOct15.txt')
    specialValueSTOCHRSIOct18 = openFileArray('lstSpecialValueSTOCHRSIOct18.txt')
    ALllist = specialValueSTOCHRSIOct18 
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


