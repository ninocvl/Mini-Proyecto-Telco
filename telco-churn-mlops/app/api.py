from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("app/model.joblib")

class CustomerData(BaseModel):
    SeniorCitizen: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str  # "Month-to-month", "One year", etc.
    PaymentMethod: str  # "Electronic check", "Credit card", etc.

@app.post("/predict")
def predict(data: CustomerData):
    # Preprocesamiento en memoria (ejemplo simplificado)
    features = np.array([
        data.SeniorCitizen,
        data.MonthlyCharges,
        data.TotalCharges,
        1 if data.Contract == "Month-to-month" else 0,
        1 if data.PaymentMethod == "Electronic check" else 0
    ]).reshape(1, -1)
    
    prediction = model.predict_proba(features)[0][1]  # Probabilidad de churn
    return {"churn_probability": float(prediction), "prediction": int(prediction > 0.5)}