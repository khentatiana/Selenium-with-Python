import pytest


@pytest.fixture()
def setup():
    print("\nThis is SETUP method. "
          "Will be run before each method in which specified \"setup\" as a parameter")

def testMethod1(setup):
    print("\nThis is Test method1")

def testMethod2(setup):
    print("\nThis is Test method2")
