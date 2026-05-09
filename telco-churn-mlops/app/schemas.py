from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    SeniorCitizen: int = Field(..., ge=0, le=1, description="1 si es adulto mayor, 0 si no")
    MonthlyCharges: float = Field(..., gt=0, description="Cargo mensual en USD")
    TotalCharges: float = Field(..., ge=0, description="Cargo total acumulado en USD")
    Contract: str = Field(..., description="Month-to-month, One year, Two year")
    PaymentMethod: str = Field(..., description="Método de pago del cliente")

    class Config:
        json_schema_extra = {
            "example": {
                "SeniorCitizen": 0,
                "MonthlyCharges": 65.5,
                "TotalCharges": 1200.0,
                "Contract": "Month-to-month",
                "PaymentMethod": "Electronic check",
            }
        }
