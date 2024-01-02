
import matplotlib as plt
from ta.volume import MFIIndicator
from SpecialFunctions import formatDataset
import numpy as np

def get_MFI(data, window):
    MFIind = MFIIndicator(data['high'], data['low'], data['close'], data['volume'], window)
    return MFIind.money_flow_index()
def getData():
    # calltimes30('BTCUSDT')
    df = eval(open('documents/BTCData.txt', 'r').read())
    df = formatDataset(df[len(df)-40000:len(df)-17500])
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    for column in columns_to_convert:
        df[column] = df[column].apply(float)
    global dfIndex
    dfIndex = df.index[0]
    return df

df = getData()
mfi48 = get_MFI(df, 50)
NPmfi48 = np.array(mfi48)

plt.plot(NPmfi48)
plt.show()