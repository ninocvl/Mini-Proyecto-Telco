import joblib
import numpy as np
import pandas as pd
import os
import pytest

# Subir un nivel desde tests/ a telco-churn-mlops/, luego entrar a app/
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "app", "model.joblib")


@pytest.fixture
def model():
    if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) == 0:
        pytest.skip("model.joblib no encontrado — entrena primero el modelo")
    return joblib.load(MODEL_PATH)


def test_model_loads(model):
    assert model is not None


def test_model_predict_proba_shape(model):
    X = pd.DataFrame([{
        "gender": "Female", "SeniorCitizen": 0, "Partner": "Yes",
        "Dependents": "No", "tenure": 24, "PhoneService": "Yes",
        "MultipleLines": "No", "InternetService": "DSL",
        "OnlineSecurity": "Yes", "OnlineBackup": "No",
        "DeviceProtection": "Yes", "TechSupport": "No",
        "StreamingTV": "No", "StreamingMovies": "No",
        "Contract": "One year", "PaperlessBilling": "Yes",
        "PaymentMethod": "Mailed check", "MonthlyCharges": 50.0,
        "TotalCharges": 1200.0
    }])
    proba = model.predict_proba(X)
    assert proba.shape == (1, 2)
    assert 0.0 <= proba[0][0] <= 1.0
    assert 0.0 <= proba[0][1] <= 1.0


def test_model_predict_shape(model):
    X = pd.DataFrame([{
        "gender": "Male", "SeniorCitizen": 1, "Partner": "No",
        "Dependents": "No", "tenure": 1, "PhoneService": "Yes",
        "MultipleLines": "Yes", "InternetService": "Fiber optic",
        "OnlineSecurity": "No", "OnlineBackup": "No",
        "DeviceProtection": "No", "TechSupport": "No",
        "StreamingTV": "Yes", "StreamingMovies": "Yes",
        "Contract": "Month-to-month", "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check", "MonthlyCharges": 100.0,
        "TotalCharges": 100.0
    }])
    pred = model.predict(X)
    assert pred.shape == (1,)
    assert pred[0] in [0, 1]