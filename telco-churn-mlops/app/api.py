from fastapi import FastAPI
import joblib
import pandas as pd
import os
import sys

# Hacer que el directorio del script esté en sys.path para importar schemas.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schemas import CustomerData  # ahora sí funciona

# El resto del código se mantiene igual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.joblib")

app = FastAPI()
model = joblib.load(model_path)

@app.post("/predict")
def predict(data: CustomerData):
    input_df = pd.DataFrame([data.model_dump()])
    proba = model.predict_proba(input_df)[0, 1]
    pred_label = "Yes" if proba > 0.5 else "No"
    return {"churn_probability": float(proba), "prediction": pred_label}