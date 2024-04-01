from selenium import webdriver
import datetime
import time
from time import *

from selenium.webdriver import ActionChains, Keys
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
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
#sleep(5)
input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome to World of Aelin's")
#ctrl+A
#ctrl+c
#tab
#ctrl+v
act=ActionChains(driver)
#ctrl+A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
##ctrl+c on same input 1 box
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#tab to naviagate to next input box
act.send_keys(Keys.TAB).perform()
##ctrl+v on input 2
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
