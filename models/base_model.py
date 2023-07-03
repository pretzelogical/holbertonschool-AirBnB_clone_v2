#!/usr/bin/python3
""" Air BnB Clone Basemodel """

import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()

class BaseModel:
    """ Type class of BaseModel """
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """ Type method initialize """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, timeformat))
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ Type method __str__ """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Type method save """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Type method to_dict """
        rt_dict = self.__dict__.copy()
        rt_dict["created_at"] = self.created_at.isoformat()
        rt_dict["updated_at"] = self.updated_at.isoformat()
        rt_dict["__class__"] = self.__class__.__name__
        return rt_dict
