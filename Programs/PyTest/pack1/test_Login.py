# Use of pytest framework

import pytest

@pytest.fixture()
def setup():
    print("Before every method")
    yield
    print("After every method")

def test_loginByEmail(setup):
    print("Login by Email")

def test_loginByMobile(setup):
    print("Login by Mobile")