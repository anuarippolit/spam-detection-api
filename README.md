# Spam Detection API

REST API that classifies SMS messages as spam or ham.
Logs all predictions to PostgreSQL for history tracking.

## Stack

Python · FastAPI · scikit-learn · PostgreSQL · Docker

## Run

git clone https://github.com/anuarippolit/spam-detection-api
cp .env.example .env
docker compose up --build

## API

POST /predict
{"text": "You won a free iPhone! Click here to claim."}
→ {"label": "spam", "confidence": 0.97}

GET /history
→ list of past predictions with timestamps

## Model

CountVectorizer + Logistic Regression trained on SMS Spam Collection dataset.
Serialized with joblib, loaded once at startup.
