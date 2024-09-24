# Tests for user management

import pytest
from Library_Management import UserManagement

@pytest.fixture
def user_mgmt():
    return UserManagement()

def test_add_user(user_mgmt):
    user_mgmt.add_user('john_doe', 'John Doe', 'johndoe@example.com')
    assert user_mgmt.get_user('john_doe') is not None

def test_remove_user(user_mgmt):
    user_mgmt.add_user('jane_doe', 'Jane Doe', 'janedoe@example.com')
    user_mgmt.remove_user('jane_doe')
    assert user_mgmt.get_user('jane_doe') is None

def test_get_user(user_mgmt):
    user_mgmt.add_user('john_doe', 'John Doe', 'johndoe@example.com')
    user = user_mgmt.get_user('john_doe')
    assert user['name'] == 'John Doe'
    assert user['email'] == 'johndoe@example.com'
