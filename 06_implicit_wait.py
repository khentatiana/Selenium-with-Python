from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.newtours.demoaut.com/")

browser.implicitly_wait(5)

assert "Welcome: Mercury Tours" in browser.title
print(browser.title)
browser.quit()
