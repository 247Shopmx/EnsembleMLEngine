import pandas as pd

def load_csv(path):
    data = pd.read_csv(path)
    return data

def clean_data(df):
    df = df.dropna()
    return df
