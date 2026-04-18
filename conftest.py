import pytest
import json
import requests

@pytest.fixture
def test_data():
    with open("test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def base_url(test_data):
    return test_data["base_url"]