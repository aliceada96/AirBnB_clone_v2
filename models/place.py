#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
        )
    else:
        @property
        def reviews(self):
            """Returns a list of review instances with place_id equals
            to the current Place.i"""
            from models import storage
            from models.review import Review
    
            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
        
        @property
        def amenities(self):
            """Getter for amenities attribute"""
            from models.amenity import Amenity
            from models import storage
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenities.place_id == self.id:
                    amenities.append(amenity)
            return amenities
        
        @amenities.setter
        def amenities(self, amenity_obj):
            """Setter for amenities attribute"""
            from models.amenity import Amenity
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
    