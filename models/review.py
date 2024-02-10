#!/usr/bin/python3
"""The review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Starting review class"""
    place_id = ""
    user_id = ""
    text = ""
