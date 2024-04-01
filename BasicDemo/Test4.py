from selenium import webdriver
from selenium import *
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
#//a[contains(@id,'u_')]
driver.find_element(By.XPATH,"//a[contains(@id,'u_')]").click()
sleep(3)
driver.close()