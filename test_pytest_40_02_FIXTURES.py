import pytest


@pytest.yield_fixture()
def setup():
    print("\nThis is SETUP method. Will be run BEFORE "
          "each method in which specified \"setup\" as a parameter")
    yield           # teardown after each method executed
    print("\nThis method will be run AFTER "
          "each method in which specified \"setup\" as a parameter")

def testMethod1(setup):
    print("\nThis is Test method1")

def testMethod2(setup):
    print("\nThis is Test method2")

def testMethod3(setup):
    print("\nThis is Test method3")