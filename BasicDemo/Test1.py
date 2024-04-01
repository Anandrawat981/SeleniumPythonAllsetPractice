from selenium import webdriver
from selenium import *
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager.install()))
#driver.get("google.com")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/login")
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#driver.get("https://google.com")

username = driver.find_element("id","Email")
password = driver.find_element("id","Password")
login_button = driver.find_element("xpath","//*[text()='Log in']")
username.clear()
username.send_keys("admin@yourstore.com")
password.clear()
password.send_keys("admin")
login_button.click()
t=driver.title
expected_title ='Dashboard / nopCommerce administration'
print("Titile is : ",t)
if t == expected_title:
    print("Test case passed")
else:
    print("Titile not matched, Test case failed")
driver.close()
#assert t==expected_title, "Invalid Titile"

