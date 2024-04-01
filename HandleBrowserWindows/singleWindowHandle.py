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

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
windowID=driver.current_window_handle
#print(windowID) #fab73f95-27e9-4c19-a2f1-2ed3deab8f1d
sleep(2)
#entry2=driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
entry2 =mywait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")))
entry2.click()
#entry3 =driver.find_element(By.LINK_TEXT,"Open Source HRMS")
#entry3 =mywait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Open Source HRMS")))
#entry3.click()
#sleep(3)
#driver.find_element(By.LINK_TEXT,"Privacy Policy").click()

windowIDs= driver.window_handles
'''#Approach 1
#print(windowIDs)
parentWindowID = windowIDs[0]
childWindowID = windowIDs[1]
sleep(2)
driver.switch_to.window(parentWindowID)
print(driver.title)
sleep(2)
driver.switch_to.window(childWindowID)
print(driver.title)
sleep(3)
driver.close()'''

#Approach 2
'''for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)
    driver.close()'''

for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title == 'OrangeHRM':
        driver.close()




#driver.quit()