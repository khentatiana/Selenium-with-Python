import unittest
from selenium import webdriver

class Assertion_IsNone(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome()
        self.assertIsNotNone(driver)


if __name__ == "__main__":
    unittest.main()