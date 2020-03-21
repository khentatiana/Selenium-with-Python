from selenium import webdriver

link = "https://www.amazon.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

# capture all the cookies created by browser
cookies = browser.get_cookies()

# print number of cookies have been created
print(len(cookies))

# print all the cookie pairs
print(cookies)

# adding new cookie to the browser
new_cookie = {'name': "Mycookie", 'value': "1234565"} # cookie is dictionary
browser.add_cookie(new_cookie)
# check that new cookie is added
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)

# delete cookie from the browser. You need the 'name' of the cookie
browser.delete_cookie("Mycookie")
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)

# delete all the cookies from the browser
browser.delete_all_cookies()
cookies_cleaned = browser.get_cookies()
print(len(cookies_cleaned))
print(cookies_cleaned)

browser.quit()