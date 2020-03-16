from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

link = "https://www.expedia.com/"

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
browser.maximize_window()


flight_tab = browser.find_element_by_xpath("//span[contains(text(),'Flights')]")
flight_tab.click()

roundtrip_btn = browser.find_element_by_id("flight-type-roundtrip-label-hp-flight")
roundtrip_btn.click()

from_input = browser.find_element_by_id("flight-origin-hp-flight")
from_input.send_keys("SFO")

destination_input = browser.find_element_by_id("flight-destination-hp-flight")
destination_input.send_keys("NYC")

departing_date = browser.find_element_by_id("flight-departing-hp-flight").send_keys("05/01/2020")
returning_date = browser.find_element_by_id("flight-returning-hp-flight").send_keys("05/08/2020")
travelers = browser.find_element_by_id("traveler-selector-hp-flight").click()

search_btn = browser.find_element_by_class_name("btn-primary.btn-action.gcw-submit").click()

assert "SFO to NYC Flights | Expedia" in browser.title

#explicit wait
wait = WebDriverWait(browser, 10)
nonstop_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
nonstop_checkbox.click()

time.sleep(5)


browser.quit()
