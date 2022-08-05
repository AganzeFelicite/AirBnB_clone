import uuid
from datetime import datetime
'''this is the base module'''


class BaseModel:
    '''this is the basemodel class in this module'''
    def __init__(self):
        self.id = str(uuid.uuid4())  # to assign a unique id for each class instance
        self.created_at = datetime.now()  # to store the time created
        self.updated_at = None

    def __str__(self):
        '''this returns [class name] (id) <all the methods of the class'''
        return ("[{}] {} {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """this is an instance method to update the update_at
           attribute every time and date
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """this a function to print a dictionary containing __dic__"""
        r = {key:self.__dict__[key] for key in self.__dict__}
        r["__class__"] = type(self).__name__
        r["created_at"] = self.created_at.isoformat()
        r["updated_at"] = self.updated_at.isoformat()
        return r
