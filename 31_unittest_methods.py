import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("\nInitiate driver....")

    @classmethod
    def tearDown(self):
        browser = self.driver
        browser.quit()
        print("\nQuit browser....")
    @classmethod
    def setUpClass(cls):
        print("\nOpen application...")

    @classmethod
    def tearDownClass(cls):
        print("\nClose application...")

    def test_Google(self):
        link = "https://www.google.com/"
        browser = self.driver
        browser.get(link)

        print("\nThe title og this webpage is: ", browser.title)

    def test_Bing(self):
        link = "https://www.bing.com/"
        browser = self.driver
        browser.get(link)
        print("\nThe title og this webpage is: ", browser.title)




if __name__ == "__main__":
    unittest.main()

