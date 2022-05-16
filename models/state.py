#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="states",
                              cascade="all, delete, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """ return all the cities"""
            list_city = []
            for vcity in models.storage.all('City').values():
                if(vcity.state_id == self.id):
                    list_city.append(vcity)
            return list_city
