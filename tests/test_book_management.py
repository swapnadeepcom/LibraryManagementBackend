import unittest
from book_management import BookManagement

class TestBookManagement(unittest.TestCase):

    def setUp(self):
        self.book_mgmt = BookManagement()

    def test_add_book(self):
        with self.assertLogs() as captured:
            self.book_mgmt.add_book("101", "Python Basics")
            self.assertIn("Book 'Python Basics' added successfully!", captured.output[0])
        self.assertIn("101", self.book_mgmt.books)
        self.assertEqual(self.book_mgmt.books["101"], "Python Basics")

    def test_issue_book(self):
        self.book_mgmt.add_book("102", "Data Science")
        with self.assertLogs() as captured:
            self.book_mgmt.issue_book("102", "john_doe")
            self.assertIn("issued to john_doe", captured.output[0])
        self.assertIn("102", self.book_mgmt.issued_books)
        self.assertEqual(self.book_mgmt.issued_books["102"], "john_doe")

    def test_return_book(self):
        self.book_mgmt.add_book("103", "AI for Beginners")
        self.book_mgmt.issue_book("103", "jane_doe")
        with self.assertLogs() as captured:
            self.book_mgmt.return_book("103")
            self.assertIn("returned by jane_doe", captured.output[0])
        self.assertNotIn("103", self.book_mgmt.issued_books)

if __name__ == '__main__':
    unittest.main()
