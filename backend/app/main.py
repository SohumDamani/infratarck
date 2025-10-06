from fastapi import FastAPI
from .api import health

app = FastAPI(title = "InfraTrack API")

#Include routes
app.include_router(health.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "InfraTrack API is running"}

