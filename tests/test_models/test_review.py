#!/usr/bin/python3
"""Test review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review instances."""
    def test_attributes(self):
        """test attr"""
        self.assertTrue(Review.text == '')
        self.assertTrue(Review.place_id == '')
        self.assertTrue(Review.user_id == "")

    def test_inheritance(self):
        """Test inhert"""
        self.assertTrue(issubclass(Review, BaseModel)
                and Review is not BaseModel)


if __name__ == "___main__":
    unittest.main()
