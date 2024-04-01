from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
'''
find_elements retun as list collection
find _element return webelement

three conditions:
This is in case of find _element 
1. locator matching with single webelement -perform singe action
2. locator maching with mutiple weblement - perform action on 1st elemts and single element
3. Element not then throw NoSuchELementExpection

three conditions:
This is in case of find _elements 
1. locator matching with single webelement -returning single value or performing single actions
2. locator maching with mutiple weblement - retuenning mi=uyiple elements
3. Element not then does not throw anything

'''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
element=driver.find_element(By.XPATH,"//input[@id='Email']")
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