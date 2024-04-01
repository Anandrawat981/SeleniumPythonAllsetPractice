from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()