from selenium import webdriver
import datetime
import time
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
driver.get("https://jqueryui.com/datepicker/")

driver.maximize_window()
frame1=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame1)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/11/2024")
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
month = "June"
year = "2025"
date = "9"
while True:
    mn=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mn==month and yr==year :
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break

#Test2
#if datetime