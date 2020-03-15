import time
from selenium import webdriver


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

count_input_feilds = browser.find_elements_by_css_selector("input[type=text]")
print(len(count_input_feilds))

browser.quit()
