from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

link = "http://demo.automationtesting.in/Windows.html"
browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
browser.get(link)
browser.implicitly_wait(5)

# current window handle(parent window)
print("Parent window title:", browser.title)
print("Parent window handle:", browser.current_window_handle)

browser.find_element_by_xpath("//a[contains(text(),'Open New Tabbed Windows')]").click()
browser.find_element_by_class_name("btn.btn-info").click()

browser.find_element_by_xpath("//a[contains(text(),'Open New Seperate Windows')]").click()
browser.find_element_by_class_name("btn.btn-primary").click()

if browser.title == "Frames & windows":
    browser.close()
    print("Parent window is closed")

# returns all the handle values of opened windows
handels = browser.window_handles
for single_handle in handels:
    browser.switch_to.window(single_handle)

print("Child window title:", browser.title)
print("Child window handle:", browser.current_window_handle)

browser.quit()
print("closed all windows")
