def build_features(df):
    df["goal_diff"] = df["home_goals"] - df["away_goals"]
    df["total_goals"] = df["home_goals"] + df["away_goals"]

    df["btts"] = ((df["home_goals"] > 0) & (df["away_goals"] > 0)).astype(int)

    return df
