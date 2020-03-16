from selenium import webdriver
import time
from selenium.webdriver import ActionChains

link = "https://opensource-demo.orangehrmlive.com/"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_id("txtUsername").send_keys("Admin")
browser.find_element_by_id("txtPassword").send_keys("admin123")
browser.find_element_by_id("btnLogin").click()

admin = browser.find_element_by_id("menu_admin_viewAdminModule")
user_management = browser.find_element_by_id("menu_admin_UserManagement")
users = browser.find_element_by_id("menu_admin_viewSystemUsers")

mouse_actions = ActionChains(browser)
mouse_actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

time.sleep(10)
browser.quit()