from selenium import webdriver
import time

link = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
browser = webdriver.Chrome()
browser.get(link)

browser.maximize_window()
browser.execute_script("window.scrollBy(0, 3000)", "")
time.sleep(5)

russian_flag = browser.find_element_by_xpath("//td[contains(text(),'Russia')]")
browser.execute_script("arguments[0].scrollIntoView();", russian_flag)
time.sleep(5)

browser.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)

browser.quit()

