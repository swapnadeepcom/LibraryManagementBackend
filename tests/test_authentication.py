import sys
import os
import unittest
from unittest.mock import patch

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from authentication import Authentication

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        # Initialize Authentication with empty dictionaries
        self.auth = Authentication(admins={}, librarians={}, users={})

    @patch('builtins.input', side_effect=["admin1", "admin_pass"])
    def test_register_admin(self, mock_input):
        self.auth.register('admin')
        self.assertIn('admin1', self.auth.admins)
        self.assertEqual(self.auth.admins['admin1'], 'admin_pass')

    @patch('builtins.input', side_effect=["librarian1", "librarian_pass"])
    def test_register_librarian(self, mock_input):
        self.auth.register('librarian')
        self.assertIn('librarian1', self.auth.librarians)
        self.assertEqual(self.auth.librarians['librarian1'], 'librarian_pass')

    @patch('builtins.input', side_effect=["user1", "user_pass"])
    def test_register_user(self, mock_input):
        self.auth.register('user')
        self.assertIn('user1', self.auth.users)
        self.assertEqual(self.auth.users['user1'], 'user_pass')

    @patch('builtins.input', side_effect=["admin1", "admin_pass"])
    def test_login_admin(self, mock_input):
        self.auth.admins = {'admin1': 'admin_pass'}
        with patch('builtins.print') as mocked_print:
            self.auth.login('admin')
            mocked_print.assert_called_with("Logged in as Admin")

    @patch('builtins.input', side_effect=["admin1", "wrong_pass"])
    def test_login_invalid(self, mock_input):
        self.auth.admins = {'admin1': 'admin_pass'}
        with patch('builtins.print') as mocked_print:
            self.auth.login('admin')
            mocked_print.assert_called_with("Invalid credentials")

if __name__ == '__main__':
    unittest.main()
