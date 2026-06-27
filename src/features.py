import pandas as pd

def add_basic_features(df):
    df["goal_diff"] = df["goals_home"] - df["goals_away"]
    return df
