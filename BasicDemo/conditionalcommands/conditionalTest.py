from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/login")
#is_displayed ,is_enabled
entry1=driver.find_element(By.XPATH,"//input[@id='Email']")
print(entry1.is_enabled())
print(entry1.is_displayed())
entry2=driver.find_element(By.XPATH,"//input[@id='RememberMe']")
print(entry2.is_selected())
entry2.click()
print(entry2.is_selected())
sleep(2)



sleep(3)
driver.close()