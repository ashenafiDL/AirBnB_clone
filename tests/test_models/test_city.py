#!/usr/bin/python3
"""
Test file for the module `city.py`
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """test for correct instantiation
    """

    def test_instantiation(self):
        """test for correct instantiation
        """
        ct1 = City()
        self.assertIsInstance(ct1, City)

    def test_class_attrs(self):
        """test for class attributes
        """
        ct1 = City()
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

        self.assertNotIn('state_id', ct1.to_dict())
        self.assertNotIn('name', ct1.to_dict())

    def test_id_type(self):
        """test for correct id type
        """
        ct1 = City()
        self.assertIsInstance(ct1.id, str)

    def test_created_at_type(self):
        """test for correct created at type
        """
        self.assertEqual(type(City().created_at), datetime)

    def test_updated_at_type(self):
        """test for correct updated at type
        """
        self.assertEqual(type(City().updated_at), datetime)

    def test_uniq_id(self):
        """test for uniq id
        """
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_uniq_creation_time(self):
        """test for uniq creation time
        """
        ct1 = City()
        sleep(2)
        ct2 = City()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_uniq_update_time(self):
        """test for uniq update time
        """
        ct1 = City()
        sleep(2)
        ct2 = City()
        self.assertLess(ct1.updated_at, ct2.updated_at)


class TestCitySave(unittest.TestCase):
    """test if object is saved
    """

    def test_save(self):
        """test save
        """
        ct1 = City()
        self.assertIn(ct1, storage.all().values())

    def test_update_time_change(self):
        """test update time
        """
        ct1 = City()
        initial_update = ct1.updated_at
        sleep(2)
        ct1.save()
        first_update = ct1.updated_at
        sleep(2)
        ct1.save()
        second_update = ct1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        """test if file exists
        """
        ct1 = City()
        ct1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        """test if file contains correct class name and id
        """
        ct1 = City()
        ct1.save()
        test_id = "City.{}".format(ct1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestCityToDict(unittest.TestCase):
    """test for the function `to_dict`
    """

    def test_to_dict_type(self):
        """test for correct type
        """
        ct1 = City()
        self.assertIsInstance(ct1.to_dict(), dict)

    def test_contains_correct_keys(self):
        """test for correct keys
        """
        ct1 = City()
        self.assertIn('__class__', ct1.to_dict().keys())
        self.assertIn('id', ct1.to_dict().keys())
        self.assertIn('created_at', ct1.to_dict().keys())
        self.assertIn('updated_at', ct1.to_dict().keys())

    def test_correct_format(self):
        """test for correct format
        """
        ct1 = City()
        self.assertIsInstance(ct1.to_dict()['created_at'], str)
        self.assertIsInstance(ct1.to_dict()['updated_at'], str)


class TestCityRepresentation(unittest.TestCase):
    """test for `__str__`
    """

    def test_correct_format(self):
        """test correct format
        """
        ct1 = City()
        str_repr = ct1.__str__()
        self.assertIn('City', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestCityFromDict(unittest.TestCase):
    """test create from dict
    """

    def test_kwargs(self):
        """test create with kwargs
        """
        ct1 = City(id="my-uniq-id-123", name='Test For Name')
        self.assertEqual(ct1.name, 'Test For Name')
        self.assertEqual(ct1.id, "my-uniq-id-123")


if __name__ == "__main__":
    unittest.main()
