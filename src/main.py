from data_loader import load_matches, clean_matches
from features import build_features
from model_xgboost import train_model

def main():
    df = load_matches()
    df = clean_matches(df)
    df = build_features(df)

    print("Dataset listo:", df.shape)

    model = train_model(df)

    print("Modelo entrenado correctamente")

if __name__ == "__main__":
    main()
