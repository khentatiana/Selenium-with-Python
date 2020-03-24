import pytest

@pytest.yield_fixture()
def setup():
    print("\nThis is SETUP method.Open URL")
    yield
    print("\nThis is teardown after each method. Close browser after each login")

def test_LoginByEmail(setup):
    print("\nThis is login via email test")

def test_LoginByFacebook(setup):
    print("\nThis is login by Facebook test")

def test_LoginByTwitter(setup):
    print("\nThis is login by Twitter test")

