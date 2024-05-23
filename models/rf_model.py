import joblib

def load_model(path: str):
    modelo = joblib.load(path)
    return modelo

#model = load_model('models/random_forest_model.pkl')