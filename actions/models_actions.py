import joblib
from . import download_blod

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

            try:
                model["model"] = joblib.load(file_path) 
            except FileNotFoundError:
                print(f"Model file {model['blob_name']} not found, downloading it from blob storage.")
                download_blod(model['blob_name'])
                print("Model file has been downloaded")
                
                model["model"] = joblib.load(file_path) 

    return models