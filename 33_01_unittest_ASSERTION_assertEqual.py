import unittest
from selenium import webdriver

class AssertionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()

    def test_Title(self):
        link = "https://www.bing.com/"
        browser = self.driver
        browser.get(link)
        browser.implicitly_wait(1)

        titleOfwebpage = browser.title

        self.assertEqual("Bing",titleOfwebpage, "Message will be shown if NOT equal here...")

if __name__ == "__main__":
    unittest.main()
