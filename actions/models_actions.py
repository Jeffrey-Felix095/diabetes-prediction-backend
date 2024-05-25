import joblib

models = {
    # "xavier": {
    #     "blob_name": "xavier-xavier.jpg"
    # },
    "random_forest_model": {
        "blob_name": "random_forest_model.pkl"
    }
}

def load_models():
    global models 

    for model in models.values():
        if model.get("model") == None:
            file_path = f"ml_models/{model['blob_name']}"
            model["model"] = joblib.load(file_path)     

    return models

def clear_models():
    models.clear()