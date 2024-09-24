# Tests for book management

import pytest
from Library_Management import BookManagement

@pytest.fixture
def book_mgmt():
    return BookManagement()

def test_add_book(book_mgmt):
    book_mgmt.add_book('123', 'Python 101', 'John Smith')
    assert book_mgmt.get_book('123') is not None

def test_remove_book(book_mgmt):
    book_mgmt.add_book('456', 'Data Science Basics', 'Jane Doe')
    book_mgmt.remove_book('456')
    assert book_mgmt.get_book('456') is None

def test_get_book(book_mgmt):
    book_mgmt.add_book('789', 'Advanced AI', 'John AI')
    book = book_mgmt.get_book('789')
    assert book['title'] == 'Advanced AI'
    assert book['author'] == 'John AI'
