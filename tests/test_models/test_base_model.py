#!/usr/bin/python3
"""Module unittest"""
import unittest
from models.base_model import BaseModel


class TestBasModel(unittest.TestCase):
    """test The BasModel class"""

    def setUp(self):
        """set up of text"""
        self.v1 = BaseModel()
        self.v2 = BaseModel()

    def treatDown(self):
        """treat down method"""
        del self.v1
        del self.v2

    def test_uid(self):
        """Test uuid model"""
        self.assertTrue(isinstance(self.v1.id, str), "Id is a string")
        self.assertNotEqual(self.v1.id, self.v2.id, "Id is different")

    def test_time(self):
        """Test time """
        self.assertNotEqual(
                self.v1.created_at, self.v2.created_at,
                "Instance is has a different creation time")
        self.assertNotEqual(
                self.v1.updated_at, self.v2.updated_at,
                "Instance has a different updated time")

    def test_str(self):
        """Test __str__"""
        ism = f"[{self.v1.__class__.__name__}]"
        aynaikhsan = f"{ism} ({self.v1.id}) {self.v1.__dict__}"
        self.assertEqual(str(self.v1), aynaikhsan,
                "the output is the same as string")

    def test_save(self):
        """Test save method"""
        self.assertFalse(
                self.v1.updated_at > self.v2.updated_at,
                "First instance is be newer than the second instance")
        self.v1.save()
        self.assertTrue(
                self.v1.updated_at > self.v2.updated_at,
                "Save should update the update time")
    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_dict(self):
        """Test to_dict"""
        obj_dict = self.v1.to_dict()
        self.assertEqual(
                obj_dict['__class__'], self.v1.__class__.__name__,
                "Class names should match")
        self.assertEqual(
                obj_dict['created_at'], self.v1.created_at.isoformat(),
                "Creation times should match")
        self.assertEqual(
                obj_dict['updated_at'], self.v1.updated_at.isoformat(),
                "Update times should match")

    def test_init(self):
        """Test __init__"""
        obj_dict = self.v1.to_dict()
        self.v0 = BaseModel(**obj_dict)
        for key in obj_dict.keys():
            if key not in ['updated_at', 'created_at', '__class__']:
                self.assertEqual(
                        obj_dict[key], self.v0.__dict__[key],
                        f"Values for key '{key}' should match")
                self.assertEqual(
                        type(self.v0.updated_at), type(self.v1.updated_at),
                        "Updated time is an instance of the datetime class")
                self.assertEqual(
                        type(self.v0.created_at), type(self.v1.created_at),
                        "Creation time is an instance of the datetime class")
                self.assertFalse('__class__' in self.v0.__dict__)

if __name__ == "__main__":
    unittest.main()
