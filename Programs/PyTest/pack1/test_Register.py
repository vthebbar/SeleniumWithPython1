# use of pytest framework

import pytest

@pytest.fixture()
def setup():
    print("Before every method")
    yield
    print("After every method")

def test_RegsiterbyEmail(setup):
    print("Register by email")

def test_RegisterByMobile(setup):
    print("Register by Mobile")