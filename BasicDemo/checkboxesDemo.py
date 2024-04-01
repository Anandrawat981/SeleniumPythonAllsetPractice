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
driver.get("https://app.endtest.io/guides/docs/how-to-test-checkboxes/")
driver.maximize_window()
#select specific checkbox or one
#checkbox=mywait.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='fs-checkbox-flag'])[2]")))
#checkbox.click()
#checkboxs=mywait.until(EC.presence_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))
#print(len(checkboxs))

# slecting all the check box
#for checkbox in checkboxs:
 #   checkbox.click()
#selecting checkbox by choice
# //input[@type='checkbox' and contains(@id,'pet')]
checkboxs =driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'pet')]")
#t =[]
for checkbox in checkboxs:
    #t.append(checkbox.get_attribute('value'))
    petname=checkbox.get_attribute('value')
    if petname =='rabbit' or petname =='cat' or petname =='dog':
        checkbox.click()
sleep(3)
print(petname)



#driver.close()
#driver.quit()