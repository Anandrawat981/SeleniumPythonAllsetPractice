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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
button=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act=ActionChains(driver)
#context_click is right click here
act.double_click(button).perform()
field1= driver.find_element(By.XPATH,"//input[@id='field1']").text
field2 =driver.find_element(By.XPATH,"//input[@id='field2']").text
if field2==field1:
    print("Pass test case")
else:
    print("Fail test case")