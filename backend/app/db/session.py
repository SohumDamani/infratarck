from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load the database URL from environment variable (set in docker-compose.yml)
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine (talks to PostgreSQL)
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models (this is the declarative_base we discussed)
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    """
    Creates a new SQLAlchemy session for each request,
    ensures it's closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
