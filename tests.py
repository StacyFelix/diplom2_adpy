import unittest
import diplom2 as app
from unittest.mock import patch


class TestDiplom2(unittest.TestCase):
    token = 'cb6c56d4f9f54d37c74990608bcebd40b1043b054cd716404f5d40eda33c620ccb25ba78bb64e709f2454'
    user = app.User(511577556)

    def test_get_list_top10_users(self):
        user_input = ["geter", "30", "35"]
        with patch('builtins.input', side_effect=user_input):
            list_top10_users = self.user.get_list_top10_users()
            self.assertIsInstance(list_top10_users, list)
            self.assertLessEqual(len(list_top10_users), 10)
            for user in list_top10_users:
                self.assertLessEqual(len(user['photos_top3']), 3)
                self.assertEqual(len(set(list(user.keys())).difference({"id", "weight", "photos_top3"})), 0)


if __name__ == '__main__':
    unittest.main()
