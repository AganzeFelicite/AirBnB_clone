#!/usr/bin/python3
"""this is the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """this is the class of the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
