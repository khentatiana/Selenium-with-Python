from selenium import webdriver
import time

link = "http://testautomationpractice.blogspot.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

alert_button = browser.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
#To click OK on alert message
browser.switch_to_alert().accept()

#To click CANCEL on alert message
#browser.switch_to_alert().dissmiss()

time.sleep(10)
browser.quit()



