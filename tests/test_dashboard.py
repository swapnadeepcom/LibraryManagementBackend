import unittest
from dashboard import Dashboard

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.dashboard = Dashboard()

    def test_admin_dashboard(self):
        with self.assertLogs() as captured:
            self.dashboard.admin_dashboard()
            self.assertIn("Welcome to the Admin Dashboard!", captured.output[0])

    def test_librarian_dashboard(self):
        with self.assertLogs() as captured:
            self.dashboard.librarian_dashboard()
            self.assertIn("Welcome to the Librarian Dashboard!", captured.output[0])

    def test_user_dashboard(self):
        with self.assertLogs() as captured:
            self.dashboard.user_dashboard()
            self.assertIn("Welcome to the User Dashboard!", captured.output[0])

if __name__ == '__main__':
    unittest.main()
