from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/en-gb/"
link2 = "https://docs.google.com/document/d/1UUfFl69by0QUzxo7EIQj3keyeAsz2XJqTHKjAA2YaUE/edit"
browser = webdriver.Chrome()
browser.get(link)
print(browser.title + "\nShould be printed above: Oscar - Sandbox")
browser.get(link2)
print(browser.title + "\nShould be printed above: \"Google Docs: Sign-in\"")
browser.back()
print(browser.title + "\nShould be printed above: Oscar - Sandbox" )
browser.forward()
print(browser.title + "\nShould be printed above: \"Google Docs: Sign-in\"")
browser.quit()