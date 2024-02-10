#!/usr/bin/python3
"""Define a __init__ magic method for the storage engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
