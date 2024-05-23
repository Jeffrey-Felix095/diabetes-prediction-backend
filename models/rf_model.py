import joblib

def load_model(path: str):
    modelo = joblib.load(path)
    return modelo