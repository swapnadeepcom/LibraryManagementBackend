# Tests for dashboard logic

import pytest
from Library_Management import Dashboard

@pytest.fixture
def dashboard():
    return Dashboard()

def test_generate_report(dashboard):
    report = dashboard.generate_report()
    assert isinstance(report, dict)
    assert 'total_users' in report
    assert 'total_books' in report

def test_get_statistics(dashboard):
    stats = dashboard.get_statistics()
    assert isinstance(stats, dict)
    assert 'most_popular_book' in stats
