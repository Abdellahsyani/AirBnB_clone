#!/usr/bin/python3
"""Test module city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """Test city class"""
    def test_attribut(self):
        """test attr"""
        self.assertTrue(City.name == '')
        self.assertTrue(City.state_id == '')

    def test_inhertance(self):
        """Test city inhert"""
        self.assertTrue(
                issubclass(City, BaseModel)
                and City is not BaseModel)

if __name__ == "__main__":
    unittest.main()
