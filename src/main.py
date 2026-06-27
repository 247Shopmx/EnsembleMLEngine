import json

def load_config():
    with open("../config/config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    print("Sistema Football AI iniciado")
    print("Modelo activo:", config["models"])

if __name__ == "__main__":
    main()
