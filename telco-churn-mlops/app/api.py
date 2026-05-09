import sys
import os

# Ajuste de path DEBE ir antes de los imports locales
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI  # noqa: E402
import joblib  # noqa: E402
import pandas as pd  # noqa: E402
from schemas import CustomerData  # noqa: E402

# Ruta absoluta al directorio del script para cargar el modelo
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