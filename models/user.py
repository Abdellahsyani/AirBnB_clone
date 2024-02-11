#!/usr/bin/python3
"""The User class to craete user instance"""


from models.base_model import BaseModel


class User(BaseModel):
    """Start using the user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
