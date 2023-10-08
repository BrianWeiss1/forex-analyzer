import pandas as pd
def formatDataset(data):
    df = pd.DataFrame(data)
    df['datetime'] = pd.to_datetime(df['date'])
    df = df.set_index('datetime')
    df = df.drop('date', axis=1)
    return df
def formatDataset1(df):
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    for column in columns_to_convert:
        df[column] = df[column].astype(float)
    return df