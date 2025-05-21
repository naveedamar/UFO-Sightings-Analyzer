import pytest
from project import load_data, sighting_count, count_by_duration, get_all_shapes, count_by_shape, get_top_shapes, count_by_region, get_region_values, search_by_duration, search_by_shape, search_by_region
import os

TEST_CSV_FILE = "data/ufo_sightings.csv"

def test_load_data():
    data = load_data(TEST_CSV_FILE)
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)
    assert 'city' in data[0]

def test_load_data_file_not_found():
    data = load_data("non_existent_file.csv")
    assert isinstance(data, list)
    assert not data

def test_sighting_count():
    data = load_data(TEST_CSV_FILE)
    assert sighting_count(data) >= 0

def test_count_by_duration():
    data = load_data(TEST_CSV_FILE)
    assert count_by_duration(data, 0) >= 0
    assert count_by_duration(data, 999999) >= 0

def test_get_all_shapes():
    data = load_data(TEST_CSV_FILE)
    shapes = get_all_shapes(data)
    assert isinstance(shapes, list)
    assert len(shapes) >= 0

def test_get_top_shapes():
    data = load_data(TEST_CSV_FILE)
    top_2 = get_top_shapes(data, 2)
    assert isinstance(top_2, list)
    if top_2:
        assert len(top_2) <= 2
        assert isinstance(top_2[0], tuple)
        assert len(top_2[0]) == 2

def test_get_region_values():
    data = load_data(TEST_CSV_FILE)
    cities = get_region_values(data, 'city')
    assert isinstance(cities, list)
    assert len(cities) >= 0
    states = get_region_values(data, 'state')
    assert isinstance(states, list)
    assert len(states) >= 0
    countries = get_region_values(data, 'country')
    assert isinstance(countries, list)
    assert len(countries) >= 0

def test_count_by_region():
    data = load_data(TEST_CSV_FILE)
    assert count_by_region(data, 'city', 'some_city') >= 0
    assert count_by_region(data, 'country', 'some_country') >= 0

def test_search_by_duration():
    data = load_data(TEST_CSV_FILE)
    results = search_by_duration(data, 0)
    assert isinstance(results, list)

def test_search_by_shape():
    data = load_data(TEST_CSV_FILE)
    results = search_by_shape(data, 'circle')
    assert isinstance(results, list)

def test_search_by_region():
    data = load_data(TEST_CSV_FILE)
    results_city = search_by_region(data, 'city', 'some_city')
    assert isinstance(results_city, list)
    results_country = search_by_region(data, 'country', 'some_country')
    assert isinstance(results_country, list)