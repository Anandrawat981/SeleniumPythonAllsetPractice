from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests as requests


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
outerFrame = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outerFrame)
InnerFrame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(InnerFrame)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
#driver.switch_to.parent_frame()
driver.switch_to.default_content()
sleep(3)
driver.find_element(By.XPATH,"//a[text()='WebTable']").click()
sleep(3)

#driver.close()/
#driver.quit()