import joblib

def load_model(path: str):
    # Carga el modelo actualizado
        # Carga el modelo guardado
    modelo = joblib.load(path)

    # Vuelve a guardar el modelo utilizando la versión actual de scikit-learn
    joblib.dump(modelo, path)
    modelo = joblib.load(path)
    return modelo

model = load_model('models/random_forest_model.pkl')