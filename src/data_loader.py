import pandas as pd

def load_matches():
    df = pd.read_csv("../data/matches.csv")
    return df

def clean_matches(df):
    df = df.dropna()

    df["home_win"] = (df["home_goals"] > df["away_goals"]).astype(int)
    df["draw"] = (df["home_goals"] == df["away_goals"]).astype(int)
    df["away_win"] = (df["home_goals"] < df["away_goals"]).astype(int)

    return df
