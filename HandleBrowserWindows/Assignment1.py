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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
sleep(2)
entry2 =mywait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@class='wikipedia-search-input']")))
entry2.send_keys("selenium")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
results=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']")
sleep(3)
windowIDs= driver.window_handles
for result in results:
    print(result.text)
    sleep(3)
    #result.click()
for windowid in windowIDs:
    resclick = driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']")
    resclick.click()
    driver.switch_to.window(windowid)
    print(driver.title)
    driver.find_element(By.XPATH,"//a[normalize-space()='Selenium (software)']")
    driver.switch_to.window(windowid)

sleep(3)

#for c in resclick:
#    c.click()


'''for windowid in windowIDs:
    driver.switch_to.window(windowid)
    print(driver.title)'''












#driver.quit()