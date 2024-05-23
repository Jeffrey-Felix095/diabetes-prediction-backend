from fastapi import APIRouter, HTTPException
from schemas.schemas import Features, Prediction
import pandas as pd
from models.rf_model import model

router = APIRouter()

@router.post("/predict", response_model=Prediction)
def predict(features: Features):
    try:
        # Validar los datos de entrada
        if not isinstance(features, Features):
            raise HTTPException(status_code=400, detail="Los datos de entrada no son válidos")

        # Convertir los datos en un DataFrame de pandas
        data = pd.DataFrame([features.dict()])

        # Realizar la predicción
        prediction = model.predict(data)

        # Retornar la predicción en formato JSON
        return {"diabetes_prediction": int(prediction[0])}

    except Exception as e:
        # Manejar cualquier excepción y retornar un error HTTP 500
        raise HTTPException(status_code=500, detail="Ocurrió un error al procesar la solicitud")

