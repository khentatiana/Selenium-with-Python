from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
#To specify download location instaed of default of Chrome browser
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory":"/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube"})


link = "http://demo.automationtesting.in/FileDownload.html"
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get(link)

browser.find_element_by_id("textbox").send_keys("some text to create txt file")
browser.find_element_by_id("createTxt").click()
browser.find_element_by_id("link-to-download").click()

browser.find_element_by_id("pdfbox"). send_keys("some text to create txt file")
browser.find_element_by_id("createPdf").click()
browser.find_element_by_id("pdf-link-to-download").click()


browser.quit()