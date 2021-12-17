# To illustrate use of fixtures in pytest

import pytest

@pytest.fixture()    # annotation or decoration
def setup():
    print("Before every method")
    yield
    print("After every method")

def test_method1(setup):
    print("Method 1")

def test_method(setup):
    print("Method 2")