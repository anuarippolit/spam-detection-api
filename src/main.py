from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List 

from .database import engine, Base, get_db
# 1. Import your models module explicitly here so it binds to Base
from . import models 
from .schemas import PredictionRequest, PredictionResponse
from .predictor import predictor

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 2. Fire the table creation on the fully registered Base metadata object
    Base.metadata.create_all(bind=engine)
    yield  
    pass

app = FastAPI(
    title="SMS Spam Detection API",
    description="A production-ready API that classifies text messages as Spam or Ham and logs requests to PostgreSQL.",
    version="1.0.0",
    lifespan=lifespan # Make sure your lifespan manager is explicitly assigned here!
)

@app.get("/health", tags=["Utility"])
def health_check():
    return {"status": "healthy", "model_loaded": predictor.model is not None}

@app.post("/predict", response_model=PredictionResponse, tags=["ML Inference"])
def predict_text(payload: PredictionRequest, db: Session = Depends(get_db)):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text payload cannot be empty.")
    try:
        # make a prediction 
        label_prediction = predictor.predict(payload.text)

        # create a model object to save it into db
        # Use models.PredictionRecord since we imported the module
        db_record = models.PredictionRecord(
            text=payload.text,
            prediction=label_prediction
        )

        # save it into db
        db.add(db_record)
        db.commit()
        db.refresh(db_record)

        return db_record 

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Inference Engine Error: {str(e)}")

@app.get("/history", response_model=List[PredictionResponse], tags=["Database Log"])
def get_history(limit: int=10, db: Session = Depends(get_db)):
    # Use models.PredictionRecord here as well
    records = db.query(models.PredictionRecord).order_by(models.PredictionRecord.id.desc()).limit(limit).all()
    return records