FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend/app contents directly into /app
COPY app/ .

# Expose port
EXPOSE 8000

# Run FastAPI (now directly under /app/main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
