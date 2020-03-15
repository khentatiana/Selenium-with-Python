from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

link = "http://selenium1py.pythonanywhere.com/"
browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
browser.get(link)
print(browser.title)
browser.quit()
