import unittest


class SignupTest(unittest.TestCase):
    def test_SignupByEmail(self):
        print("\nThis is signup by email test")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("\nThis is signup by Facebook test")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("\nThis is signup by Twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()