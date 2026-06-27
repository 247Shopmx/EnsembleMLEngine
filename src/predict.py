import numpy as np

def predict_match(model, home_goals, away_goals):
    goal_diff = home_goals - away_goals
    total_goals = home_goals + away_goals
    btts = 1 if home_goals > 0 and away_goals > 0 else 0

    X = np.array([[home_goals, away_goals, goal_diff, total_goals, btts]])

    prob = model.predict_proba(X)[0]

    return {
        "away_win": float(prob[0]),
        "home_win": float(prob[1])
    }
