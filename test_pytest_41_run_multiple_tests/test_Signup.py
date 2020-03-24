import pytest


@pytest.yield_fixture()
def setup():
    print("\nOpen URL")
    yield
    print("\nClose browser")


def test_SignupByEmail(setup):
    print("\nThis is signup by email test")


def test_SignupByFacebook(setup):
    print("\nThis is signup by Facebook test")


def test_SignupByTwitter(setup):
    print("\nThis is signup by Twitter test")
