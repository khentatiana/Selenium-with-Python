from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/en-gb/"
link2 = "https://www.google.com/search?q=translate+english+to+russian&rlz=1C5CHFA_enUS889US889&oq=translate+english+to+russian&aqs=chrome..69i57j0l7.14489j0j7&sourceid=chrome&ie=UTF-8"
browser = webdriver.Chrome()
browser.get(link)
print(browser.title)
print(browser.current_url)
browser.close()

browser = webdriver.Chrome()
browser.get(link2)
print(browser.title)
print(browser.current_url)
browser.quit()
