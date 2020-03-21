import unittest
from selenium import webdriver

class Assertion_Not_Equal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()

    def test_notEqual(self):
        link = "https://www.bing.com/"
        self.driver.get(link)
        title = self.driver.title

        self.assertTrue("Bing"== title, "if FALSE (meaning equal), then will see this message")
if __name__ == "__main__":
    unittest.main()