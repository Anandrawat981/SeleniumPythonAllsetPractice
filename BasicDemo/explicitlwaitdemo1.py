from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
element=mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='Email']")))
#element=driver.find_element(By.XPATH,"//input[@id='Email']")
element.clear()
element.send_keys("Anand@gmail.com")
print(type(element))
print(element.get_attribute("value"))
print("Text is : ",element.text)
element1=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print(element1.text)
print("Attribute is :",element1.get_attribute("type"))

#driver.close()
driver.quit()