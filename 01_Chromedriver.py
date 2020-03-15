from selenium import webdriver

def browser():
	link = "http://selenium1py.pythonanywhere.com"
	browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
	browser.get(link)
	print(browser.title)
