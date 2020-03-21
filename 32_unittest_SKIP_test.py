import unittest

class SkippingTest(unittest.TestCase):
    def test_search(self):
        print("\n1.This is search test")
    def test_login(self):
        print("\n2.This is login test")
    def test_register(self):
        print("\n3.This is register test")
    def test_clean(self):
        print("\n4.This is clean test")

# TO SKIP TEST ADD decorator @unittest.SkipTest in from of the test
    @unittest.SkipTest
    def test_skip(self):
        print("\n5.This is skip test")
# TO SKIP TEST ADD decorator @unittest.skip("Write message here")
    @unittest.skip("Test is skipped because of the following reason....")
    def test_skip(self):
        print("\n6.This is skip test with message")
# TO SKIP TEST ADD  with condition decorator @unittest.skipIf(1 == 1, "Message if failed:)
    @unittest.skipIf(1 == 1, "If condition is met, then test is skipped. "
                             "If condition \"1==1\" is FALSE, the his test will run")
    def test_skip(self):
        print("\n7.This is skip test with condition")

if __name__ == "__main__":
    unittest.main()