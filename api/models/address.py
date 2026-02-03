from sqlalchemy import Column, Integer, String, Float
from core.db.database import Base

class Address(Base):

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

    __tablename__ = "addresses"