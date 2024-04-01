from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#self node xpath
#text_mesg = driver.find_element(By.XPATH,"//a[contains(text(),'Indo C')]/self::a").text
#parent node xpath
#text_mesg = driver.find_element(By.XPATH,"//a[contains(text(),'NLC')]/parent::td").text
#print(text_mesg)
#Anscestor
#text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/child::td")
#lenmesg=len(text_mesgs)

#text_mesgs = driver.find_element(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr").text
#print(text_mesgs)
#descendeant  //a[contains(text(),'NLC')]/ancestor::tr/descendant::*
#text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/descendant::*")
#print(len(text_mesgs))
#sleep(3)

#fwllowing element
#text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/following::*")
#print(len(text_mesgs))

#following siblings
#text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/following-sibling::*")
#print(len(text_mesgs))
#precedings
#text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/preceding::tr")
#print(len(text_mesgs))
#preceding siblings
text_mesgs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC')]/ancestor::tr/preceding-sibling::tr")
print(len(text_mesgs))
sleep(3)
#driver.close()