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


dropdown_ele = driver.find_element(By.XPATH,"//select[@id='oldSelectMenu']")
dropdown=Select(dropdown_ele)
'''dropdown.select_by_visible_text("Indigo")
sleep(3)
dropdown.select_by_index(8)
sleep(3)
dropdown.select_by_value("9")
sleep(3)'''

#capture all th option and print
alloptions=dropdown.options
print("Total number of options:",len(alloptions))
'''for alloption in alloptions:
    print(alloption.text)'''
for alloption in alloptions:
    if alloption.text == 'White':
        alloption.click()
        break

sleep(3)
#driver.close()
#driver.quit()