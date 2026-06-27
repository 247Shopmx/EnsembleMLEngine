import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, log_loss

def train_model(df):
    features = ["home_goals", "away_goals", "goal_diff", "total_goals", "btts"]

    X = df[features]
    y = df["home_win"]  # simplificado (puedes expandir luego a W/D/L multiclase)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)

    acc = accuracy_score(y_test, preds)
    loss = log_loss(y_test, probs)

    print("Accuracy:", acc)
    print("LogLoss:", loss)

    return model
