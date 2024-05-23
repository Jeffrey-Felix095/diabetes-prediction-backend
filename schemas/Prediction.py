from pydantic import BaseModel

class Prediction(BaseModel):
    diabetes_prediction: int