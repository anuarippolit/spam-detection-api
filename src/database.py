from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings

DATABASE_URL = settings.DATABASE_URL

# create connection with db on server
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# create a session with db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create ORM base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()