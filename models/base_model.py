#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import datetime
import models
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """class base model"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True,
                    nullable=False)
        created_at = Column(DateTime, default=datetime.datetime.utcnow,
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            if "id" not in kwargs:
                kwargs["id"] = self.id = str(uuid.uuid4())
            if "updated_at" not in kwargs:
                kwargs['updated_at'] = datetime.datetime.now().isoformat()
            updated_at = kwargs['updated_at']
            kwargs['updated_at'] = datetime.datetime.\
                strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f')

            if "created_at" not in kwargs:
                kwargs['created_at'] = datetime.datetime.now().isoformat()
            created_at = kwargs['created_at']
            kwargs['created_at'] = datetime.datetime.\
                strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary
