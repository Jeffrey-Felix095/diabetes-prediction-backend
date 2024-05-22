from fastapi import APIRouter
from schemas.schemas import Features, Prediction
import pandas as pd
from models.rf_model import model


router = APIRouter()

@router.post("/predict", response_model=Prediction)
def predict(features: Features):

    data = pd.DataFrame([features.dict()])
    prediction = model.predict(data)
    return {"diabetes_prediction": int(prediction[0])}
