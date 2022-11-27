#!/usr/bin/python3
"""Test file for the module `amenity.py`
"""
import unittest
from datetime import datetime
from time import sleep
from models import storage
import os

from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Test for correct instantiation
    """

    def test_instantiation(self):
        """Test correct type
        """
        am = Amenity()
        self.assertIsInstance(am, Amenity)

    def test_class_attr(self):
        """Test for class attributes
        """
        am1 = Amenity()
        self.assertIsInstance(Amenity.name, str)
        self.assertNotIn('name', am1.to_dict())

    def test_id_type(self):
        """Test for correct id type
        """
        am1 = Amenity()
        self.assertIsInstance(am1.id, str)

    def test_created_at_type(self):
        """Test for correct created_at type
        """
        self.assertEqual(type(Amenity().created_at), datetime)

    def test_updated_at_type(self):
        """Test for correct created_at type
        """
        self.assertEqual(type(Amenity().updated_at), datetime)

    def test_uniq_id(self):
        """Test the uniqueness of two object's ids
        """
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_uniq_creation_time(self):
        """Test the uniqueness of two objects created at different time
        """
        am1 = Amenity()
        sleep(2)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_uniq_update_time(self):
        """Test for change of updated_at time
        """
        am1 = Amenity()
        sleep(2)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)


class TestAmenitySave(unittest.TestCase):
    """Test for correctly saving of Amenity class objects
    """

    def test_save(self):
        """Test if saved
        """
        am1 = Amenity()
        self.assertIn(am1, storage.all().values())

    def test_update_time_change(self):
        """Test for change of updated at time
        """
        am1 = Amenity()
        initial_update = am1.updated_at
        sleep(2)
        am1.save()
        first_update = am1.updated_at
        sleep(2)
        am1.save()
        second_update = am1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        """Test for existence of the file
        """
        am1 = Amenity()
        am1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        """test for correct id
        """
        am1 = Amenity()
        am1.save()
        test_id = "Amenity.{}".format(am1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestAmenityToDict(unittest.TestCase):
    def test_to_dict_type(self):
        """test correct type
        """
        am1 = Amenity()
        self.assertIsInstance(am1.to_dict(), dict)

    def test_contains_correct_keys(self):
        """test correct keys
        """
        am1 = Amenity()
        self.assertIn('__class__', am1.to_dict().keys())
        self.assertIn('id', am1.to_dict().keys())
        self.assertIn('created_at', am1.to_dict().keys())
        self.assertIn('updated_at', am1.to_dict().keys())

    def test_contains_additional_keys(self):
        """test additional keys
        """
        am1 = Amenity()
        am1.name = 'Best School'
        self.assertIn('name', am1.to_dict().keys())

    def test_correct_format(self):
        """test correct format
        """
        am1 = Amenity()
        self.assertIsInstance(am1.to_dict()['created_at'], str)
        self.assertIsInstance(am1.to_dict()['updated_at'], str)


class TestAmenityRepresentation(unittest.TestCase):
    """Test for `__str__`
    """

    def test_correct_format(self):
        """test correct format
        """
        am1 = Amenity()
        str_repr = am1.__str__()
        self.assertIn('Amenity', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestAmenityFromDict(unittest.TestCase):
    """test from dict creation

    Args:
        unittest (_type_): _description_
    """

    def test_kwargs(self):
        """test for creating new object with kwargs
        """
        am1 = Amenity(id="my-uniq-id-123", name='Test For Name')
        self.assertEqual(am1.name, 'Test For Name')
        self.assertEqual(am1.id, "my-uniq-id-123")


if __name__ == "__main__":
    unittest.main()
