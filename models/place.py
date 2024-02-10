#!/usr/bin/python3
"""The place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """The place of cities class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
