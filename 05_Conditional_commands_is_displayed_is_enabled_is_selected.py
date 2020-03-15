from selenium import webdriver
import time

link = "http://www.newtours.demoaut.com/"
browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
browser.get(link)
browser.implicitly_wait(5)

print(browser.title)

user_element = browser.find_element_by_name("userName")
print("user_element:")
print(user_element.is_displayed())
print(user_element.is_enabled())

pw_element = browser.find_element_by_name("password")
print("pw_element:")
print(pw_element.is_displayed())
print(pw_element.is_enabled())

user_element.send_keys("mercury")
pw_element.send_keys("mercury")
button = browser.find_element_by_name("login")
button.click()
print("new title is:" + browser.title)

radio_btn_rountrip = browser.find_element_by_css_selector("input[value=roundtrip]")
print("radio_btn_rountrip:")
print("If True, then radio button is checked:", radio_btn_rountrip.is_selected())

radio_btn_onewaytrip = browser.find_element_by_css_selector("input[value=oneway]")
print("oneway:")
print("If True, then radio button is checked:", radio_btn_onewaytrip.is_selected())

browser.quit()

link2 = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link2)

button = browser.find_element_by_class_name("btn.btn-default")
print("The submit button sb.b. disabled, display false:", button.is_enabled())
input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
input1.send_keys("Tanya")
input2= browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
input2.send_keys("Khen")
input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
input3.send_keys("tkhen@gmail.com")
time.sleep(5)

print("The submit button sb.b. disabled, display True:", button.is_enabled())
button.click()

browser.quit()