import pytest
from book_management import BookManagement

@pytest.fixture
def book_mgmt():
    return BookManagement()

def test_add_book(book_mgmt, capsys):
    book_mgmt.add_book("101", "Python Basics")
    captured = capsys.readouterr()
    assert "Python Basics added successfully!" in captured.out
    assert book_mgmt.books["101"] == "Python Basics"

def test_issue_book(book_mgmt, capsys):
    book_mgmt.add_book("102", "Data Science")
    book_mgmt.issue_book("102", "john_doe")
    captured = capsys.readouterr()
    assert "issued to john_doe" in captured.out
    assert book_mgmt.issued_books["102"] == "john_doe"

def test_return_book(book_mgmt, capsys):
    book_mgmt.add_book("103", "AI for Beginners")
    book_mgmt.issue_book("103", "jane_doe")
    book_mgmt.return_book("103")
    captured = capsys.readouterr()
    assert "returned by jane_doe" in captured.out
    assert "103" not in book_mgmt.issued_books
