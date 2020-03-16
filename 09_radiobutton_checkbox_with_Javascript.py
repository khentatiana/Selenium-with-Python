from selenium import webdriver
import time

link = "https://www.trulia.com/"
browser = webdriver.Chrome()
browser.get(link)

search = browser.find_element_by_id("banner-search").clear().send_keys("San Jose, CA")
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
browser.execute_script("document.getElementById("uniform-layered_id_attribute_group_2").checked())
time.sleep(5)
browser.delete_all_cookies()
browser.quit()