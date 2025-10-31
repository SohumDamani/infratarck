from session import engine
from models import Base

# This will create all tables in the database that are inherited from Base
Base.metadata.create_all(bind=engine)
