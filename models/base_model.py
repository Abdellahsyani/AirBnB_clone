#!/usr/bin/python3
"""Define a BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Start BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize the variable attribut.
        Args:
            *args: The vector who let us add unlimite numbers.
            **kwargs: The dictionary vector
        """
        if kwargs:
            for key in kwargs.keys():
                if key != '__class__':
                    self.__dict__[key] = kwargs[key]
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """define str method and return the class name ..."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the instance attribut"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """return all instance attribut to dictionary"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
