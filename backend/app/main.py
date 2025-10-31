from fastapi import FastAPI
from api.health import router as health_router
from api.assets import router as assets_router

app = FastAPI(title = "InfraTrack API")

#Create DB Tablespoons 
#Include routes
app.include_router(health_router, prefix="/api")
app.include_router(assets_router)

@app.get("/")
def root():
    return {"message": "InfraTrack API is running"}

