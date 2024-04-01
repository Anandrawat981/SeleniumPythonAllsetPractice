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
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()
sleep(5)
'''#1. scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
sleep(5)
value=driver.execute_script("return window.pageYoffset;")
sleep(5)
print("Number of pixels moved:",value) '''

#scoll down page untill visible text
flag_IN=driver.find_element(By.XPATH,"//div[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();",flag_IN)
value1=driver.execute_script("return window.pageYoffset;") # this is javascript
print("Number of pixels moved:",value1)

#scoll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(4)
#scoll up to the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")