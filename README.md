# Predicción de Churn en Telecomunicaciones — Proyecto MLOps End-to-End

[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7.svg)](https://render.com)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square)
![Gradio](https://img.shields.io/badge/Gradio-4.x-orange?style=flat-square)

## Descripción del Proyecto

Este proyecto implementa un flujo completo de MLOps para la predicción de abandono de clientes (churn) en una empresa de telecomunicaciones. Utilizando el dataset [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn) de Kaggle (~7,000 registros), se desarrolló, entrenó y desplegó un modelo de clasificación binaria siguiendo las mejores prácticas de la industria.

El proyecto abarca desde el análisis exploratorio de datos (EDA) y el entrenamiento seguro con Pipelines de Scikit-learn, hasta el despliegue en producción con FastAPI, Docker, CI/CD con GitHub Actions e interpretabilidad con LIME.

## Demo en Vivo

| Componente | URL | Descripción |
|---|---|---|
| Frontend (Gradio) | [telco-churn-front.onrender.com](https://telco-churn-front.onrender.com) | Interfaz interactiva para probar el modelo |
| API (FastAPI) | [telco-churn-api-sseb.onrender.com/docs](https://telco-churn-api-sseb.onrender.com/docs) | Documentación Swagger de la API REST |
| API Endpoint | [telco-churn-api-sseb.onrender.com/predict](https://telco-churn-api-sseb.onrender.com/predict) | Endpoint POST para predicciones |

> **Nota sobre el plan gratuito de Render:** La primera predicción puede tardar entre 30 y 60 segundos debido al *cold start*. Las siguientes son instantáneas.


## Arquitectura del Proyecto

```
telco-churn-mlops/
├── data/                        # Dataset original y archivos procesados
├── notebooks/
│   ├── 1_eda_preprocessing.ipynb   # Análisis exploratorio y limpieza
│   ├── 2_model_training.ipynb      # Entrenamiento, GridSearchCV, evaluación
│   └── 3_interpretability.ipynb    # Explicabilidad con LIME
├── app/
│   ├── api.py                   # FastAPI — servicio de inferencia
│   ├── schemas.py               # Modelos Pydantic
│   └── model.joblib             # Pipeline entrenado
├── frontend/
│   ├── app.py                   # Interfaz Gradio
│   ├── Dockerfile               # Imagen del frontend
│   └── requirements.txt
├── tests/
│   ├── test_api.py              # Pruebas unitarias de la API
│   └── test_model.py            # Validación del modelo
├── Dockerfile                   # Imagen de la API
├── requirements.txt
├── myst.yml

```