from data_loader import load_matches, clean_matches
from features import build_features

def main():
    df = load_matches()
    df = clean_matches(df)
    df = build_features(df)

    print("Dataset listo para ML")
    print(df.head())

if __name__ == "__main__":
    main()
