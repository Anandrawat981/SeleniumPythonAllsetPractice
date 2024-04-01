from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests as requests


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("https://www.w3.org/WAI/UA/TS/html401/cp0101/0101-FRAME-TEST.html")
driver.maximize_window()
#//frame[@name='head']
driver.switch_to.frame("head")
element1 = driver.find_element(By.LINK_TEXT,"HTML 4.01 specification for FRAME")
sleep(3)
element1.click()
driver.switch_to.default_content()
sleep(3)
driver.switch_to.frame("target1")
driver.find_element(By.LINK_TEXT,"Test Link 1").click()
driver.switch_to.default_content()
sleep(3)
driver.switch_to.frame("target2")
driver.find_element(By.LINK_TEXT,"Test Link 2").click()
driver.switch_to.default_content()
sleep(3)
#driver.close()/
#driver.quit()