import pandas as pd
def formatDataset(data):
    df = pd.DataFrame(data)
    df['datetime'] = pd.to_datetime(df['date'])
    df = df.set_index('datetime')
    df = df.drop('date', axis=1)
    return df