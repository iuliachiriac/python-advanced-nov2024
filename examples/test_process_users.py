import json
import os
import unittest

from process_users import get_name_age, get_users


class GetUsersTestCase(unittest.TestCase):
    FILE_NAME = "test_users.json"

    @classmethod
    def setUpClass(cls):
        cls.users_expected = [{
            "name": "John Doe",
            "age": 20,
        }, {
            "first_name": "Anna",
            "last_name": "Smith",
            "age": 35,
        }, {
            "name": "Jane Addams",
            "age": 45,
        }]
        with open(cls.FILE_NAME, "w") as f:
            json.dump(cls.users_expected, f)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.FILE_NAME)

    def test_nonexistent_file(self):
        users = get_users("nonexistent.txt")
        self.assertListEqual(users, [])

    def test_unfiltered_list(self):
        users = get_users(self.FILE_NAME)

        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 3)
        self.assertListEqual(self.users_expected, users)

    def test_filtered_list(self):
        users = get_users(self.FILE_NAME, 20, 38)

        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 1)
        self.assertListEqual(users, self.users_expected[1:2])

    def test_invalid_json(self):
        filename = "file.txt"
        with open(filename, "w"):
            pass

        with self.assertRaises(json.decoder.JSONDecodeError):
            get_users(filename)

        os.remove(filename)


class GetNameAgeTestCase(unittest.TestCase):
    def test_name(self):
        inputs = [{
            "name": "John Doe",
            "age": 20,
        }, {
            "first_name": "Anna",
            "last_name": "Smith",
            "age": 35,
        }]
        outputs = [("John Doe", 20), ("Anna Smith", 35)]

        for user, (name_exp, age_exp) in zip(inputs, outputs):
            with self.subTest(f"Failed for user={user}"):
                name, age = get_name_age(user)
                self.assertEqual(name, name_exp)
                self.assertEqual(age, age_exp)
