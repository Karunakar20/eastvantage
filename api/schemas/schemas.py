from pydantic import BaseModel, Field
from typing import Optional

class AddressSchema(BaseModel):
    # id: Optional[int] = None
    street: Optional[str] = Field(None, example="123 Main St")
    city: Optional[str] = Field(None, example="Bangalore")
    state: Optional[str] = Field(None, example="Karnataka")
    country: Optional[str] = Field(None, example="India")

    latitude: Optional[float] = Field(None, ge=-90, le=90, example=12.9716)
    longitude: Optional[float] = Field(None, ge=-180, le=180, example=77.5946)

    class Config:
        from_attributes = True

class AddressSearchSchema(BaseModel):
    id: Optional[int] = None
    street: Optional[str] = Field(None, example="123 Main St")
    city: Optional[str] = Field(None, example="Bangalore")
    state: Optional[str] = Field(None, example="Karnataka")
    country: Optional[str] = Field(None, example="India")

    latitude: Optional[float] = Field(None, ge=-90, le=90, example=12.9716)
    longitude: Optional[float] = Field(None, ge=-180, le=180, example=77.5946)
    distance: Optional[float] = Field(None, example=100)

    class Config:
        from_attributes = True
