from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.facebook.com/")
#driver.find_element(By.LINK_TEXT,"Get started").click()
#d=driver.find_element(By.CSS_SELECTOR,'input#email')
#d=driver.find_element(By.CSS_SELECTOR,'input.inputtext')
d=driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]')
d1=driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_pass]')


d.send_keys('abc')
d1.send_keys('test1')
sleep(3)
driver.close()
