from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://automationpractice.com/index.php?id_category=8&controller=category"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

checkbox = browser.find_element_by_xpath("//div[@id='uniform-layered_id_attribute_group_1']")
checkbox.click()
time.sleep(2)
print(checkbox.is_enabled())


browser.quit()
