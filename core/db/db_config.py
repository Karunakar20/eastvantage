from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.db.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_connection():
     db = SessionLocal()
     try:
          yield db
          
     finally:
          db.close()