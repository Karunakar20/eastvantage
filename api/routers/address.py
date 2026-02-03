from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from core.db.db_config import db_connection
from api.schemas.schemas import AddressSchema,AddressSearchSchema
from api.service.address_service import AddressService
from api.models.address import Address

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.post("/", response_model=AddressSchema, status_code=201)
def create_address(
    address: AddressSchema,
    db: Session = Depends(db_connection)
):
    responce = AddressService(db=db, data=address).createOrUpdate()

    if not responce:
        raise HTTPException(status_code=404, detail="Address not found")

    return responce


@router.put("/{address_id}", response_model=AddressSchema)
def update_address(
    address_id: int,
    address: AddressSchema,
    db: Session = Depends(db_connection)
):
    responce = AddressService(db=db, data=address, address_id=address_id).createOrUpdate()

    if not responce:
        raise HTTPException(status_code=404, detail="Address not found")

    return responce


@router.delete("/{address_id}", status_code=204)
def delete_address(address_id: int,db: Session = Depends(db_connection)):
    responce = AddressService(db=db, data=None, address_id=address_id).deleteAddress()

    if not responce:
        raise HTTPException(status_code=404, detail="Address not found")

    return responce


@router.get("/", response_model=List[AddressSearchSchema])
def get_addresses(
    lat: Optional[float] = Query(None),
    lon: Optional[float] = Query(None),
    distance: Optional[float] = Query(None),
    db: Session = Depends(db_connection)
):
    # Distance-based search
    if lat is not None and lon is not None and distance is not None:
        data = AddressSearchSchema(latitude=lat, longitude=lon, distance=distance)
        return AddressService(db=db, data=data).getAddressesWithiDistance()

    # Get all
    return db.query(Address).all()
