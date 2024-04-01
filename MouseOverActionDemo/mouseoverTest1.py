from selenium import webdriver
import datetime
import time
from time import *

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://jqueryui.com/")
driver.maximize_window()
'''sleep(8)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(5)'''

ele1=driver.find_element(By.XPATH,"//a[text()='Contribute']")
sleep(2)
ele2=driver.find_element(By.XPATH,"//a[text()='Bug Triage']")
#Users=driver.find_element(By.LINK_TEXT,"Users")
act=ActionChains(driver)
#act.move_to_element(admin1).move_to_element(userManag).move_to_element(Users).click().perform()
act.move_to_element(ele1).move_to_element(ele2).click().perform()
