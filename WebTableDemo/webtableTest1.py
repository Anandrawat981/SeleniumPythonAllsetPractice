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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#Count no of rows and columns
webTable_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print("No of rows: ",len(webTable_rows))
webTable_colums = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th")
print("No of columns:",len(webTable_colums))
#Read specific row and columns data
oneElemnet=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
print(oneElemnet.text)
f = open('data.xls', "w+")
#Read all rows and columns data
for r in range(2,len(webTable_rows)+1):
    for c in range(1,len(webTable_colums)+1):
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end=' ----> ')
        f.write(data)
    print()
f.close()

#Read data based on conditions[List books name whose author is Mukesh]

print("#Read data based on conditions[List books name whose author is Mukesh]")

for r in range(2,len(webTable_rows)+1):
    authorname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authorname == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        priceDetails = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print("Book name is :",bookName,"|| Author is :",authorname,"|| Price is :",priceDetails)






