#!/usr/bin/python3
"""
base_model
"""
from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """ Represents the base model for objects in the hbnb project """

    def __init__(self, *args, **kwargs):
        """ initializes new instance of BaseModel """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                """ if k == "__class__":
                    pass
                el
                """
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns string representation of the BaseModel """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """  returns a dictionary containing all keys/values of
             __dict__ of the instance """
        my_dict_copy = self.__dict__.copy()
        my_dict_copy["created_at"] = self.created_at.isoformat()
        my_dict_copy["updated_at"] = self.updated_at.isoformat()
        my_dict_copy["__class__"] = self.__class__.__name__
        return my_dict_copy
