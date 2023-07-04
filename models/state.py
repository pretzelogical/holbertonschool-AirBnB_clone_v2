#!/usr/bin/python3
""" Module class state """

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """
    Class States
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states',
                              cascade='all, delete, delete-orphan')
    else:

        @property
        def cities(self):
            st_cities = []
            for city in models.storage.all(City).values():
                if (self.id == city.state_id):
                    st_cities.append(city)
            return st_cities