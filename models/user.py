#!/usr/bin/python3
"""
user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
