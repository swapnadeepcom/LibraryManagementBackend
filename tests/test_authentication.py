# Tests for authentication

import pytest
from authentication import Authentication

@pytest.fixture
def auth():
    return Authentication()

def test_login(auth):
    auth.add_user('john_doe', 'password123')
    assert auth.login('john_doe', 'password123') is True

def test_failed_login(auth):
    auth.add_user('john_doe', 'password123')
    assert auth.login('john_doe', 'wrongpassword') is False

def test_logout(auth):
    auth.add_user('john_doe', 'password123')
    auth.login('john_doe', 'password123')
    assert auth.logout('john_doe') is True
