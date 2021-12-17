# To access HTML web table elements

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys, window
from selenium.webdriver.common.by import By
import time
import os

cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://sqengineer.com/practice-sites/practice-tables-selenium/")
driver.maximize_window()
driver.implicitly_wait(2)

# count number of rows and columns
rows= len(driver.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr"))
cols= len(driver.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr[1]/th"))

# Header
print("AUTOMATION TOOL "+"   TYPE "+"     LINK ")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        table_item=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(table_item, end="    ")
        if c==3:
           ele=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]/a")
           link=ele.get_attribute("href")
           print("link=",link)
                      #driver.find_element(By.TAG_NAME,"body").send_keys(Keys.CONTROL + 't')
           driver.execute_script('''window.open(" ","_blank");''')

    print()

