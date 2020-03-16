from selenium import webdriver
from selenium.webdriver import ActionChains
import time

link = "http://testautomationpractice.blogspot.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

source_element = browser.find_element_by_id("draggable")
target_element = browser.find_element_by_id("droppable")

action = ActionChains(browser)
action.drag_and_drop(source_element, target_element).perform()

time.sleep(5)

browser.quit()