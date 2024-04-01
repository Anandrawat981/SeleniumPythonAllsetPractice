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
import os
location=os.getcwd()
print(location)

def chrome_setup():


    prefernaces={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    ops.add_argument("--headless")
    #ops.add_experimental_option("prefs",prefernaces)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
    return driver



def firefox_setup():
    preferences = {"download.default_directory": location}
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf") #"application/msword"
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2) #0-desktop 1=download floder, 2 -desried location
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True)
    ops.add_argument("--headless")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
    return driver

def edge_setup():
    prefernaces={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", prefernaces)
    ops.add_argument("--headless")
    driver =webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=ops)
    return driver
#driver=chrome_setup()
#driver=edge_setup()
driver = firefox_setup()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
print(driver.title)
print(driver.current_url)
