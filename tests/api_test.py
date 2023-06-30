import pytest
import requests
from pygemstones.system import runner as r

# ------------------------------------------------------------------------------
# FIXTURES
# ------------------------------------------------------------------------------


# general fixture before and after all tests
@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_session():
    print("> Running general command before all tests")
    print("• docker start")
    r.run(["ls", "-lah"])
    # command to be executed before all tests

    yield

    print("> Running general command after all tests")
    print("• docker stop")
    r.run(["ls", "-lah"])
    # command to be executed after all tests


# fixture before and after each individual test
@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Running command before each test")
    print("• reset database to a dump")
    r.run(["ls", "-lah"])
    # command to be executed before each test

    yield

    print("running command after each test")
    print("• clear database")
    r.run(["ls", "-lah"])
    # command to be executed after each test


# ------------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------------


# test all products
def test_get_products():
    response = requests.get("https://dummyjson.com/products")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["total"] == 100

    # test fields
    product = json_data["products"][0]
    assert "title" in product
    assert "thumbnail" in product
    assert type(product["title"]) is str


# test search products
def test_search():
    response = requests.get("https://dummyjson.com/products/search?q=phone")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["total"] == 4

    # test fields
    product = json_data["products"][0]
    assert "title" in product
    assert "thumbnail" in product
    assert type(product["title"]) is str
