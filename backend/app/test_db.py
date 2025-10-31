from sqlalchemy import text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from db.session import engine

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("✅ Connected to:", result.scalar())
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
