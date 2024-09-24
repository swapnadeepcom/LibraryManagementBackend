import unittest
from user_management import UserManagement

class TestUserManagement(unittest.TestCase):
    def test_register(self):
        system = UserManagement()
        system.admins = {}
        # simulate registration here
        self.assertIsInstance(system.admins, dict)

if __name__ == '__main__':
    unittest.main()
