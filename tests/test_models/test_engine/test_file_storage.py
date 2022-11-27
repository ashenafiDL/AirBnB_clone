#!/usr/bin/python3
"""
Test file for the `file_storage` module
"""
import os
import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorageInstantiation(unittest.TestCase):
    """Test instantiation of `FileStorage` object"""

    def test_type(self):
        """Test if it is an instance of FileStorage class
        """
        fs = FileStorage()
        self.assertIsInstance(fs,  FileStorage)

    def test_object_type(self):
        """Test if it is an instance of FileStorage class
        """
        self.assertIsInstance(storage, FileStorage)

    def test_private_file_path(self):
        """Test for private variables
        """
        with self.assertRaises(AttributeError):
            self.assertIsInstance(FileStorage.file_path, str)

    def test_private_object_list(self):
        """Test for private variables
        """
        with self.assertRaises(AttributeError):
            self.assertIsInstance(FileStorage.objects, dict)


class TestFileStorageAll(unittest.TestCase):
    """Tests for the `all` method
    """

    def test_type(self):
        """Test the function's return type
        """
        self.assertIsInstance(storage.all(), dict)


class TestFileStorageNew(unittest.TestCase):
    """Tests for the `new` method
    """

    def test_new_BaseModel(self):
        """Test if it saves with the correct class and id
        """
        bm = BaseModel()
        test_key = "BaseModel.{}".format(bm.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_Amenity(self):
        """Test if it saves with the correct class and id
        """
        am = Amenity()
        test_key = "Amenity.{}".format(am.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_City(self):
        """Test if it saves with the correct class and id
        """
        ct = City()
        test_key = "City.{}".format(ct.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_PLace(self):
        """Test if it saves with the correct class and id
        """
        pl = Place()
        test_key = "Place.{}".format(pl.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_Review(self):
        """Test if it saves with the correct class and id
        """
        rv = Review()
        test_key = "Review.{}".format(rv.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_State(self):
        """Test if it saves with the correct class and id
        """
        st = State()
        test_key = "State.{}".format(st.id)
        self.assertIn(test_key, storage.all().keys())

    def test_new_User(self):
        """Test if it saves with the correct class and id
        """
        us = User()
        test_key = "User.{}".format(us.id)
        self.assertIn(test_key, storage.all().keys())


class TestFileStorageSave(unittest.TestCase):
    """Tests for the `save` method
    """

    @classmethod
    def setUp(self):
        """Temporarily rename the `file.json` to `temp`
        """
        try:
            os.rename('file.json', 'temp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Revert changes made to the `file.json` file
        """
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_save(self):
        """Tests `save` method
        """
        bm = BaseModel()
        am = Amenity()
        ct = City()
        pl = Place()
        rv = Review()
        st = State()
        us = User()
        storage.new(bm)
        storage.new(am)
        storage.new(ct)
        storage.new(pl)
        storage.new(rv)
        storage.new(st)
        storage.new(us)
        storage.save()
        test_save = ""

        with open('file.json', 'r') as f:
            test_save = f.read()
            self.assertIn('BaseModel.{}'.format(bm.id), test_save)
            self.assertIn('Amenity.{}'.format(am.id), test_save)
            self.assertIn('City.{}'.format(ct.id), test_save)
            self.assertIn('Place.{}'.format(pl.id), test_save)
            self.assertIn('Review.{}'.format(rv.id), test_save)
            self.assertIn('State.{}'.format(st.id), test_save)
            self.assertIn('User.{}'.format(us.id), test_save)


class TestFileStorageReload(unittest.TestCase):
    """Tests for the `reload` method
    """

    def test_reload(self):
        """Test `reload` method
        """
        bm = BaseModel()
        am = Amenity()
        ct = City()
        pl = Place()
        rv = Review()
        st = State()
        us = User()

        storage.reload()

        objs = FileStorage._FileStorage__objects

        self.assertIn('BaseModel.{}'.format(bm.id), objs)
        self.assertIn('Amenity.{}'.format(am.id), objs)
        self.assertIn('City.{}'.format(ct.id), objs)
        self.assertIn('Place.{}'.format(pl.id), objs)
        self.assertIn('Review.{}'.format(rv.id), objs)
        self.assertIn('State.{}'.format(st.id), objs)
        self.assertIn('User.{}'.format(us.id), objs)


if __name__ == '__main__':
    unittest.main()
