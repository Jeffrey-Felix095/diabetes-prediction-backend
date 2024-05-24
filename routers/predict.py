import pandas as pd

from fastapi import APIRouter, HTTPException
from schemas import Features, Prediction
from actions import load_models


models = load_models()
router = APIRouter()

@router.post("/predict", response_model=Prediction)
def predict(features: Features):

    print(Features)

    try:
        # Validar los datos de entrada
        if not isinstance(features, Features):
            raise HTTPException(status_code=400, detail="Los datos de entrada no son válidos")
        
        # Convertir los datos en un DataFrame de pandas
        data = pd.DataFrame([features.model_dump()])

        random_forest_model = models["random_forest_model"]["model"]

        # Realizar la predicción
        prediction = random_forest_model.predict(data)

        # Retornar la predicción en formato JSON
        return {
            "diabetes_prediction": int(prediction[0]),
            "random_forest_prediction": int(prediction[0])
        }

    except Exception as e:
        # Manejar cualquier excepción y retornar un error HTTP 500
        raise HTTPException(
            status_code=500,
            detail="Ocurrió un error al procesar la solicitud"
        )

