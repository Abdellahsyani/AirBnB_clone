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
        return (FileStorage.__objects)

    def new(self, obj):
        """sets __objeccts to obj with id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to file JSON"""
        json_dict = FileStorage.__objects.copy()
        for key, value in json_dict.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(json_dict, fp, indent=4)

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
        try:
            with open(FileStorage.__file_path, 'r') as fp:
                reading = fp.read()
                if reading.strip():
                    FileStorage.__objects = json.loads(reading)
                    for key, value in FileStorage.__objects.items():
                        FileStorage.__objects[key] = \
                                classes[value['__class__']](**value)
        except FileNotFoundError:
            FileStorage.__objects = {}
