#!/usr/bin/env python3

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
        if kwargs == {}:
            self.id = str(uuid.uuid4())  # to assign a unique id
            self.created_at = datetime.now()  # to store the time
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save(self)
        else:
            for key, val in kwargs.items():
                if key == "__class__":
                    pass
                elif key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.fromisoformat(val)
                else:
                    self.__dict__[key] = val

    def __str__(self) -> str:
        '''this returns [class name] (id) <all the methods of the class'''
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return f'{[a]} {b} {c}'

    def save(self):
        """this is a method to set the updated_at method"""
        self.updated_at = datetime.now()
        models.storage.save(self)

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
