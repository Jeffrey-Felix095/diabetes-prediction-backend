import os
import joblib

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

BLOB_CONNECTION_STRING = os.getenv('BLOB_CONNECTION_STRING')
if not BLOB_CONNECTION_STRING:
    raise ValueError("No BLOB_CONNECTION_STRING found in environment variables")

CONTAINER_NAME = "models"

def download_blod(blob_name: str) -> str:
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    file_path = f"ml_models/{blob_name}"
    
    with open(file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    
    return download_file 


models = {
    # "xavier": {
    #     "blob_name": "xavier-xavier.jpg"
    # },
    # "random_forest_model": {
    #     "blob_name": "Random Forest (Tuned)_model.pkl"
    # },
    "decision_tree_model": {
        "file_path": "Decision Tree (Tuned)_model.pkl"
    },
    # "knn_model": {
    #     "blob_name": "K-Nearest Neighbors (Tuned)_model.pkl"
    # }
}


for model in models.values():    
    blod_name = model['file_path']
    file_path = f"ml_models/{model['file_path']}"
    
    try:
        model["model"] = joblib.load(file_path) 
    except FileNotFoundError:
        print(f"Model file {model['path']} not found. Downloading from blod storage.")
        download_blod(blod_name)
