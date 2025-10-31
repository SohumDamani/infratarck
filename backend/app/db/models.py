from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from .session import Base  # ✅ Import Base from session.py

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # Ensure each (name, category) pair is unique
    __table_args__ = (UniqueConstraint("name", "category", name="_name_category_uc"),)
