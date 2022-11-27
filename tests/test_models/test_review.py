#!/usr/bin/python3
"""
test file for the module `review.py`
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """test for correct instantiation
    """

    def test_instantiation(self):
        rv1 = Review()
        self.assertIsInstance(rv1, Review)

    def test_class_attrs(self):
        rv1 = Review()
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

        self.assertNotIn('place_id', rv1.to_dict())
        self.assertNotIn('user_id', rv1.to_dict())
        self.assertNotIn('text', rv1.to_dict())

    def test_id_type(self):
        rv1 = Review()
        self.assertIsInstance(rv1.id, str)

    def test_created_at_type(self):
        self.assertEqual(type(Review().created_at), datetime)

    def test_updated_at_type(self):
        self.assertEqual(type(Review().updated_at), datetime)

    def test_uniq_id(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_uniq_creation_time(self):
        rv1 = Review()
        sleep(2)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_uniq_update_time(self):
        rv1 = Review()
        sleep(2)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)


class TestReviewSave(unittest.TestCase):
    """test if correctly saved
    """

    def test_save(self):
        rv1 = Review()
        self.assertIn(rv1, storage.all().values())

    def test_update_time_change(self):
        rv1 = Review()
        initial_update = rv1.updated_at
        sleep(2)
        rv1.save()
        first_update = rv1.updated_at
        sleep(2)
        rv1.save()
        second_update = rv1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        rv1 = Review()
        rv1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        rv1 = Review()
        rv1.save()
        test_id = "Review.{}".format(rv1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestReviewToDict(unittest.TestCase):
    """test for correct dict
    """

    def test_to_dict_type(self):
        rv1 = Review()
        self.assertIsInstance(rv1.to_dict(), dict)

    def test_contains_correct_keys(self):
        rv1 = Review()
        self.assertIn('__class__', rv1.to_dict().keys())
        self.assertIn('id', rv1.to_dict().keys())
        self.assertIn('created_at', rv1.to_dict().keys())
        self.assertIn('updated_at', rv1.to_dict().keys())

    def test_correct_format(self):
        rv1 = Review()
        self.assertIsInstance(rv1.to_dict()['created_at'], str)
        self.assertIsInstance(rv1.to_dict()['updated_at'], str)


class TestReviewRepresentation(unittest.TestCase):
    """test fro __str__"""

    def test_correct_format(self):
        rv1 = Review()
        str_repr = rv1.__str__()
        self.assertIn('Review', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestReviewFromDict(unittest.TestCase):
    """test for creation from dict
    """

    def test_kwargs(self):
        rv1 = Review(id="my-uniq-id-123", name='Test For Name')
        self.assertEqual(rv1.name, 'Test For Name')
        self.assertEqual(rv1.id, "my-uniq-id-123")


if __name__ == "__main__":
    unittest.main()
