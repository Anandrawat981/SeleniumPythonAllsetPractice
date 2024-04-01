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

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
dropdown_ele = driver.find_elements(By.XPATH,"//select[@id='oldSelectMenu']//option")
for dropdown in dropdown_ele:
    if dropdown.text == 'Black':
        dropdown.click()
        break

sleep(3)
#driver.close()
#driver.quit()