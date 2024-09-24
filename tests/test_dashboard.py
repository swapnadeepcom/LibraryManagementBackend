import pytest
from dashboard import Dashboard

@pytest.fixture
def dashboard():
    return Dashboard()

def test_admin_dashboard(dashboard, capsys):
    dashboard.admin_dashboard()
    captured = capsys.readouterr()
    assert "Welcome to the Admin Dashboard!" in captured.out

def test_librarian_dashboard(dashboard, capsys):
    dashboard.librarian_dashboard()
    captured = capsys.readouterr()
    assert "Welcome to the Librarian Dashboard!" in captured.out

def test_user_dashboard(dashboard, capsys):
    dashboard.user_dashboard()
    captured = capsys.readouterr()
    assert "Welcome to the User Dashboard!" in captured.out
