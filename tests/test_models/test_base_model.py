#!/usr/bin/python3
"""
test file for the module `base_model.py`
"""
from datetime import datetime
import unittest
from time import sleep

from models.base_model import BaseModel
from models import storage
import os


class TestBaseModelInstantiation(unittest.TestCase):
    """Test for correct instantiation
    """

    def test_instantiation(self):
        """Test correct type
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_id_type(self):
        """test for correct id type
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_created_at_type(self):
        """test for correct type
        """
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_updated_at_type(self):
        """test for correct type
        """
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_uniq_id(self):
        """test for uniq id
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_uniq_creation_time(self):
        """test for uniq created at time
        """
        b1 = BaseModel()
        sleep(2)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_uniq_update_time(self):
        """test for uniq updated at time
        """
        b1 = BaseModel()
        sleep(2)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)


class TestBaseModelSave(unittest.TestCase):
    """test if object is saved
    """

    def test_save(self):
        """test save
        """
        b1 = BaseModel()
        self.assertIn(b1, storage.all().values())

    def test_update_time_change(self):
        """test update time
        """
        b1 = BaseModel()
        initial_update = b1.updated_at
        sleep(2)
        b1.save()
        first_update = b1.updated_at
        sleep(2)
        b1.save()
        second_update = b1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        """test if file exists
        """
        b1 = BaseModel()
        b1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        """test if file contains correct class name and id
        """
        b1 = BaseModel()
        b1.save()
        test_id = "BaseModel.{}".format(b1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """test for the function `to_dict`
    """

    def test_to_dict_type(self):
        """test for correct type
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict(), dict)

    def test_contains_correct_keys(self):
        """test for correct keys
        """
        b1 = BaseModel()
        self.assertIn('__class__', b1.to_dict().keys())
        self.assertIn('id', b1.to_dict().keys())
        self.assertIn('created_at', b1.to_dict().keys())
        self.assertIn('updated_at', b1.to_dict().keys())

    def test_contains_additional_keys(self):
        """test for additional keys
        """
        b1 = BaseModel()
        b1.name = 'Best School'
        b1.my_number = 98
        self.assertIn('name', b1.to_dict().keys())
        self.assertIn('my_number', b1.to_dict().keys())

    def test_correct_format(self):
        """test for correct format
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict()['created_at'], str)
        self.assertIsInstance(b1.to_dict()['updated_at'], str)


class TestBaseModelRepresentation(unittest.TestCase):
    """test for `__str__`
    """

    def test_correct_format(self):
        """test correct format
        """
        b1 = BaseModel()
        str_repr = b1.__str__()
        self.assertIn('BaseModel', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestBaseModelFromDict(unittest.TestCase):
    """test create from dict
    """

    def test_kwargs(self):
        """test create with kwargs
        """
        b1 = BaseModel(id="my-uniq-id-123", name='Test For Name', my_number=89)
        self.assertEqual(b1.name, 'Test For Name')
        self.assertEqual(b1.my_number, 89)
        self.assertEqual(b1.id, "my-uniq-id-123")


if __name__ == '__main__':
    unittest.main()
