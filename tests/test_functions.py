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


def test_filter_vacancies(empty_list, some_list, some_words, some_another_words):
    assert functions.filter_vacancies(empty_list, empty_list) == []
    assert functions.filter_vacancies(some_list, empty_list) == [{
        "name": "Test Name",
        "apply_alternate_url": "Test Url",
        "salary": {"from": 20, "to": 30},
        "snippet": {"requirement": "Test Requirements"},
        "experience": {"name": "Test Experience"},
        "area": {"name": "Test Area"},
        "mid_salary": 25,
    }]
    assert functions.filter_vacancies(some_list, some_words) == []
    assert functions.filter_vacancies(some_list, some_another_words) == [{
        "name": "Test Name",
        "apply_alternate_url": "Test Url",
        "salary": {"from": 20, "to": 30},
        "snippet": {"requirement": "Test Requirements"},
        "experience": {"name": "Test Experience"},
        "area": {"name": "Test Area"},
        "mid_salary": 25,
    }]


def test_get_vacancies_by_salary(some_list, empty_list, some_value):
    assert functions.get_vacancies_by_salary(empty_list, 1, 2) == []


def test_sort_vacancies(empty_list, some_list):
    assert functions.sort_vacancies(empty_list) == []


def test_get_top_vacancies(empty_list, some_value, some_list):
    assert functions.get_top_vacancies(empty_list, 2) == []
    assert functions.get_top_vacancies(empty_list, some_value) == []
    assert functions.get_top_vacancies(some_list, 2) == [{
        "name": "Test Name",
        "apply_alternate_url": "Test Url",
        "salary": {"from": 20, "to": 30},
        "snippet": {"requirement": "Test Requirements"},
        "experience": {"name": "Test Experience"},
        "area": {"name": "Test Area"},
        "mid_salary": 25,
    }]


def test_print_vacancies(empty_list, some_another_list, one_more_list):
    assert functions.print_vacancies(empty_list) == []
