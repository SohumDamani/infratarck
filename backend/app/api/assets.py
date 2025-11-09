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

# Update an existing asset (PUT method)
@router.put("/assets/{id}", response_model=AssetRead)
def update_asset(id: int, payload: AssetCreate, db: Session = Depends(get_db)):
    # Find the asset by id
    asset_to_update = db.query(Asset).filter(Asset.id == id).first()

    if not asset_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found"
        )

    # Update the asset fields
    asset_to_update.name = payload.name
    asset_to_update.category = payload.category
    asset_to_update.price = payload.price
    asset_to_update.quantity = payload.quantity

    # Commit changes
    db.commit()
    db.refresh(asset_to_update)

    return asset_to_update 

# Get a single asset by ID (GET method)
@router.get("/assets/{id}", response_model=AssetRead)
def get_asset_by_id(id: int, db: Session = Depends(get_db)):
    # Find the asset by id
    asset = db.query(Asset).filter(Asset.id == id).first()

    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found"
        )

    return asset

# Delete an asset (DELETE method)
@router.delete("/assets/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset(id: int, db: Session = Depends(get_db)):
    # Find the asset by id
    #.first() is still neded even toh id is unique to return one object or None.
    asset_to_delete = db.query(Asset).filter(Asset.id == id).first()

    if not asset_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found"
        )

    db.delete(asset_to_delete)
    db.commit()

    # Return nothing, but HTTP 204 will signal success
    return None