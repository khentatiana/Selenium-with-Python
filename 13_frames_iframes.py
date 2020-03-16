from selenium import webdriver
import time

link = "https://www.w3schools.com/html/default.asp"
browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
browser.get(link)
browser.implicitly_wait(5)

#browserwitch_to.frame("frame_name")
iframe = browser.switch_to.frame("google_ads_iframe_/22152718/sws-hb//w3schools.com//mid_content_0")


time.sleep(10)
browser.quit()
