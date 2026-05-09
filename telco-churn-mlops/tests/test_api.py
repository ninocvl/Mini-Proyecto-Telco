import sys
import os

# Ajustar el path ANTES de importar api
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_predict_churn_high_risk():
    """Cliente con perfil de alto riesgo → probabilidad alta y predicción Yes"""
    payload = {
        "gender": "Male",
        "SeniorCitizen": 1,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 118.75,
        "TotalCharges": 18.8,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "prediction" in data
    assert data["prediction"] in ["Yes", "No"]
    assert 0.0 <= data["churn_probability"] <= 1.0
    assert data["churn_probability"] > 0.5


def test_predict_low_risk():
    """Cliente fidelizado de bajo riesgo → probabilidad baja y predicción No"""
    payload = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 72,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Two year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Bank transfer (automatic)",
        "MonthlyCharges": 25.0,
        "TotalCharges": 5000.0,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in ["Yes", "No"]
    assert 0.0 <= data["churn_probability"] <= 1.0
    assert data["churn_probability"] < 0.5


def test_predict_missing_field():
    """Falta un campo obligatorio → error 422"""
    payload = {"SeniorCitizen": 1}  # incompleto
    response = client.post("/predict", json=payload)
    assert response.status_code == 422