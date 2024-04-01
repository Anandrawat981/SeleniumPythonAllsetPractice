from selenium import webdriver
import datetime
import time
from time import *

from selenium.webdriver import ActionChains
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
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

ele1=driver.find_element(By.XPATH,"//span[@class='ng-tns-c58-10 ui-calendar']")
ele1.click()
sleep(2)
month='March'
year='2025'
date='29'



month1 = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month ng-tns-c58-10 ng-star-inserted']").text
year1 = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year ng-tns-c58-10 ng-star-inserted']").text
print(month1,year1)