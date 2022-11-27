#!/usr/bin/python3
"""
Test file for the module `user.py`
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """test for correct instantiation
    """

    def test_instantiation(self):
        st1 = User()
        self.assertIsInstance(st1, User)

    def test_class_attrs(self):
        st1 = User()
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

        self.assertNotIn('email', st1.to_dict())
        self.assertNotIn('password', st1.to_dict())
        self.assertNotIn('first_name', st1.to_dict())
        self.assertNotIn('last_name', st1.to_dict())

    def test_id_type(self):
        st1 = User()
        self.assertIsInstance(st1.id, str)

    def test_created_at_type(self):
        self.assertEqual(type(User().created_at), datetime)

    def test_updated_at_type(self):
        self.assertEqual(type(User().updated_at), datetime)

    def test_uniq_id(self):
        st1 = User()
        am2 = User()
        self.assertNotEqual(st1.id, am2.id)

    def test_uniq_creation_time(self):
        st1 = User()
        sleep(2)
        am2 = User()
        self.assertLess(st1.created_at, am2.created_at)

    def test_uniq_update_time(self):
        st1 = User()
        sleep(2)
        am2 = User()
        self.assertLess(st1.updated_at, am2.updated_at)


class TestUserSave(unittest.TestCase):
    """test if correctly saved
    """

    def test_save(self):
        st1 = User()
        self.assertIn(st1, storage.all().values())

    def test_update_time_change(self):
        st1 = User()
        initial_update = st1.updated_at
        sleep(2)
        st1.save()
        first_update = st1.updated_at
        sleep(2)
        st1.save()
        second_update = st1.updated_at

        self.assertLess(initial_update, first_update)
        self.assertLess(first_update, second_update)

    def test_file_exists(self):
        st1 = User()
        st1.save()
        boolean = os.path.exists('file.json')
        self.assertTrue(boolean)

    def test_file_contains_id(self):
        st1 = User()
        st1.save()
        test_id = "User.{}".format(st1.id)
        with open('file.json', 'r') as f:
            self.assertIn(test_id, f.read())


class TestUserToDict(unittest.TestCase):
    """test for creation from dict
    """

    def test_to_dict_type(self):
        st1 = User()
        self.assertIsInstance(st1.to_dict(), dict)

    def test_contains_correct_keys(self):
        st1 = User()
        self.assertIn('__class__', st1.to_dict().keys())
        self.assertIn('id', st1.to_dict().keys())
        self.assertIn('created_at', st1.to_dict().keys())
        self.assertIn('updated_at', st1.to_dict().keys())

    def test_correct_format(self):
        st1 = User()
        self.assertIsInstance(st1.to_dict()['created_at'], str)
        self.assertIsInstance(st1.to_dict()['updated_at'], str)


class TestUserRepresentation(unittest.TestCase):
    """test fro __str__
    """

    def test_correct_format(self):
        st1 = User()
        str_repr = st1.__str__()
        self.assertIn('User', str_repr)
        self.assertIn('updated_at', str_repr)
        self.assertIn('created_at', str_repr)


class TestUserFromDict(unittest.TestCase):
    """test for creation from dict

    Args:
        unittest (_type_): _description_
    """

    def test_kwargs(self):
        st1 = User(id="my-uniq-id-123", name='Test For Name')
        self.assertEqual(st1.name, 'Test For Name')
        self.assertEqual(st1.id, "my-uniq-id-123")


if __name__ == "__main__":
    unittest.main()
