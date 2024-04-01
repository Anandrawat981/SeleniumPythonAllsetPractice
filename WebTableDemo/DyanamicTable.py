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

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(10)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(5)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
sleep(5)
driver.find_element(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item' and text()='User Management ']").click()
driver.find_element(By.LINK_TEXT,"Users").click()
