
from . import download_blod

models = {
    "xavier": {
        "blob_name": "xavier-xavier.jpg"
    }
}

def load_models():
    global models 

    for model in models.values():
        if model.get("model") == None:
            file_path, download_file = download_blod(model["blob_name"])
            model["file_path"] = file_path
            model["download_file"] = download_file            

    return models