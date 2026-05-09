import joblib
import numpy as np
import os
import pytest

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "app", "model.joblib")


@pytest.fixture
def model():
    if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) == 0:
        pytest.skip("model.joblib no encontrado — entrena primero el modelo")
    return joblib.load(MODEL_PATH)


def test_model_loads(model):
    assert model is not None


def test_model_predict_shape(model):
    X = np.array([[1, 99.9, 500.0, 1, 1]])
    pred = model.predict(X)
    assert pred.shape == (1,)


def test_model_predict_proba_range(model):
    X = np.array([[0, 20.0, 5000.0, 0, 0]])
    proba = model.predict_proba(X)
    assert proba.shape == (1, 2)
    assert 0.0 <= proba[0][1] <= 1.0
