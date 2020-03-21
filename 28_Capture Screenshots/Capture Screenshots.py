from selenium import webdriver

link = "https://www.amazon.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
browser.maximize_window()

# save screenshot as png file
browser.save_screenshot("/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube/28_Capture Screenshots/screenshot.png")

browser.get_screenshot_as_file("/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube/28_Capture Screenshots/screen.jpg")
browser.quit()
