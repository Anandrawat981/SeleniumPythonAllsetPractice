'''
https://www.Worldometers.info/world-population/
current world population
today :birth death and population growth
this year: birth deaths and population growth today

while(true)
{
keep getting element test using selenium
print it on console
//break the loop after few sec (20 sec)
}
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.nopcommerce.com/en")
#driver.find_element(By.LINK_TEXT,"Get started").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Get")
driver.close()
