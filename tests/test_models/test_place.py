#!/usr/bin/python3
"""Test Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """Test place method"""
    def test_attribute(self):
        """testing attr class"""
        self.assertTrue(Place.name == '')
        self.assertTrue(Place.city_id == '')
        self.assertTrue(Place.user_id == "")
        self.assertTrue(Place.description == "")
        self.assertTrue(Place.number_rooms == 0)
        self.assertTrue(Place.number_bathrooms == 0)
        self.assertTrue(Place.max_guest == 0)
        self.assertTrue(Place.price_by_night == 0)
        self.assertTrue(Place.latitude == 0.0)
        self.assertTrue(Place.longitude == 0.0)
        self.assertTrue(Place.amenity_ids == [])
        self.assertTrue(type(Place.longitude) is float)
        self.assertTrue(type(Place.latitude) is float)
        self.assertTrue(type(Place.amenity_ids) is list)

    def test_inhertince(self):
        """test inhert"""
        self.assertTrue(issubclass(Place, BaseModel)
                and Place is not BaseModel)

if __name__ == "__main__":
    unittest.main()
