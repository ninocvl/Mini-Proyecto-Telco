from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    gender: str = Field(..., description="Género del cliente: Male o Female")
    SeniorCitizen: int = Field(..., ge=0, le=1, description="1 si es adulto mayor, 0 si no")
    Partner: str = Field(..., description="Tiene pareja: Yes o No")
    Dependents: str = Field(..., description="Tiene dependientes: Yes o No")
    tenure: int = Field(..., ge=0, description="Meses de antigüedad en la compañía")
    PhoneService: str = Field(..., description="Tiene servicio telefónico: Yes o No")
    MultipleLines: str = Field(..., description="Líneas múltiples: Yes, No o No phone service")
    InternetService: str = Field(..., description="Proveedor de internet: DSL, Fiber optic o No")
    OnlineSecurity: str = Field(..., description="Seguridad en línea: Yes, No o No internet service")
    OnlineBackup: str = Field(..., description="Respaldo en línea: Yes, No o No internet service")
    DeviceProtection: str = Field(..., description="Protección de dispositivo: Yes, No o No internet service")
    TechSupport: str = Field(..., description="Soporte técnico: Yes, No o No internet service")
    StreamingTV: str = Field(..., description="TV por streaming: Yes, No o No internet service")
    StreamingMovies: str = Field(..., description="Películas por streaming: Yes, No o No internet service")
    Contract: str = Field(..., description="Tipo de contrato: Month-to-month, One year o Two year")
    PaperlessBilling: str = Field(..., description="Facturación electrónica: Yes o No")
    PaymentMethod: str = Field(
        ...,
        description="Método de pago: Electronic check, Mailed check, Bank transfer (automatic) o Credit card (automatic)",
    )
    MonthlyCharges: float = Field(..., gt=0, description="Cargo mensual en USD")
    TotalCharges: float = Field(..., ge=0, description="Cargo total acumulado en USD")

    class Config:
        json_schema_extra = {
            "example": {
                "gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 1,
                "PhoneService": "No",
                "MultipleLines": "No phone service",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 29.85,
                "TotalCharges": 29.85,
            }
        }