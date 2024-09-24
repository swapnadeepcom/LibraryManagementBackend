import pytest
from authentication import Authentication

@pytest.fixture
def auth():
    # Initialize with empty admin, librarian, and user dictionaries
    return Authentication(admins={}, librarians={}, users={})

def test_register_admin(auth, mocker):
    mocker.patch('builtins.input', side_effect=["admin1", "admin_pass"])
    auth.register('admin')
    assert auth.admins['admin1'] == 'admin_pass'

def test_register_librarian(auth, mocker):
    mocker.patch('builtins.input', side_effect=["librarian1", "librarian_pass"])
    auth.register('librarian')
    assert auth.librarians['librarian1'] == 'librarian_pass'

def test_register_user(auth, mocker):
    mocker.patch('builtins.input', side_effect=["user1", "user_pass"])
    auth.register('user')
    assert auth.users['user1'] == 'user_pass'

def test_login_admin(auth, mocker):
    auth.admins = {'admin1': 'admin_pass'}
    mocker.patch('builtins.input', side_effect=["admin1", "admin_pass"])
    assert auth.login('admin') == None  # Assumed it prints the login message, no return value

def test_login_invalid(auth, mocker):
    auth.admins = {'admin1': 'admin_pass'}
    mocker.patch('builtins.input', side_effect=["admin1", "wrong_pass"])
    assert auth.login('admin') == None  # Expecting failure
