#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     primary_key=True),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True))
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        reviews = relationship("Review", backref="places",
                               cascade="all, delete, delete-orphan")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ return all the places"""
            list_place = []
            for vplace in models.storage.all('Place').values():
                if(vplace.place_id == self.id):
                    list_place.append(vplace)
            return list_place

        @property
        def cities(self):
            """cities with relation to state"""
            list_city = []
            for cty in models.storage.all(models.review).values():
                if(cty.place_id == self.id):
                    list_city.append(cty)
            return list_city

        @property
        def amenities(self):
            my_atr_amenity = []
            for amty in self.amenity_ids:
                if self.id == amty.id:
                    my_atr_amenity.append(amty)
            return my_atr_amenity

        @amenities.setter
        def amenities(self, amenity):
            if type(amenity).__name__ == 'Amenity':
                self.amenity_ids.append(amenity)
