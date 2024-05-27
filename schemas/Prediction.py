from pydantic import BaseModel

class Prediction(BaseModel):
    diabetes_prediction: int
    random_forest_prediction: int
    decision_tree_prediction: int
    knn_prediction: int