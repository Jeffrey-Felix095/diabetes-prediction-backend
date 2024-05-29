import joblib

models = {
    # "xavier": {
    #     "file_path": "xavier-xavier.jpg"
    # },
    "random_forest_model": {
        "file_path": "Random Forest (Tuned)_model.pkl"
    },
    # "decision_tree_model": {
    #     "file_path": "Decision Tree (Tuned)_model.pkl"
    # },
    # "knn_model": {
    #     "file_path": "K-Nearest Neighbors (Tuned)_model.pkl"
    # }
}

def load_models():
    global models 

    for model in models.values():
        if model.get("model") == None:
            file_path = f"ml_models/{model['file_path']}"

            try:
                model["model"] = joblib.load(file_path) 
            except FileNotFoundError:
                print(f"Model file {model['file_path']} not found")
                model["model"] = joblib.load(file_path) 

    return models