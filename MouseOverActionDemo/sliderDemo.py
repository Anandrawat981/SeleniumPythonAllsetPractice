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
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
driver.maximize_window()
#driver.switch_to.frame("iframeResult")
min_slider = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
max_slider = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")
print("Location of Slider before moving")
print(min_slider.location) #{'x': 59, 'y': 251}
print(max_slider.location) #{'x': 517, 'y': 251}
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,251).perform()
act.drag_and_drop_by_offset(max_slider,-100,251).perform()
print("Location of Slider after moving")
print(min_slider.location) #
print(max_slider.location) #