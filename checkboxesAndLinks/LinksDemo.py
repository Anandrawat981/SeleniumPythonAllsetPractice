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

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()

'''link1 =driver.find_element(By.LINK_TEXT,"HTML Tutorials")  #mostly we use this link_text only  
#link1 =driver.find_element(By.PARTIAL_LINK_TEXT,"HTML ")  
sleep(3)
link1.click()
sleep(3) '''

#case 2: total number of links in page
links2=driver.find_elements(By.TAG_NAME,'a')
print("Total number of links:", len(links2))
f=open('link_text.txt','w+')

#now print all the links
for link in links2:
    f.write(link.text+'\n')
    print()
    #print(link.text)
f.close()

#driver.close()
#driver.quit()