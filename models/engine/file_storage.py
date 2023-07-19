#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
            all or only element of specified class
            """
        # OLD CODE
        # if cls is None:
        #     return FileStorage.__objects
        # else:
        #     dict_all = {}
        #     if cls is not str:
        #         # select only name of class
        #         cls = cls.__name__
        #     for key, value in FileStorage.__objects.items():
        #         if cls in key:
        #             dict_all.update({key: value})
        #     return (dict_all)

        dict_all = {}
        if cls is None:
            return FileStorage.__objects
        else:
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    dict_all[key] = value
            return dict_all

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # if obj is not None:
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
            method to delete objects of specific class
        """
        try:
            # construct identifiant object : class_name.id_obj
            value = "{}.{}".format(obj.__class__.__name__, obj.id)
            # delete object del method
            del self.__objects[value]
            self.save()
        except Exception:
            pass

    def close(self):
        """ self explanatory """

        self.reload()
