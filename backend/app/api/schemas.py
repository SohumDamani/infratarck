from pydantic import BaseModel, Field
from typing import Optional

class AssetCreate(BaseModel):
    name: str = Field(..., description="Name of the infrastructure asset")
    category: str = Field(..., description="Type or category (e.g., server, router, IoT device)")
    price: float = Field(..., ge=0, description="Monetary value or cost of asset")
    quantity: int = Field(..., ge=0, description="Quantity or count of the asset")

class AssetRead(BaseModel):
    id: int
    name: str
    category: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
