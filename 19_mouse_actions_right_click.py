from selenium import webdriver
from selenium.webdriver import ActionChains
import time

link = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

button = browser.find_element_by_class_name("context-menu-one.btn.btn-neutral")
actions = ActionChains(browser)
actions.context_click(button).perform()

time.sleep(5)

browser.quit()