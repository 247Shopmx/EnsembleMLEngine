from data_loader import load_matches, clean_matches
from features import build_features
from model_xgboost import train_model
from predict import predict_match

def main():
    df = load_matches()
    df = clean_matches(df)
    df = build_features(df)

    model = train_model(df)

    result = predict_match(model, 2, 1)

    print("Predicción ejemplo:", result)

if __name__ == "__main__":
    main()
