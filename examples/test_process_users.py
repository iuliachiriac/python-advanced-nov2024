import json
import os
import unittest

from process_users import get_users


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
