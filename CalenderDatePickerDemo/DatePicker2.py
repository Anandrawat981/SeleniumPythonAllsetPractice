from selenium import webdriver
import datetime
import time
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='dob']").click()
months=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
datepicker_months =Select(months)
datepicker_months.select_by_visible_text("Nov")
years=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
datepicker_years =Select(years)
datepicker_years.select_by_visible_text("1997")
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a")

for date in alldates:
    if date.text == "10":
        date.click()
        break



