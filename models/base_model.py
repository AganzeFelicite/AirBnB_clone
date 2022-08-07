import uuid
from datetime import datetime, timezone
'''this is the base module'''


class BaseModel:
    '''this is the basemodel class in this module'''
    def __init__(self, *args, **kwargs):
        """
        initialisation of instance attributes
        """
        if kwargs != {}:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
                    
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
         else:
            self.id = str(uuid.uuid4())  # to assign a unique id
            self.created_at = datetime.now()  # to store the time
            self.updated_at = datetime.now() 

    def __str__(self):
        '''this returns [class name] (id) <all the methods of the class'''
        
        return ("[{}] {} {}".format(
            self.__class__.__name__,str(self.id),str(self.__dict__)))


    def save(self):
        """this is an instance method to update the update_at
           attribute every time and date
        """
        self.updated_at = datetime.now()

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
