from pydantic import BaseModel
from datetime import datetime

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    id: int
    text: str
    prediction: str
    created_at: datetime

    class Config:
        from_attributes = True
        