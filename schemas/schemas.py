from pydantic import BaseModel

class Features(BaseModel):
    HighBP: int
    HighChol: int
    BMI: float
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    HvyAlcoholConsump: int
    GenHlth: int
    MentHlth: int
    PhysHlth: int
    DiffWalk: int
    Age: int
    Education: int
    Income: int

class Prediction(BaseModel):
    diabetes_prediction: int