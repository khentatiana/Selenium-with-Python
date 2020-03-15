from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "https://fs2.formsite.com/R1Tuim/form1/index.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

dropdown_elements = browser.find_element_by_id("RESULT_RadioButton-6")
dropdown = Select(dropdown_elements)
#select by visible text
dropdown.select_by_visible_text("M")
print("should be M")
time.sleep(5)

#select by index
dropdown.select_by_index(2)
print("should be F")
time.sleep(5)

#select by value
dropdown.select_by_value("Radio-0")
print("should be M")
time.sleep(5)

browser.quit()