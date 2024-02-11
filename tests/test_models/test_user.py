#!/usr/bin/python3
"""module test"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """start testing"""
    def setUp(self):
        """setUp test"""
        self.v1 = User()
        self.v2 = User()

    def tearDown(self):
        """tearDown test"""
        del self.v1
        del self.v2

    def test_attributes(self):
        """test attr"""
        self.assertTrue(User.email == "")
        self.assertTrue(User.password == "")
        self.assertTrue(User.first_name == "")
        self.assertTrue(User.last_name == "")

    def test_inheritance(self):
        """Test inherits"""
        self.assertTrue(issubclass(User, BaseModel)
                and User is not BaseModel)

        def test_uid(self):
            """test uid"""
        self.assertTrue(isinstance(self.v1.id, str), "uuid is a string")
        self.assertFalse(self.v1.id == self.v2.id, "uuid not the same")

    def test_time(self):
        """test time"""
        self.assertNotEqual(self.v1.created_at, self.v2.created_at,
                "instance can't created time")
        self.assertNotEqual(self.v1.updated_at, self.v2.updated_at,
                "instances can't updated time")

    def test_save(self):
        """test save"""
        self.assertFalse(self.v1.updated_at > self.v2.updated_at,
                "first instance")
        self.v1.save()
        self.assertTrue(self.v1.updated_at > self.v2.updated_at,
                "Save updated time")

    def test_dict(self):
        """test to_dict"""
        dict = self.v1.to_dict()
        self.assertEqual(dict['__class__'], self.v1.__class__.__name__,
                "items is values")
        self.assertEqual(dict['created_at'], self.v1.created_at.isoformat(),
                "Both is same value")
        self.assertEqual(dict['updated_at'], self.v1.updated_at.isoformat(),
                "Both is the same value")

    def test_init(self):
        """test unit"""
        json_dict = self.v1.to_dict()
        self.v0 = User(**json_dict)

        for key in json_dict.keys():
            if key not in ['updated_at', 'created_at', '__class__']:
                self.assertEqual(json_dict[key], self.v0.__dict__[key],
                        f"[{key}] testing")

        self.assertEqual(type(self.v0.updated_at), type(self.v1.updated_at),
                "updat and create are in datetime")
        self.assertEqual(type(self.v0.created_at), type(self.v1.created_at),
                "Updated and created is datetime class")
        self.assertFalse('__class__' in self.v0.__dict__)

if __name__ == "__main__":
    unittest.main()
