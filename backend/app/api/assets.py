from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.models import Asset
from .schemas import AssetCreate, AssetRead

# Initialize APIRouter for asset-related endpoints
router = APIRouter()

# Create a new asset (POST method)
@router.post("/assets/")
def create_asset(payload: AssetCreate, db: Session = Depends(get_db)):
    # to avoid accidential addition of the same assets twice
    existing_asset = db.query(Asset).filter(Asset.name == payload.name, Asset.category == payload.category).first()
    if existing_asset:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Asset already exists"
        )
    new_asset = Asset(name=payload.name, category=payload.category, price=payload.price, quantity=payload.quantity)
    db.add(new_asset)  # Add to the session
    db.commit()
    print(f"Committing asset: {new_asset}")  # Commit the transaction to the database
    db.refresh(new_asset)  # Refresh to get the new asset (e.g., its ID)
    return new_asset  # Return the created asset

# Get all assets (GET method)
@router.get("/assets/")
def get_assets(db: Session = Depends(get_db)):
    assets = db.query(Asset).all()  # Query all assets in the database
    return assets  # Return the list of assets
