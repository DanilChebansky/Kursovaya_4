import pytest
from src import functions


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def some_list():
    return [{
        "name": "Test Name",
        "apply_alternate_url": "Test Url",
        "salary": {"from": 20, "to": 30},
        "snippet": {"requirement": "Test Requirements"},
        "experience": {"name": "Test Experience"},
        "area": {"name": "Test Area"},
        "mid_salary": 25,
    }]


@pytest.fixture
def some_another_list():
    return [{
        "name": "Test Name",
        "url": "Test Url",
        "salary": {"from": 20, "to": 30},
        "requirements": "Test Requirements",
        "experience": "Test Experience",
        "area": "Test Area",
        "mid_salary": 25
    }]


@pytest.fixture
def one_more_list():
    return [{
        "name": "Test Name",
        "url": "Test Url",
        "salary": {"from": None, "to": None},
        "requirements": "Test Requirements",
        "experience": "Test Experience",
        "area": "Test Area",
        "mid_salary": 25
    }]


@pytest.fixture
def some_words():
    return ["Url", "Junior"]


@pytest.fixture
def some_another_words():
    return ["Test", "Junior"]


@pytest.fixture
def some_value():
    return "hundred"