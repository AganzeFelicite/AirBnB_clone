#!/usr/bin/env python3
from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
"""this is the test module for testing the baseclass"""
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__
class TestBaseModel(unittest.TestCase):
    """this is the test case for the basemodel class"""
    def setUp(self):
        self.one = BaseModel()
        
        

    def test_if_id_is_string(self):
        self.assertEqual(type(self.one.id).__name__, "str")

    def test_if_id_is_not_none(self):
        self.assertIsNotNone(self.one.id,msg="is not None")
    
    def test_if__str__returns_str(self):
        self.assertEqual(type(self.one.__str__()).__name__, "str")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,"base_model.py needs a docstring")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    '''def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.one:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
              )'''



if __name__ == "__main__":
    unittest.main()
