from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables

load_dotenv()

DatabaseURL = os.getenv("DATABASE_URL")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST", "db")   # default = 'db' (service name)
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
# Load environment variables
engine = create_engine(os.getenv("DATABASE_URL"))

# Load environment variables
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()