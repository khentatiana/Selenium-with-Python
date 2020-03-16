from selenium import webdriver
from selenium.webdriver import ActionChains
import time

link = "http://testautomationpractice.blogspot.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
#upload file element is located inside frame. nee to switch to frame first
browser.switch_to.frame(0)

browser.find_element_by_id("RESULT_FileUpload-10").send_keys("/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube/01_youtube_url")
time.sleep(5)

browser.quit()
