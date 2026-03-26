import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scr'))

from people_counter import count_people_by_location

SMALL_FILE = os.path.join(os.path.dirname(__file__), '..', 'Testing_data', 'people.json')
BIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'Testing_data', 'BIGpeople.json')


# people.json

def test_small_returns_dict():
    result = count_people_by_location(SMALL_FILE)
    assert isinstance(result, dict)

def test_small_tallinn():
    result = count_people_by_location(SMALL_FILE)
    assert result.get("Tallinn") == 3

def test_small_tartu():
    result = count_people_by_location(SMALL_FILE)
    assert result.get("Tartu") == 2

def test_small_parnu():
    result = count_people_by_location(SMALL_FILE)
    assert result.get("Pärnu") == 1

def test_small_total_people():
    result = count_people_by_location(SMALL_FILE)
    assert sum(result.values()) == 6

def test_small_location_count():
    result = count_people_by_location(SMALL_FILE)
    assert len(result) == 3


# BIGpeople.json

def test_big_returns_dict():
    result = count_people_by_location(BIG_FILE)
    assert isinstance(result, dict)

def test_big_tallinn():
    result = count_people_by_location(BIG_FILE)
    assert result.get("Tallinn") == 7

def test_big_tartu():
    result = count_people_by_location(BIG_FILE)
    assert result.get("Tartu") == 6

def test_big_parnu():
    result = count_people_by_location(BIG_FILE)
    assert result.get("Pärnu") == 4

def test_big_narva():
    result = count_people_by_location(BIG_FILE)
    assert result.get("Narva") == 3

def test_big_total_people():
    result = count_people_by_location(BIG_FILE)
    assert sum(result.values()) == 30

def test_big_all_values_positive():
    result = count_people_by_location(BIG_FILE)
    assert all(v > 0 for v in result.values())


# kontroll

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_people_by_location("nonexistent.json")
