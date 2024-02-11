#!/usr/bin/python3
"""Test cases file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    """Test cases of file_storage class"""

    def test_filepath(self):
        """Test path file.json"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str),
                        "__file_path is string")
        self.assertTrue(FileStorage._FileStorage__file_path.endswith('.json'),
                        "__file_path exten is .json")

    def test_objects(self):
        """test objects"""
        self.assertTrue(
            isinstance(FileStorage._FileStorage__objects, dict),
            "that is a dictionary"
                )


class Test_FileStorageInstance(unittest.TestCase):
    """Test all instance isinde the FileStorage class"""
    def setUp(self):
        """set instance to test"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """tearDown attributes"""
        del self.storage

    def test_all(self):
        """test all method"""
        self.assertTrue(
                isinstance(self.storage.all(), dict),
                "storage.all() return dictionary")

    def test_new(self):
        """test new method"""
        length_1 = len(self.storage.all())
        v1 = BaseModel()
        self.storage.new(v1)
        length_2 = len(self.storage.all())
        self.assertTrue(
                length_2 == length_1 + 1,
                "that is not add to __object")
        v1_storage = self.storage.all()[f'BaseModel.{v1.id}']
        self.assertTrue(
                v1_storage is v1,
                "storage.new() is add the object as it is in __objects")

    def test_reload(self):
        """test the reload method"""
        v1 = BaseModel()
        self.storage.new(v1)
        self.storage.save()
        self.storage.reload()
        v1_rep = FileStorage._FileStorage__objects[f"BaseModel.{v1.id}"]
        self.assertTrue(isinstance(
            v1_rep, BaseModel),
            "reload objects it was a class")
        self.assertTrue(v1_rep.to_dict() == v1.to_dict())
        v1.name = "My model"
        self.assertFalse(v1_rep.to_dict() == v1.to_dict())


if __name__ == "__main__":
    unittest.main()
