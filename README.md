# SMS Spam Detection API 

A production-ready, containerized FastAPI microservice that classifies SMS text messages as **Spam** or **Ham** using a pre-trained Machine Learning model (scikit-learn) and automatically logs all inference history to a PostgreSQL database.

---

## 🏗️ Architecture & Stack

- **Framework:** FastAPI (Python 3.13) 
- **Database Layer:** PostgreSQL 15 managed seamlessly through SQLAlchemy ORM sessions.
- **Machine Learning Engine:** Static serialized pipelines (`CountVectorizer` + Classification Model) bundled natively and loaded via `joblib`.
- **Infrastructure:** Multi-container orchestration fully decoupled using Docker and Docker Compose.

---

## ⚡ Quick Start (Local Run via Docker Compose)

Thanks to Docker orchestration, you don't need to install Python, PostgreSQL, or any ML frameworks on your host machine. You can boot the entire infrastructure with a single command block.

### 1. Clone the Repository
```bash
git clone [https://github.com/anuarippolit/spam-detection-api.git](https://github.com/anuarippolit/spam-detection-api.git)
cd spam-detection-api
```

### 2. Create .env file with enviornmental variables. 

Example in .env.example

### 3. Build the system and launch 

```bash
docker compose up --build
```

---

## ⚙️ Project Structure

```text
spam-detection-api/
├── models/                  # Serialized ML artifacts (.pkl)
│   ├── model.pkl
│   └── vectorizer.pkl
├── src/                     # Application Source Code
│   ├── config.py            # Pydantic Settings environment parsing
│   ├── database.py          # SQLAlchemy Engine & session pool lifecycle
│   ├── main.py              # FastAPI Application & Endpoints
│   ├── models.py            # Database tables schema definition
│   ├── predictor.py         # Thread-safe ML model inference layer
│   └── schemas.py           # Pydantic data validation contracts
├── .dockerignore            # Build asset caching exclusions
├── .gitignore               # Version control ignore definitions
├── Dockerfile               # Single container blueprint
├── docker-compose.yml       # Production environment network orchestrator
├── requirements.txt         # Pre-compiled application dependencies
└── README.md                # Documentation

