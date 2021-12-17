# To illustrate use of fixtures in pytest

import pytest

@pytest.fixture()
def setup():
    print("Before every method - Setup method")

def test_method1(setup):
    print("Method 1")

def test_method2(setup):
    print("Method2")