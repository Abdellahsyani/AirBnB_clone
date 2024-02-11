#!/usr/bin/python3
"""Test module state"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State instances."""
    def test_attributes(self):
        """test attr"""
        self.assertTrue(State.name == '')

    def test_inheritance(self):
        """Test inhert"""
        self.assertTrue(issubclass(State, BaseModel)
                and State is not BaseModel
                                                                )


if __name__ == "___main__":
    unittest.main()
