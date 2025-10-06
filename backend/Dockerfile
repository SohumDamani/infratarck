# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
