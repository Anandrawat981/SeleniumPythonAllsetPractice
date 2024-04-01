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
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
#driver.switch_to.frame("iframeResult")
target1=driver.find_element(By.XPATH,"//div[@id='box106']")
source1=driver.find_element(By.XPATH,"//div[@id='box1']")
source2=driver.find_element(By.XPATH,"//div[@id='box3']")
target2=driver.find_element(By.XPATH,"//div[@id='box103']")

target3 =driver.find_element(By.XPATH,"//div[@id='dropContent']")


act=ActionChains(driver)
act.drag_and_drop(source1,target1).perform() #drag and drop operation
act.drag_and_drop(source2,target2).perform()
act.drag_and_drop(source1,target3).perform()