#!/usr/bin/python3
"""Define a FileStorage class"""
import json
import os


class FileStorage():
    """Starting the class with define private class attribut"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets __objeccts to obj with id"""
        key = "{}.{}".format(obj.__class__.__name__ , obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objects to file JSON"""
        with open(FileStorage.__file_path, 'w') as fp:
            fp.write(json.dumps(FileStorage.__objects, indent=4))

    def reload(self):
        """deserializes the JSON file to objects if file_path exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "City": City,
                "Place": Place,
                "State": State,
                "Review": Review,
                "Amenity": Amenity
                }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                FileStorage.__objects = json.loads(fp.read())
