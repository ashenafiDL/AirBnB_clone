#!/usr/bin/python3
"""
Test file for the module `place.py`
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """test for correct instantiation
    """

    def test_instantiation(self):
        pl1 = Place()
        self.assertIsInstance(pl1, Place)

    def test_class_attrs(self):
        pl1 = Place()
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

        self.assertNotIn('state_id', pl1.to_dict())
        self.assertNotIn('user_id', pl1.to_dict())
        self.assertNotIn('name', pl1.to_dict())
        self.assertNotIn('description', pl1.to_dict())
        self.assertNotIn('number_rooms', pl1.to_dict())
        self.assertNotIn('number_bathrooms', pl1.to_dict())
        self.assertNotIn('max_guest', pl1.to_dict())
        self.assertNotIn('price_by_night', pl1.to_dict())
        self.assertNotIn('latitude', pl1.to_dict())
        self.assertNotIn('longitude', pl1.to_dict())
        self.assertNotIn('amenity_ids', pl1.to_dict())

    def test_id_type(self):
        pl1 = Place()
        self.assertIsInstance(pl1.id, str)

    def test_created_at_type(self):
        self.assertEqual(type(Place().created_at), datetime)

    def test_updated_at_type(self):
        self.assertEqual(type(Place().updated_at), datetime)

    def test_uniq_id(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_uniq_creation_time(self):
        pl1 = Place()
        sleep(2)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_uniq_update_time(self):
        pl1 = Place()
        sleep(2)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)


class TestPlaceSave(unittest.TestCase):
    """test if object is saved
    """

    def test_save(self):
        pl1 = Place()
        self.assertIn(pl1, storage.all().values())

    def test_update_time_change(self):
        pl1 = Place()
        initial_update = pl1.updated_at
        sleep(2)
        pl1.save()
        first_update = pl1.updated_at
        sleep(2)
        pl1.save()
        second_update = pl1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        pl1 = Place()
        pl1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        pl1 = Place()
        pl1.save()
        test_id = "Place.{}".format(pl1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestPlaceToDict(unittest.TestCase):
    """test creation from dict
    """

    def test_to_dict_type(self):
        pl1 = Place()
        self.assertIsInstance(pl1.to_dict(), dict)

    def test_contains_correct_keys(self):
        pl1 = Place()
        self.assertIn('__class__', pl1.to_dict().keys())
        self.assertIn('id', pl1.to_dict().keys())
        self.assertIn('created_at', pl1.to_dict().keys())
        self.assertIn('updated_at', pl1.to_dict().keys())

    def test_correct_format(self):
        pl1 = Place()
        self.assertIsInstance(pl1.to_dict()['created_at'], str)
        self.assertIsInstance(pl1.to_dict()['updated_at'], str)


class TestPlaceRepresentation(unittest.TestCase):
    """test for __str__
    """

    def test_correct_format(self):
        """test for correct output
        """
        pl1 = Place()
        str_repr = pl1.__str__()
        self.assertIn('Place', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestPlaceFromDict(unittest.TestCase):
    """test for create with dict
    """

    def test_kwargs(self):
        """test create with kwargs
        """
        pl1 = Place(id="my-uniq-id-123", name='Test For Name')
        self.assertEqual(pl1.name, 'Test For Name')
        self.assertEqual(pl1.id, "my-uniq-id-123")


if __name__ == "__main__":
    unittest.main()
