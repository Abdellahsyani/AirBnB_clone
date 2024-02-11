#!/usr/bin/python3
"""module test"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Test instances."""
    def test_attributes(self):
        """test attr"""
        self.assertTrue(Amenity.name == '')

    def test_inheritance(self):
        """Test inhert"""
        self.assertTrue(issubclass(Amenity, BaseModel)
                and Amenity is not BaseModel)


if __name__ == "___main__":
    unittest.main()
