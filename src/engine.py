from sqlalchemy import create_engine
from .models import Base

engine = create_engine("sqlite:///src/data/database.db", echo=False)
Base.metadata.create_all(engine)