#!/usr/bin/env python3
"""this is the file_storage model"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

objts = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
class FileStorage:
    """initialization of private class variable"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        '''this is a public method that returns a dictionary of all objects'''
        return self.__objects

    def new(self, obj):
        """this add elements to the dictionary __objects """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """this is saves the object and
        puts it into a file after doing serialisation
        """
        dicts = {}
        for key in self.__objects:
            dicts[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(dicts, file)

    def reload(self):
        """this will convert the file
        elements from json 
        to python okbjcts
        ie doing the deserialization
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                old_dict = json.load(f)
        
            for key in old_dict:
                self.__objects[key] = objts[old_dict[key]["__class__"]](**old_dict[key])
        except:
            pass
        
