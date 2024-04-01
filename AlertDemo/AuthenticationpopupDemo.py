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
try:
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.maximize_window()
    result=driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credenti')]").text
    if result =="Congratulations! You must have the proper credentials.":
        print("Authication pass")
    print(result)
    sleep(10)
except:
    print('Authentication failed, Try again')
    sleep(10)

#driver.close()/
#driver.quit()