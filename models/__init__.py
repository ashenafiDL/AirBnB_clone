#!/usr/bin/python3
"""
initialization file for module models
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
