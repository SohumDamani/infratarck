from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Step 1: Define Base (to be inherited by all models)
Base = declarative_base()

# Step 2: Define Asset model
class Asset(Base):
    # used to keep track of different cloud infrastructure asstes like servers, VM , Containers
    __tablename__ = "assets"  # This table will be created in the database

    # Step 3: Define columns in the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, index=True)  # Asset name
    category = Column(String)  # Asset category
    price = Column(Float)  # Asset price
    quantity = Column(Integer)  # Asset quantity in stock
