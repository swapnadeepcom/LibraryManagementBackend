# Tests for book transactions

import pytest
from transaction_management import Transaction

@pytest.fixture
def transaction():
    return Transaction()

def test_borrow_book(transaction):
    transaction.add_user('john_doe')
    transaction.add_book('123', 'Python 101', 'John Smith')
    assert transaction.borrow_book('john_doe', '123') is True

def test_return_book(transaction):
    transaction.add_user('john_doe')
    transaction.add_book('123', 'Python 101', 'John Smith')
    transaction.borrow_book('john_doe', '123')
    assert transaction.return_book('john_doe', '123') is True

def test_failed_borrow_book(transaction):
    transaction.add_user('john_doe')
    assert transaction.borrow_book('john_doe', 'invalid_book') is False
