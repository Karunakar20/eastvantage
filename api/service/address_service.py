from sqlalchemy.orm import Session
from api.models.address import Address
from api.schemas.schemas import AddressSchema
from math import radians, cos, sin, asin, sqrt
from typing import Optional


class AddressService:

    def __init__(
        self,
        db: Session,
        data: Optional[AddressSchema] = None,
        address_id: Optional[int] = None
    ):
        self.db = db
        self.data = data
        self.id = address_id

    def __getAddress(self):
        print("self.id", self.id)
        if not self.id:
            return None
        return self.db.query(Address).filter(Address.id == self.id).first()

    def createOrUpdate(self):
        """
        Create or update an address.
        If ID exists -> update
        Else -> create
        """
        if not self.data:
            raise ValueError("Address data is required")

        if self.id:
            db_address = self.__getAddress()
            print("db_address", db_address)
            if db_address:
                update_data = self.data.model_dump(
                        exclude_unset=True,
                        exclude={"id"}
                    )
                print("update_data", update_data)
                for key, value in update_data.items():
                    setattr(db_address, key, value)

                self.db.commit()
                self.db.refresh(db_address)
                return db_address
        print("-----")
        # Create new
        # Exclude 'id' to ensure database autoincrement usage
        db_address = Address(**self.data.model_dump(exclude={"id"}))
        self.db.add(db_address)
        self.db.commit()
        self.db.refresh(db_address)
        return db_address

    def deleteAddress(self):
        db_address = self.__getAddress()
        print("db_address", db_address)
        if not db_address:
            return False

        self.db.delete(db_address)
        self.db.commit()
        return True

    @staticmethod
    def __calculateDistance(lat1, lon1, lat2, lon2):
        """
        Calculate the great-circle distance (Haversine formula)
        """
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Earth radius in km
        print("-------------------", c * r)
        return c * r

    def getAddressesWithiDistance(self):
        """
        Retrieve addresses within a given distance (km)
        """
        if not self.data:
            raise ValueError("Search data is required")

        if not all([self.data.latitude, self.data.longitude, self.data.distance]):
            raise ValueError("latitude, longitude and distance are required")

        all_addresses = self.db.query(Address).all()
        result = []

        for address in all_addresses:
            dist = self.__calculateDistance(
                self.data.latitude,
                self.data.longitude,
                address.latitude,
                address.longitude
            )

            print(dist, self.data.distance)

            if dist <= self.data.distance:
                result.append(address)

        return result
