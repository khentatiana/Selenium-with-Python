import unittest


class LoginTest(unittest.TestCase):
    def test_LoginByEmail(self):
        print("\nThis is login by email test")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("\nThis is login by Facebook test")
        self.assertTrue(True)

    def test_ByTwitter(self):
        print("\nThis is login by Twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
