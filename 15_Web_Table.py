from selenium import webdriver

link = "http://testautomationpractice.blogspot.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

#count number of rows including table header
table_rows = len(browser.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))
print("Table has", table_rows, "rows.")
#count number of table_columns
table_columns = len(browser.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td"))
print("Table has", table_columns, "columns.")

#to print table
for r in range(2, table_rows + 1):
    for c in range(1, table_columns + 1):
        #copy xpath for the cell element:    //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1] and modify as below
        value = browser.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        #print each cell value following by space
        print(value, end=' ')
    #print each row following by transfering to new line
    print()
browser.quit()






