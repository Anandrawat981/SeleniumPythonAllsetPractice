from selenium import webdriver
import datetime
import time
from time import *

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

import mysql.connector

try:

    connection1 = mysql.connector.connect(host="localhost", port=3306, user="root", password="Future@981",
                                              database="mydb")
    corsor = connection1.cursor()
    corsor.execute("select *from sys_configcal")
    for rows in corsor:
        price1 =rows[0]
        rateofInterest1 =rows[1]
        period_year_num =rows[2]
        period_year_text =rows[3]
        frequecy1 =rows[4]
        Expected_maturity_value1 =rows[5]

        # Pass the data to the application for text

        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(price1)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofInterest1)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period_year_num)
        # select1 = driver.find_element(By.XPATH,"//select[@id='tenurePeriod']")
        # period_dropdown = Select(select1)
        period_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        period_dropdown.select_by_visible_text(period_year_text)
        frequecy_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequecy_dropdown.select_by_visible_text(frequecy1)
        driver.find_element(By.XPATH, "//a[@onclick='return getfdMatVal(this);']").click()
        Actual_maturityValue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # Validation

        if float(Actual_maturityValue) == float(Expected_maturity_value1):
            print("Test Passed")

        else:
            print("Test Fail")
        driver.find_element(By.XPATH, "//a[@onclick='javascript:reset_fdcalcfrm();']").click()
        sleep(3)
    corsor.close()
    connection1.close()
except:
    print("connection broken______")

