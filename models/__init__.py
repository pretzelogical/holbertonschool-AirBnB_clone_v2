#!/usr/bin/python3
from os import getenv
""" Import FileStorage to handle data
    Import DBStorage to handle database
"""

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
