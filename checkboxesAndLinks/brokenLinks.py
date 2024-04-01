from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests as requests


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME,"a")
count=0
print(len(allLinks))
# we need to install the requests package
for link in allLinks:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >=400:
        print(url,"Is broken link")
        count+=1
    else:
        print(url,"valid link, not broken link")

print("Total number of broken links are:",count)
print("Total number of valid links are:",len(allLinks)-count)
#driver.close()
#driver.quit()