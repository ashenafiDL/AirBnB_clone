#!/usr/bin/python3
"""
FileStorage
"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represents abstract storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary attribute __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets obj and its id in __objects """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """ serializes __objects to JSON file (path: __file_path) """
        dict_c = FileStorage.__objects
        dicts_i = {obj: dict_c[obj].to_dict() for obj in dict_c.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dicts_i, f)

    def reload(self):
        """Deserializes the JSON file - if it exists - to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                dicts_i = json.load(f)
                for i in dicts_i.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
