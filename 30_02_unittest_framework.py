import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Google(self):
        link = "https://www.google.com/"
        browser = self.driver
        browser.get(link)

        print("\nThe title og this webpage is: ", browser.title)
        browser.close()

    def test_Bing(self):
        link = "https://www.bing.com/"
        browser = self.driver
        browser.get(link)
        print("\nThe title og this webpage is: ", browser.title)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

