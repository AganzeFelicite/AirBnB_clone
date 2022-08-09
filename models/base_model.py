#!/usr/bin/env python5
""""
this is the base model it creates  the class of 
Basemodel(): 
    to create an object
"""

import uuid
import models
from datetime import datetime
'''this is the base module'''


class BaseModel:
    '''this is the basemodel class in this module'''
    def __init__(self, *args, **kwargs):
        """
        initialisation of instance attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())  # to assign a unique id
            self.created_at = datetime.now()  # to store the time
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
        else:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.fromisoformat(val)
                elif key != "__class__":
                    self.__dict__[key] = val

    def __str__(self) -> str:
        '''this returns [class name] (id) <all the methods of the class'''
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """this is a method to set the updated_at method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """this a function to print a dictionary containing __dic__"""
        r = dict()
        for key, val in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                r[key] = val.isoformat()
            else:
                r[key] = val
        r["__class__"] = self.__class__.__name__
        return r
