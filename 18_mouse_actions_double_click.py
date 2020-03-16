from selenium import webdriver
from selenium.webdriver import ActionChains
import time

link = "http://testautomationpractice.blogspot.com/"
browser = webdriver.Chrome()
browser.get(link)

browser.maximize_window()

button = browser.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

actions = ActionChains(browser)
actions.double_click(button).perform()

time.sleep(10)
browser.quit()