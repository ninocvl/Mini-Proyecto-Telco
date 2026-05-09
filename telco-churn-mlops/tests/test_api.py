from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_churn():
    payload = {
        "SeniorCitizen": 1,
        "MonthlyCharges": 99.9,
        "TotalCharges": 500.0,
        "Contract": "Month-to-month",
        "PaymentMethod": "Electronic check",
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "prediction" in data
    assert data["prediction"] in ["Yes", "No"]
    assert 0.0 <= data["churn_probability"] <= 1.0


def test_predict_no_churn():
    payload = {
        "SeniorCitizen": 0,
        "MonthlyCharges": 20.0,
        "TotalCharges": 5000.0,
        "Contract": "Two year",
        "PaymentMethod": "Bank transfer (automatic)",
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
