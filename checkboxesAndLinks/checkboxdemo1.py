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
#driver.get("https://total-qa.com/checkbox-example/")
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()

checkboxs =driver.find_elements(By.XPATH,"//input[@type='checkbox']")

'''for checkbox in checkboxs:
    checkbox.click()
sleep(3)
for checkbox in checkboxs:
    #t.append(checkbox.get_attribute('value'))
    color1=checkbox.get_attribute('value')
    if color1 =='red' or color1 =='green' or color1 =='blue':
        checkbox.click() '''
#last two check box clicking
#for i in range(len(checkboxs)-2,len(checkboxs)):
#    checkboxs[i].click()

#select the two check box from starting
for i in range(len(checkboxs)):
    if i <2:
        checkboxs[i].click()

sleep(3)




#driver.close()
#driver.quit()