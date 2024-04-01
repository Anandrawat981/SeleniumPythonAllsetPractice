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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
element1 = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
element1.click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome Alien's")
sleep(3)
#alertwindow.accept() #this will accept the okay button
alertwindow.dismiss()
sleep(3)
result=driver.find_element(By.XPATH,"//p[@id='result']").text
print(result)
#driver.close()/
#driver.quit()