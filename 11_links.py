from selenium import webdriver
import time

link = "http://www.newtours.demoaut.com/"

browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
browser.get(link)
browser.implicitly_wait(5)

links = browser.find_elements_by_tag_name("a")
#count number of links on the webpage
print("Number of links on this webpage is", len(links))

#read all links on the page
for single_link in links:
    print(single_link.text)
#how to click on link

browser.find_element_by_link_text("REGISTER").click()
assert "Register:" in browser.title
browser.back()

browser.find_element_by_partial_link_text("REG").click()
assert "Register: Mercury Tours" in browser.title

time.sleep(5)

browser.quit()