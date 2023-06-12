#!/usr/bin/python3
""" 
Question 9
"""
from models.base_model import BaseModel

class User(BaseModel):
  email = ""
  password = ""
  first_name = ""
  last_name = ""
