#!/usr/bin/env python3
from datetime import datetime
import unittest
from models.base_model import BaseModel
"""this is the test module for testing the baseclass"""


class TestBaseModel(unittest.TestCase):
    """this is the test case for the basemodel class"""
    def setUp(self):
        self.one = BaseModel()
        self.one.save()

    def test_if_id_is_string(self):
        self.assertEqual(type(self.one.id).__name__, "str")

    def test_if_id_is_not_none(self):
        self.assertIsNotNone(self.one.id,msg="is not None")
    
    def test_if__str__returns_str(self):
        self.assertEqual(type(self.one.__str__()).__name__, "str")



if __name__ == "__main__":
    unittest.main()
